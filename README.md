# Creator Outreach Follow-Up Tracker

Rahul runs an Instagram page and wanted to hire a content creator for it, so he sent
outreach emails/DMs to multiple creators. He had no single place to see who still needs
a follow-up, who's rejected, and who's already selected — it was all in his head and his
inbox. This script reads his real outreach log and tells him, right now, who's overdue
for a follow-up.

See [research.md](research.md) and [fieldwork.md](fieldwork.md) for the problem writeup
and fieldwork evidence — including how the plan changed once I actually talked to him.

## How to run

```bash
python3 followup.py
```

Optional: change how many days before a follow-up is "due" (default 4):

```bash
python3 followup.py --threshold 5
```

## Data

`data.csv` columns: `creator_name, platform, contacted_on, followup_sent, status`
(`status` is one of `pending`, `rejected`, `selected`)

Collected by sitting with Rahul at his home and going through the creators he's contacted
— see [fieldwork.md](fieldwork.md) for exactly how and where.

## Real output

```
Follow-up due today:
  Xploringmy...   (Instagram), contacted 5 days ago, still pending
  moksha.punm.    (Instagram), contacted 5 days ago, still pending
  Simranmaury.    (Instagram), contacted 5 days ago, still pending
  himanshi        (Instagram), contacted 5 days ago, still pending
  ayusingh9876    (Instagram), contacted 5 days ago, still pending
  Juhi            (Instagram), contacted 5 days ago, still pending
  Aishita         (Instagram), contacted 5 days ago, still pending
  bysaumyagup.    (Instagram), contacted 5 days ago, still pending
  kareenaf...     (Instagram), contacted 5 days ago, still pending
  hello           (Instagram), contacted 5 days ago, still pending
  dhaaraa.off.    (Instagram), contacted 5 days ago, still pending
  kinjalkhadk.    (Instagram), contacted 5 days ago, still pending
  hello.archi     (Instagram), contacted 5 days ago, still pending
  avanian...      (Instagram), contacted 5 days ago, still pending
  kavyajain0.     (Instagram), contacted 5 days ago, still pending
  Soumya          (Instagram), contacted 5 days ago, still pending

16 follow-ups due, 0 selected, 0 rejected, 24 already followed up (awaiting reply), 40 total valid rows.
```

Note: all 40 rows are dated the same day (16 Nov 2026) and all have status "Contacted" —
that's genuine, not rounded/fabricated. Rahul sent out his outreach in one batch on that day
and nobody has replied yet, so there are no "rejected"/"selected" rows yet. The 16 flagged
above are the ones where he hasn't sent a follow-up and it's been 5+ days.

## What it gets wrong

- A fixed day-threshold doesn't fit every creator — some reply fast, some take weeks. The
  tool treats everyone the same.
- It only knows what's in `data.csv`. If a creator replied on Instagram DM or WhatsApp
  instead of email and Rahul forgot to log it, the tool will wrongly flag them as pending.
- Once `followup_sent` is "yes" the tool stops tracking that row — it doesn't know if a
  second follow-up is needed.
- Dates must be in `YYYY-MM-DD` format exactly, or the row is skipped (and reported).

## Screen recording

[link to 3-minute screen recording here]

## AI chats

Exported to [ai-chats/](ai-chats/).
