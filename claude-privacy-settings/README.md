# Claude privacy settings: the full checklist

**As of Nov 2026, consumer plans (Free, Pro, Max).** Team, Enterprise and API run on different (commercial) terms, so this list doesn't apply to them. Every line comes from Anthropic's own pages, linked below. Anthropic renames menus now and then, so if a label doesn't match, look for the nearest one.

Anthropic may use consumer chats to train its models unless you opt out in your account settings ([Privacy Policy](https://www.anthropic.com/legal/privacy)).

## ☐ 1. Model training

- **Settings → Privacy** (web, desktop, mobile). The toggle is called "Help Improve our AI models" in the [Privacy Center](https://privacy.claude.com/en/articles/12109829).
- **On:** your data may be kept for **up to 5 years** (de-identified, in training pipelines). **Off:** the **30-day** retention period applies ([How long do you store my data?](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)).
- Turning it off stops future training on new and previously stored chats. It **can't undo** data already in a training run that has started, or models that are already trained.

## ☐ 2. Incognito chats for anything sensitive

- Click the **ghost icon** in the upper right of a new chat (not available inside projects).
- Incognito chats aren't saved to your history or memory, and **aren't used for training**, even if model training is on.
- They're still **kept for 30 days** ([Using incognito chats](https://support.claude.com/en/articles/12260368-using-incognito-chats)).

## ☐ 3. Memory (on by default)

- Memory ("Generate memory from chats") is on by default for Free, Pro, Max and Ultra.
- **Settings → Your Claude** (older layout: Settings → Memory):
  - **Pause** keeps your memories but stops using or creating them.
  - **Manage** lets you edit or delete single topics.
  - **Reset** permanently deletes all memories.
- On paid plans, also check "Search and reference chats" (past-chat search) ([Chat search and memory](https://support.claude.com/en/articles/11817273)).

## ☐ 4. Export, then delete old chats

- **Export first:** Settings → Privacy → **Export data** (web and desktop only). The link is emailed to you and expires in 24 h ([Export your data](https://support.claude.com/en/articles/9450526)).
- **Delete:** open the chat's **⋮** menu → **Delete** (on iOS, long-press). It disappears from your history right away and is deleted from Anthropic's back-end **within 30 days**. Deleted chats aren't used for future training ([Delete a conversation](https://support.claude.com/en/articles/8230524-delete-or-rename-a-conversation)).

## ☐ 5. Know the exceptions

- **Thumbs up / down:** rating a response stores **the whole conversation** as feedback, kept for **5 years**.
- **Safety flags:** even with training off, conversations flagged for safety review (or explicitly reported) may still be used. Flagged inputs and outputs are kept up to 2 years, classifier scores up to 7 years.

## ☐ 6. Claude Code

Source: [Claude Code → Data usage](https://code.claude.com/docs/en/data-usage).

- The model-training setting from step 1 also covers Claude Code used with a Free, Pro or Max account.
- Opt out of telemetry with environment variables, either in your shell or in `~/.claude/settings.json` under `"env"`:

```json
{
  "env": {
    "DISABLE_TELEMETRY": "1",
    "DISABLE_ERROR_REPORTING": "1",
    "DISABLE_FEEDBACK_COMMAND": "1"
  }
}
```

- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` turns off all non-essential traffic in one line. The metrics never include your code, prompts or file paths.
- `/feedback` (and `/bug`, `/share`) sends a transcript that is kept **5 years**. `DISABLE_FEEDBACK_COMMAND=1` turns that command off.
- Local transcripts are stored in `~/.claude/projects/` for **30 days** by default (setting: `cleanupPeriodDays`).

---

From the [Explainbrew](https://github.com/explainbrew/prompts) short "Claude privacy settings", Nov 2026. Checked against Anthropic's Privacy Policy, Privacy Center, Help Center and Claude Code docs on Nov 10, 2026. Policies change, so re-check the linked pages. Not affiliated with Anthropic.

See the [disclaimer](../README.md#disclaimer-use-at-your-own-risk).
