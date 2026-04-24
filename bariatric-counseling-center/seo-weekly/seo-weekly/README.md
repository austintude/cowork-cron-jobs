# SEO Weekly Runner -- BCC

Automated weekly SEO data collection for bariatriccounselingcenter.com.

**Schedule:** Every Monday at 8:00 AM CST
**Runner file:** C:\Users\danie\Documents\Claude\Projects\Bariatric Counseling Center\seo-tools\seo-weekly-runner.md

## What it does

1. Pulls keyword data from Google Search Console (if available)
2. Checks live Google SERP positions for all priority 1 and 2 keywords
3. Runs link integrity checks on the top 10 ranking pages
4. Writes a JSON data file to this repo folder
5. Updates manifest.json with the latest file reference

## Output files

Data files are written to: `data/seo-data-YYYY-MM-DD.json`

Manifest: `manifest.json` (always points to the latest data file)

## drbdig.com cron setup

A cron job on drbdig.com (SiteGround) fetches the latest data and saves it to the dashboard.

### Step 1 -- Create the fetch script

SSH into drbdig.com (u151-w6lqsfyvozwa, port 18765) and create:

`/home/u151-w6lqsfyvozwa/fetch-seo-data.sh`

```bash
#!/bin/bash
# Fetch latest BCC SEO data from GitHub and save to dashboard
MANIFEST_URL="https://raw.githubusercontent.com/austintude/cron-jobs/main/bariatric-counseling-center/seo-weekly/manifest.json"
DATA_DIR="/home/u151-w6lqsfyvozwa/public_html/seo/bcc/data"

# Get the latest filename from manifest
LATEST=$(curl -s "$MANIFEST_URL" | python3 -c "import sys,json; print(json.load(sys.stdin)['latest'])")

# Fetch the data file
curl -s "https://raw.githubusercontent.com/austintude/cron-jobs/main/bariatric-counseling-center/seo-weekly/data/$LATEST" -o "$DATA_DIR/$LATEST"

# Also save as latest.json for easy dashboard access
cp "$DATA_DIR/$LATEST" "$DATA_DIR/latest.json"

echo "$(date): Fetched $LATEST" >> /home/u151-w6lqsfyvozwa/seo-fetch.log
```

### Step 2 -- Schedule it

In SiteGround Cron Jobs (Site Tools > Devs > Cron Jobs), add:

- **Minute:** 0
- **Hour:** 15  (10 AM CST = 15:00 UTC)
- **Command:** `bash /home/u151-w6lqsfyvozwa/fetch-seo-data.sh`

Run every Monday (Day of week = 1).

## manifest.json format

```json
{
  "latest": "seo-data-2026-04-23.json",
  "updated": "2026-04-23T08:00:00-06:00",
  "files": [
    "seo-data-2026-04-23.json"
  ]
}
```
