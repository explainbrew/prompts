# Twenty CRM — the prompt from the video

Works with Claude Code (or any coding agent) inside a Twenty app ("apps as code").

1. Repo: https://github.com/twentyhq/twenty
2. Create an app: `npx twenty@latest app init`
3. Add the official agent skills:
   `npx skills add https://github.com/twentyhq/twenty/tree/agent-skills --skill create-app`
   `npx skills add https://github.com/twentyhq/twenty/tree/agent-skills --skill develop-app`
4. Run `twenty dev` to sync your code with the CRM, then give your agent this prompt:

```text
You are working in a Twenty app (apps as code). Use the create-app and develop-app skills.

Build a CRM for a freelance designer.

Objects:
- Client: name, company, email, phone, source (referral / Instagram / Behance / other).
- Project: title, client (relation), budget, deadline, stage (brief / design / revisions / delivered / paid).
- Invoice: number, project (relation), amount, issue date, status (issued / paid / overdue).

Create a kanban view for projects by stage.
After each step, check that the sync with the server succeeded without errors.
At the end, briefly list what was created.
```

Then, live edit:

```text
Add a Telegram field to Client.
```

Make it yours: replace "for a freelance designer" with "for a barbershop", "for a tutor", "for a real estate agency".
