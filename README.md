# apps.pascoeharvey.com

The public pages for Pascoe Harvey's apps, served by GitHub Pages at
https://apps.pascoeharvey.com.

- `roomread/`: Room Read, the dance caller for Android. This is the "Website" on its Google Play listing.
- `roomread/privacy/`: its privacy policy. **This address is the one given to Google Play, so don't move it.**
- `roomread/test/`: "Test Room Read", the guide for joining the closed test on Google Play. Send testers this address.

## The privacy policy

`privacy.md` is an exact copy of the app's `app/src/main/assets/privacy.md`
(private repository PascoeJHarvey/the-caller), and the two must always match.
Change the app's copy first, then:

    git -C /home/pascoe/dev/the-caller show origin/main:app/src/main/assets/privacy.md > privacy.md
    python3 build.py
    git add -A && git commit -m "Privacy policy: the app's copy as of <date>" && git push

`build.py` turns `privacy.md` into `roomread/privacy/index.html`.

## The tester guide

`roomread/test/index.html` is written by hand (there is no build step for it)
and uses the shared `style.css`, whose last block styles its numbered steps and
button links. Testers read it on their phones, so keep each step to about a
screen. It links to the testers' Google Group, the Play test invitation and the
Play listing. A comment marked `VIDEO PLACEHOLDER` shows where the YouTube
video goes, as a privacy-enhanced embed from `youtube-nocookie.com`, once it
exists.

## Hosting

- **Pages:** branch `main`, folder `/`, custom domain in `CNAME`, "Enforce HTTPS" on. GitHub renews the certificate itself.
- **DNS:** pascoeharvey.com is registered at Squarespace Domains (renews 30 March 2027) and has one record for this site: CNAME `apps` → `pascoejharvey.github.io`. The domain's other records are for Zoho mail; leave them alone.
- The full notes, including what to do if the site or its certificate breaks, are in the app repository: `docs/play/WEBSITE_and_privacy_policy_02Oct2026_v1.md`.

Contact: roomreadthecaller@gmail.com
