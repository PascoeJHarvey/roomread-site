# apps.pascoeharvey.com

The public pages for Pascoe Harvey's apps, served by GitHub Pages at
https://apps.pascoeharvey.com.

- `roomread/`: Room Read, the dance caller for Android.
- `roomread/privacy/`: its privacy policy, the address given to Google Play.

`privacy.md` is a copy of the app's `app/src/main/assets/privacy.md`
(repository PascoeJHarvey/the-caller) with the contact email filled in. After
changing it, run `python3 build.py` to regenerate
`roomread/privacy/index.html`, and commit both. The page in the app and the
page here should always say the same thing.
