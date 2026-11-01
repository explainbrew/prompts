# Insomnia — keep your MacBook awake with the lid closed (for coding agents)

[Insomnia](https://github.com/krishhgg/Insomnia) by krishhgg is a macOS menu bar app for timed awake sessions. Set how long your Mac stays awake, close the lid, and your coding agent (Claude Code, Codex, Gemini CLI) keeps working until the timer ends.

- Repo: https://github.com/krishhgg/Insomnia (MIT)
- Website: https://getinsomnia.app

## Will it work on my Mac?

- **macOS 26 or later on an Apple Silicon Mac.** Older macOS or Intel Macs: no.
- Status: **experimental**. The author: "Recovery can fail, and a running timer is not a safety guarantee."

## Before you install: the sudo rule

The installer asks for your password and adds `/etc/sudoers.d/insomnia`. It lets your user account run these four commands without a password:

```text
/usr/bin/pmset -a disablesleep 1
/usr/bin/pmset -a disablesleep 0
/usr/bin/pmset -b lowpowermode 1
/usr/bin/pmset -b lowpowermode 0
```

Any program running as you can use that rule too. Read it, then decide. It also installs a recovery agent (a `launchd` job that runs every minute) that undoes a session if the app is gone.

## Install

Paste this into your coding agent (from the official README):

```text
Install the latest stable Insomnia release by following https://github.com/krishhgg/Insomnia/blob/main/skills/install-insomnia/SKILL.md. If a step needs my password, give me the command to run in Terminal.
```

Manual install and checksums: [docs/install.md](https://github.com/krishhgg/Insomnia/blob/main/docs/install.md).

## Using it

1. Click the eye in the menu bar, enter days / hours / minutes, press Enter.
2. Close the lid if you want: the display goes dark, audio mutes, Slack, WhatsApp and Discord freeze, Low Power Mode turns on. Opening the lid undoes it; the timer keeps running.
3. On battery: Low Power Mode below 40%, session ends below 10% (defaults, change in Settings).
4. End early: press and hold the end control next to the countdown.

**Use a stable, well-ventilated surface. Never in a closed bag.** Run a short session you can watch first, then read `~/Library/Logs/Insomnia/insomnia.log`.

## Undo

```bash
./scripts/uninstall.sh          # app, agent and sudoers rule
./scripts/uninstall.sh --purge  # also settings and logs
```

---
From the [Explainbrew](https://github.com/explainbrew/prompts) short. Facts from the Insomnia README, Nov 1, 2026. Not affiliated with the project.
