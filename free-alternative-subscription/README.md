# Free Cursor alternatives: Zed, Cline, OpenCode (and the catch)

Three open-source tools that cover the editor and agent part of Cursor for $0, **with your own model**. They don't do everything Cursor does: Cursor has its own models, cloud agents and Bugbot reviews.

**Prices and star counts as of Nov 10, 2026.** They change, so check the linked pages before you decide.

## Why now

- Cursor's pricing page marks **Premium, $30/month**, as "Most popular". New customers can pick Free ($0, limited), Plus ($8, Grok models only), Premium ($30), Super ($100) or Ultra ($200). The old Pro at $20 is legacy and closed to new customers ([cursor.com/pricing](https://cursor.com/pricing), [Cursor help](https://cursor.com/help/account-and-billing/pricing)).
- Third-party models such as Claude or GPT are **not included** in those prices. You pay API list price from prepaid credit on top (Premium and above).
- Since Oct 12, 2026, Cursor has been sold inside The X Subscription ([xAI](https://x.ai/news/x-subscription)).

## The three

| Tool | What it is | License | Stars | Price |
| --- | --- | --- | --- | --- |
| [Zed](https://zed.dev) | A full code editor with a built-in AI agent (Zed Agent) | GPL-3.0-or-later (some parts Apache-2.0) | 94.7K | Personal plan $0. Pro $10/month is optional ([pricing](https://zed.dev/pricing)) |
| [Cline](https://github.com/cline/cline) | A coding agent inside VS Code (also JetBrains and CLI). It creates and edits files and runs commands, and asks before each edit and command unless you turn on auto-approve. Plan / Act modes | Apache-2.0 | 71.5K | Extension free for individual developers ([pricing](https://cline.bot/pricing)) |
| [OpenCode](https://opencode.ai) | A coding agent in your terminal (also desktop). 200+ providers, including local models | MIT | 225.9K | Free. It comes with a set of free models, no account needed. OpenCode Go from $10/month is optional |

## The catch: the tool is free, the model isn't

Choose one:

1. **Your own API key**: pay per use to the model provider. Zed, Cline and OpenCode all accept your own key.
2. **A local model**: free, but you need a strong machine, and local models are generally weaker than the top hosted ones. [Ollama](https://github.com/ollama/ollama) (MIT) runs models on your computer. Cline's docs say small or quantized models need **16–32 GB RAM** and larger ones **64 GB+** ([Cline docs](https://docs.cline.bot/provider-config/ollama)).

## Setup: local model with Ollama

1. Install [Ollama](https://ollama.com) and download a coding model that fits your RAM.
2. Connect a tool:
   - **Zed:** [Use a local model](https://zed.dev/docs/ai/use-a-local-model). Pick Ollama (or LM Studio) as the provider for Zed Agent.
   - **Cline:** install the extension in VS Code, then follow [Cline → Ollama](https://docs.cline.bot/provider-config/ollama).
   - **OpenCode:** [Providers](https://opencode.ai/docs/providers/). OpenCode finds Ollama at `127.0.0.1:11434` on its own, no account needed.
3. Try it on a throwaway repo first. Read every command the agent wants to run before you approve it.

## Setup: your own API key

Paste the key into the tool's provider settings (each tool's docs above). Set a spending limit at your provider before you start, because agents can use a lot of tokens.

## Why not Roo Code or Void?

Both repos are archived (2026). Continue and Aider haven't had a release or push since mid-2026. Kilo Code overlaps with Cline.

---

From the [Explainbrew](https://github.com/explainbrew/prompts) short on free Cursor alternatives, Nov 2026. Facts checked against the official pricing pages, docs and the GitHub API on Nov 10, 2026. Not affiliated with Cursor, xAI, Zed, Cline, OpenCode or Ollama.

See the [disclaimer](../README.md#disclaimer-use-at-your-own-risk).
