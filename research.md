# The Problem

I went to Rahul (my college best friend) and told him about this assignment, then asked him
what problem he's actually facing right now. He said it's cold mails and follow-ups: he sends
10–20 cold mails a day to companies while job-hunting, but he loses track of which companies
he's already mailed, which ones he still needs to follow up with, and which ones have already
rejected him. Because of this he either follows up late or doesn't follow up at all, even with
companies that might have replied if he'd pushed once more.

## The problem in 5 lines
1. Rahul sends 10–20 cold mails a day while job-hunting, but keeps no organized record of them.
2. He loses track of which companies he's already mailed and which he hasn't followed up with.
3. In his words, the lack of follow-up means he probably misses replies from companies that would
   have responded to a second mail — he has no clarity on what's pending vs. rejected vs. cold.
4. Right now he does nothing systematic — no sheet, no reminder, just memory.
5. "Fixed" means: he can look at one place and immediately know which companies he needs to
   follow up with today, and which ones have already rejected him so he stops wasting time on them.

## Existing solutions and why they don't fit
1. **Gmail follow-up reminder extensions (e.g. Boomerang, Mailtrack)** — this is built for one-off important emails, not for tracking 10-20 cold mails a day across
   companies with rejection/reply status. Doesn't fit his volume.
2. **Manual Excel/Notion tracker** — this is the "obvious" fix, but doesn't fit because Rahul
   already doesn't maintain one — the friction of manually checking a sheet every day and
   updating it himself is exactly what he's not doing today. A tool that tells him what's due
   without him checking is a better fit.


## Person
Name: Rahul
Role: B.Tech student, job-hunting, sends 10-20 cold mails/day
Where: his home, ~1 km from mine — walking distance

## Update after fieldwork

The above was my hypothesis before going to Rahul's place — based on an earlier phone call
where he mentioned job cold-mails as his problem. When I actually sat with him at his home
to collect data, the real, current problem turned out to be different: he runs an Instagram
page and had sent outreach emails/DMs to multiple content creators he wants to hire for it.
He has the same underlying problem (sent → waiting → needs follow-up/rejected/selected, with
no organized tracking), but with creators instead of job applications.

I kept the tool's core idea (read a log, tell him who's overdue for a follow-up) but changed
the data to match what he actually needed: `creator_name, platform, contacted_on,
followup_sent, status` (status = pending / rejected / selected) instead of job-application
columns. See [fieldwork.md](fieldwork.md) for the full conversation and what changed the plan.
