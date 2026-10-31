# CleanYourTV — speed up an old Android TV with one prompt

[CleanYourTV](https://github.com/Gathin23/cleanyourtv) by Gathin ([@gathint](https://x.com/gathint)) gives your AI coding assistant one prompt. Over Wi-Fi, the assistant switches off the ads, telemetry and preloaded apps on an Android TV and installs a small, Apple TV-style home screen. No root and no cable. Nothing is uninstalled, and one line undoes it all.

- Repo: https://github.com/Gathin23/cleanyourtv (MIT)
- Website: https://cleanyour.tv. This is the only official site. Other domains with the name, such as cleanyourtv.com, are not run by the project.

## Will it work on my TV?

| Your TV | Works? |
| --- | --- |
| Android TV / Google TV (TCL, Sony, Xiaomi, Philips, Hisense…) | ✅ yes: 260 tested models from 77 brands |
| Amazon Fire TV | ⚠️ cleanup only |
| Samsung (Tizen), LG (webOS) | ❌ different operating system |

Your model isn't on the [tested list](https://github.com/Gathin23/cleanyourtv/tree/main/examples)? The prompt finds the bloat on its own.

## What you need

1. A computer on the **same Wi-Fi** as the TV.
2. A coding assistant with shell access: **Claude Code**, **Codex** or **Gemini CLI**.
3. Your TV's model name.
4. About 15 minutes.

## Steps

**1. On the TV:** Settings → Device Preferences → About → press OK on **Build** seven times. Go back → Developer options → turn **USB debugging** on. If you also see **Network / ADB debugging**, turn that on too.

**2. On your computer:** clone the repo and paste [`PROMPT.md`](https://github.com/Gathin23/cleanyourtv/blob/main/PROMPT.md) into your assistant, with your TV model filled in.

```bash
git clone https://github.com/Gathin23/cleanyourtv
cd cleanyourtv
claude   # or codex / gemini
```

**3. Follow along:** tap "Allow USB debugging?" on the TV, then answer the assistant's questions: which apps you use, which apps go in the dock and in what order, and whether to keep the voice assistant, Chromecast and updates.

The assistant backs up your settings, disables the junk with `pm disable-user`, then builds the launcher, installs it and makes it your home screen. It checks each step with screenshots taken from the TV.

## ⚠️ The step you can't skip: switch debugging off

Network debugging (ADB) is **not encrypted**. On some firmware, any device on your Wi-Fi can get a shell on the TV. When you're done:

1. On the TV: Developer options → turn off **USB debugging** and **Network/ADB debugging**, and revoke the USB debugging authorisations.
2. Reboot the TV and check from your computer that the port is closed:

```bash
python3 tools/adb-closed.py <tv-ip>
```

The new home screen keeps working with debugging off.

## Changed your mind?

Everything is disabled, not deleted. To undo it:

```bash
tools/restore.sh <your-debloat-list.txt>
```

You can also re-enable any app in the TV's own Settings → Apps.

## No laptop?

There's a free, community-built [Android phone app](https://cleanyour.tv/app) by [@udhaykumarbala](https://github.com/udhaykumarbala) that does the same cleanup over Wi-Fi.

## The numbers in the video

- **29,000+ GitHub stars in a week:** the repo was created on Oct 17, 2026, and had 29,534 stars on Oct 24.
- **~500 KB launcher, built for TVs with 1 GB of RAM:** from the project's README (about 497 KB).
- **Home screen memory cut in half:** measured by [Navy Geeks](https://www.youtube.com/watch?v=dpOjBS1FAxg) on an Acer Google TV. The stock home screen used 286 MB after hours of use and 162 MB just after starting; the new launcher used 133 MB. Results vary by TV.

---

From the Explainbrew video about CleanYourTV. Facts checked against the project's README and the GitHub API on October 24, 2026. We're not affiliated with the project. Use it at your own risk: changing your TV's software may affect its warranty.

See the [disclaimer](../README.md#disclaimer-use-at-your-own-risk).
