# Bariatric Counseling Center -- Cron Jobs

Scheduled data output for bariatriccounselingcenter.com (BCC), served via drbdig.com/seo/bcc/.

## Jobs in this project

| Job | Folder | Schedule | Description |
|-----|--------|----------|-------------|
| SEO Weekly Runner | seo-weekly/ | Every Monday 8:00 AM CST | Google SERP position checks + GSC data for all tracked keywords |

## Data access

Raw JSON files are fetchable directly from GitHub:

https://raw.githubusercontent.com/austintude/cron-jobs/main/bariatric-counseling-center/seo-weekly/data/seo-data-YYYY-MM-DD.json

Latest manifest (always points to most recent file):

https://raw.githubusercontent.com/austintude/cron-jobs/main/bariatric-counseling-center/seo-weekly/manifest.json

## drbdig.com cron setup

The cron job on drbdig.com fetches the latest data file using the manifest URL above and saves it to the dashboard data folder.

See seo-weekly/README.md for full cron setup instructions.
