# Daily Devotional Automation

A small Python tool from **SS Creative Studio** that turns each day's devotion into a ready-to-post **1080×1920 WhatsApp Status image**.

## Why I built it

I post a devotional status every morning around 6:30 AM. Designing each one by hand took too long, so this script does the layout for me. It rotates through **8 colour templates** so the feed doesn't look the same every day.

## Features

- 1080×1920 vertical output for WhatsApp Status, Instagram Stories and Facebook Stories
- 8 rotating gradient templates: Pink Floral, Blue & Gold, Sage Cream, Sunset Gradient, Burgundy Rose, Forest Charcoal, Coral Teal, Lavender Silver
- Automatic text wrapping and centring
- Picks the template from the day of the month
- Brand footer: *SS Creative Studio · AI • Art • Anointing*

## Quick start

```bash
pip install -r requirements.txt
python devotion_status.py \
  --title "Peace in the Storm" \
  --verse "Peace I leave with you; my peace I give you." \
  --ref "John 14:27" \
  --message "Whatever you face today, His peace goes with you. Rest in it." \
  --day 14 --out status.jpg
```

## Daily workflow (5 to 10 minutes)

1. Read the day's devotion and fill in `DAILY_EXTRACTION_FORM.txt`.
2. Run the script with the title, verse, reference and a short message.
3. Write the caption using the formula below.
4. Post to WhatsApp Status at about 6:30 AM.
5. Log views and reactions in `analytics.csv`.

### Caption formula (140 to 160 characters)

`[Hook line] + [verse ref] + [one-line application] + [soft CTA] + #DailyDevotion #SSCreativeStudio`

## Roadmap

- [ ] Malayalam font support
- [ ] Batch mode: render a whole month from a CSV
- [ ] Scheduled posting via Zapier

---
© SS Creative Studio · Saji Pandalam
