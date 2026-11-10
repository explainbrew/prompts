# Free My TV — a clean home screen on Samsung and LG (and Google TV)

[Free My TV](https://github.com/simbasjungles/free-my-tv) describes itself as "a fast, ad-free home screen for Google TV, LG webOS and Samsung Tizen. One button to undo." Free and open source (MIT). It's the follow-up to our [CleanYourTV](../cleanyourtv/) video, which only works on Android / Google TV.

- Repo: https://github.com/simbasjungles/free-my-tv (MIT, "Built with Claude Code")
- Latest release when we checked: v1.4.0 (Nov 10, 2026)

**We don't have an LG or Samsung TV, so we haven't run this ourselves.** The steps below summarize the project's README. Read the [README](https://github.com/simbasjungles/free-my-tv#readme) before you start, because install steps change between releases.

## The honest part: what it does on each TV

| Your TV | What you get |
| --- | --- |
| Google TV / Android TV (Android 8+) | It **becomes** the home screen. Free My TV → Home Screen → Original brings the factory one back. If it crashes three times in five minutes, it switches back on its own. No root, nothing uninstalled |
| LG (webOS 3 or newer) | An LG **app** installed through LG's own Developer Mode. **LG's home screen stays where it is.** Nothing rooted or changed on the TV |
| Samsung (Tizen, 2015 or newer, with exceptions) | A Samsung **app** installed through Samsung's Developer Mode with the community TizenBrew Installer. **Samsung's home screen stays where it is.** Nothing rooted |
| Samsung Orsay models | ❌ can't run it |
| Any other TV | The README suggests plugging a Google TV streamer into HDMI |

On LG and Samsung it does **not** remove ads from the TV's own home screen. It gives you a second home screen, inside an app, without sponsored rows, banners or autoplaying promos: your streaming apps on a shelf, plus trending picks from apps you already have.

## LG (webOS)

You need a computer on the **same Wi-Fi** as the TV with **Python 3**. Another option is the webOS Homebrew Channel.

1. Turn on LG Developer Mode on the TV (LG's Developer Mode app).
2. Clone the repo and run the README's build and install steps, using your TV's IP address:

```bash
git clone https://github.com/simbasjungles/free-my-tv
cd free-my-tv
python3 webos/build.py
python3 webos/install.py <TV-IP>
```

3. **Shortcut:** while Free My TV is open, hold a number key on the remote. From then on, that key opens it from anywhere. If your remote has no number keys, open it from LG's app list.

### ⚠️ LG's 40-day deadline

LG Developer Mode lasts **about 40 days**. Before it runs out, press **EXTEND** in the Developer Mode app, or let your computer renew it (the README suggests running this weekly on a schedule):

```bash
python3 webos/renew.py <TV-IP>
```

### Remove it from LG

```bash
python3 webos/install.py <TV-IP> --uninstall
```

## Samsung (Tizen)

- **2017 and newer:** turn on Samsung's Developer Mode, open the **TizenBrew Installer**, choose **Install from GitHub**, and enter `simbasjungles/free-my-tv`. TVs from 2023 and newer ask you to sign in to a Samsung account once.
- **2015–2016:** build it yourself (see the README). Some 2016 models refuse developer installs with `failed[118]`.
- **Orsay models:** not supported.

To remove it, uninstall it like any other app. The "one button to undo" in the description is the Google TV path. On Samsung and LG you just delete the app.

## Google TV / Android TV

Follow the README's Install section. To go back, open Free My TV → Home Screen → **Original**.

## What we didn't check

- Install time on LG or Samsung. The README's "about ten minutes" refers to Google TV.
- Speed. The README's speed and memory numbers were measured on one TCL Google TV, so they don't tell you anything about LG or Samsung.

---

From the [Explainbrew](https://github.com/explainbrew/prompts) short on Free My TV, Nov 2026. Facts checked against the project's README, releases and the GitHub API on Nov 10, 2026. Not affiliated with the project. Developer Mode and sideloaded apps are your call, and may affect your TV's warranty.

See the [disclaimer](../README.md#disclaimer-use-at-your-own-risk).
