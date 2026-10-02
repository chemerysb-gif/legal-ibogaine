# Connecting the forms to Google Sheets

One-time setup, about ten minutes. You need a Google account.

## 1. Make the spreadsheet

1. Go to <https://sheets.new> and name it something like **Legal Ibogaine — submissions**.
2. You do not need to add any tabs or headers. The script creates a tab per form
   (`screening-quiz`, `provider-match`, `consultation`, `resource-gate`) and writes
   the header row the first time each one receives something.

## 2. Make up a token

Invent a long random string — 30+ characters, letters and numbers. Example shape:

    lg7Qx2vNb8ZpR4tW9cKmY6hJ3dF5sA1uE0

This is a shared secret between the site and the script. It keeps casual junk out
of the sheet. Keep it somewhere you can find it; you paste it in two places below.

## 3. Install the script

1. In the spreadsheet: **Extensions → Apps Script**.
2. Delete whatever is in `Code.gs`, then paste in the entire contents of
   `_generator/apps-script/Code.gs` from this repo.
3. At the top of the file, edit `CONFIG`:
   - `TOKEN` — the string from step 2.
   - `NOTIFY_EMAIL` — your address if you want an email on each submission,
     or leave it as `""` for none. For more than one recipient, separate them
     with commas and no spaces:
     `"you@legal-ibogaine.com,partner@example.com"` — everyone listed gets an
     identical copy, including whatever health details the visitor submitted.
   - `UPLOAD_FOLDER` — leave as-is unless you want a different Drive folder name.
4. Save (the disk icon).

## 4. Deploy it

1. **Deploy → New deployment**.
2. Click the gear next to "Select type" and choose **Web app**.
3. Set:
   - **Execute as:** Me
   - **Who has access:** **Anyone**
4. Click **Deploy**.
5. Google will ask you to authorise it. It shows a scary "Google hasn't verified
   this app" screen — this is normal for your own scripts. Click **Advanced**,
   then **Go to (project name) (unsafe)**, then **Allow**.
6. Copy the **Web app URL**. It looks like:

       https://script.google.com/macros/s/AKfycb.../exec

**Check it worked:** paste that URL into a browser tab. You should see
`{"status":"ok","message":"Legal Ibogaine form receiver is running..."}`.

## 5. Point the site at it

Open `js/main.js`. The first few lines hold:

    var ENDPOINT = "PASTE_YOUR_APPS_SCRIPT_URL_HERE";
    var TOKEN = "REPLACE_WITH_A_LONG_RANDOM_STRING";

Replace both — the URL from step 4, and the same token from step 2. The token
must match `CONFIG.TOKEN` in the script exactly.

Until you do this, every form shows a "not connected yet" notice instead of
submitting, and nothing is lost.

## 6. Deploy the site

    netlify deploy --prod

## Changing the script later

Editing the code is not enough — you must redeploy for changes to go live:
**Deploy → Manage deployments → pencil icon → Version: New version → Deploy.**
The URL stays the same, so you do not need to touch the site again.

## What lands where

| Tab | Comes from | Notes |
|---|---|---|
| `screening-quiz` | is-ibogaine-right-for-me.html | written when the visitor asks for their result by email |
| `provider-match` | find-a-provider.html | the full intake, plus `uploads` column linking to Drive |
| `consultation` | consultation.html | the contact form |
| `resource-gate` | resources.html | one row per gated download request |
| `_errors` | — | only appears if a submission fails; shows what and why |

Uploaded ECG and blood work files go to a Drive folder named in `CONFIG.UPLOAD_FOLDER`,
one subfolder per submission, with the links written into the row.

If you add or rename a question in the survey, the new field becomes a new column
automatically the next time someone submits. Existing rows keep their old columns.

## Notes

- The endpoint URL sits in the site's JavaScript, so treat it as public. The token
  only adds friction. The spreadsheet itself stays private — share it with nobody
  you would not show the data to.
- Free Google quotas are far above this site's volume. The limit worth knowing is
  email: 100 notification emails/day on a free account, counted per recipient — two
  addresses in `NOTIFY_EMAIL` means each submission uses two of that allowance.
- Nothing is queued client-side. If a visitor submits while the script is down they
  see "try again in a moment" and the row is not written.
