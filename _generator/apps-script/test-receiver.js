/* Runs Code.gs against stubbed Google services to check routing,
   header sync and value flattening without deploying. */
const fs = require("fs");
const src = fs.readFileSync(require("path").join(__dirname, "Code.gs"), "utf8");

class Sheet {
  constructor(name){ this.name=name; this.rows=[]; }
  getLastColumn(){ return this.rows.length ? this.rows[0].length : 0; }
  getLastRow(){ return this.rows.length; }
  setFrozenRows(){} 
  appendRow(r){ this.rows.push(r.slice()); }
  getRange(r,c,nr,nc){
    const self=this;
    return {
      setValues(v){ while(self.rows.length<r) self.rows.push([]); 
                    const row=self.rows[r-1]; v[0].forEach((x,i)=>row[c-1+i]=x); },
      getValues(){ const row=self.rows[r-1]||[]; const out=[];
                   for(let i=0;i<nc;i++) out.push(row[c-1+i]===undefined?"":row[c-1+i]); return [out]; },
      setFontWeight(){}
    };
  }
}
const sheets = {};
const SpreadsheetApp = { getActiveSpreadsheet: () => ({
  getSheetByName: n => sheets[n] || null,
  insertSheet: n => (sheets[n] = new Sheet(n)),
  getUrl: () => "https://docs.google.com/spreadsheets/d/FAKE"
})};
const LockService = { getScriptLock: () => ({ waitLock(){}, releaseLock(){} }) };
const driveFiles = [];
const DriveApp = { getRootFolder: () => folder("root") };
function folder(name){ return {
  getName:()=>name,
  getFoldersByName:()=>({hasNext:()=>false,next:()=>null}),
  createFolder:n=>folder(n),
  createFile:b=>{ driveFiles.push({folder:name, name:b.name, bytes:b.bytes});
                  return { getUrl:()=>"https://drive.google.com/file/d/FAKE_"+b.name }; }
};}
const Utilities = {
  base64Decode: s => Array.from(Buffer.from(s,"base64")),
  newBlob: (bytes,type,name) => ({bytes,type,name}),
  formatDate: () => "2026-09-30 10:00"
};
const Session = { getScriptTimeZone: () => "UTC" };
const mails = [];
const MailApp = { sendEmail: o => mails.push(o) };
const ContentService = { MimeType:{JSON:"json"},
  createTextOutput: t => ({ setMimeType(){ return { body:t }; } }) };

const ctx = { SpreadsheetApp, LockService, DriveApp, Utilities, Session, MailApp, ContentService, console };
const fn = new Function(...Object.keys(ctx), src + "\n;return {doPost,doGet,CONFIG};");
const api = fn(...Object.values(ctx));
const TOKEN = api.CONFIG.TOKEN;
/* Pin the notification setting so these tests pass whatever CONFIG ships with. */
api.CONFIG.NOTIFY_EMAIL = "";

const call = (payload) => JSON.parse(api.doPost({ postData:{ contents: JSON.stringify(payload) } }).body);
const show = (t) => { const s=sheets[t]; return s ? s.rows : null; };
let pass = 0, fail = 0;
const check = (label, cond, extra) => { cond ? pass++ : fail++;
  console.log((cond?"  PASS  ":"  FAIL  ") + label + (cond?"":"  -> "+JSON.stringify(extra))); };

console.log("\n-- rejections --");
check("bad token rejected", call({token:"wrong",form:"consultation",fields:{}}).status==="error");
check("unknown form rejected", call({token:TOKEN,form:"../../evil",fields:{}}).status==="error");
check("malformed JSON rejected",
  JSON.parse(api.doPost({postData:{contents:"{not json"}}).body).status==="error");
check("empty request rejected", JSON.parse(api.doPost({}).body).status==="error");
check("nothing written by rejected calls", Object.keys(sheets).filter(k=>k!=="_errors").length===0, Object.keys(sheets));

console.log("\n-- consultation --");
check("accepted", call({token:TOKEN,form:"consultation",
  fields:{name:"A Person",email:"a@example.com",country:"Portugal"}}).status==="ok");
let rows = show("consultation");
check("header row present", rows[0][0]==="received_at" && rows[0][1]==="form", rows[0]);
check("lead columns kept in order", rows[0].slice(0,7).join(",")==="received_at,form,first_name,last_name,email,phone,country", rows[0]);
check("email landed in its lead column", rows[1][4]==="a@example.com", rows[1]);
check("new field got appended as a column", rows[0].includes("name"), rows[0]);

console.log("\n-- provider-match: arrays, booleans, uploads --");
const r2 = call({token:TOKEN,form:"provider-match",
  fields:{first_name:"Test",email:"m@example.com",indications:["opioid","trauma"],
          consent_share:true,consent_marketing:false,flags:["flag_withdrawal"]},
  files:[{name:"ecg.pdf",type:"application/pdf",data:Buffer.from([37,80,68,70,255,0]).toString("base64")}]});
check("accepted", r2.status==="ok");
rows = show("provider-match");
const col = n => rows[0].indexOf(n);
check("array joined with semicolons", rows[1][col("indications")]==="opioid; trauma", rows[1][col("indications")]);
check("true -> yes", rows[1][col("consent_share")]==="yes", rows[1][col("consent_share")]);
check("false -> no  (not blank)", rows[1][col("consent_marketing")]==="no", rows[1][col("consent_marketing")]);
check("upload link in row", String(rows[1][col("uploads")]).startsWith("https://drive.google.com/"), rows[1][col("uploads")]);
check("file bytes preserved", JSON.stringify(driveFiles[0].bytes)===JSON.stringify([37,80,68,70,255,0]), driveFiles[0].bytes);
check("routed to its own tab", show("consultation").length===2 && rows.length===2);

console.log("\n-- schema drift: a new question added later --");
call({token:TOKEN,form:"provider-match",fields:{email:"b@example.com",brand_new_question:"42"}});
rows = show("provider-match");
check("new column appended", rows[0].includes("brand_new_question"), rows[0]);
check("old row not corrupted", rows[1][col("indications")]==="opioid; trauma");
check("new row aligned under new column", rows[2][rows[0].indexOf("brand_new_question")]==="42", rows[2]);
check("absent fields blank, not shifted", rows[2][col("consent_share")]==="", rows[2]);

console.log("\n-- notifications --");
mails.length = 0;
call({token:TOKEN,form:"consultation",fields:{email:"quiet@example.com"}});
check("silent when NOTIFY_EMAIL empty", mails.length===0, mails.length);

api.CONFIG.NOTIFY_EMAIL = "one@example.com,two@example.com";
mails.length = 0;
call({token:TOKEN,form:"consultation",fields:{email:"n@example.com",situation:"notify test"}});
check("one email sent for two recipients", mails.length===1, mails.length);
check("both recipients on it", mails[0] && mails[0].to==="one@example.com,two@example.com", mails[0] && mails[0].to);
check("subject names the form", mails[0] && mails[0].subject.indexOf("consultation")!==-1, mails[0] && mails[0].subject);
check("body carries the fields", mails[0] && mails[0].body.indexOf("notify test")!==-1);

/* a broken notification must not cost us the row */
const rowsBefore = show("consultation").length;
const realSend = MailApp.sendEmail;
MailApp.sendEmail = () => { throw new Error("quota exceeded"); };
const r3 = call({token:TOKEN,form:"consultation",fields:{email:"resilient@example.com"}});
MailApp.sendEmail = realSend;
check("row still written when email throws", r3.status==="ok" && show("consultation").length===rowsBefore+1,
      {status:r3.status, before:rowsBefore, after:show("consultation").length});
api.CONFIG.NOTIFY_EMAIL = "";

console.log(`\n${pass} passed, ${fail} failed\n`);
process.exit(fail ? 1 : 0);
