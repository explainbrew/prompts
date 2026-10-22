# PHP2Shell — server checklist

Two critical PHP vulnerabilities, **CVE-2026-109618** and **CVE-2026-109619** (CVSS v4.0 9.2), can allow unauthenticated remote code execution. PHP released fixes on October 21, 2026.

Official advisory: https://www.php.net/ (news from October 20–21, 2026)

## 1. Check your version

```bash
php -v
```

Also check the PHP your web server actually uses (it can differ from the CLI): create a temporary `phpinfo()` page, check the version, then delete the page. Or ask your hosting provider.

## 2. Are you safe?

| Your version | Status |
| --- | --- |
| 8.5.12 or newer | ✅ fixed |
| 8.4.27 or newer 8.4.x | ✅ fixed |
| 8.3.36 or newer 8.3.x | ✅ fixed |
| 8.2.35 or newer 8.2.x | ✅ fixed (8.2 reaches end of life on Dec 31, 2026) |
| anything older in 8.2–8.5 | ❌ update now |
| 8.1, 8.0, 7.x, 5.x | ❌ no official release from the PHP project — see step 4 |

## 3. Update

- Your own server: update PHP from your OS packages or the official source, then **restart PHP-FPM / Apache / your web server** so the new version is actually loaded.
- Linux distros may ship backported fixes under different version numbers — check your distro's security tracker.
- Shared hosting: ask your host to confirm they are patched against CVE-2026-109618 and CVE-2026-109619.
- Don't forget PHP bundled inside other software: control panels, Docker images, vendor appliances.

## 4. Stuck on PHP 8.1 or older?

- PHP says: "There are no complete mitigations, updating is the only safe choice."
- Until you upgrade: take internet-facing sites off the public network or put them behind a VPN / WAF, as advisories from CERT-EU and others recommend.
- Partial mitigations listed in the advisory (they reduce risk, they do **not** make you safe): `memory_limit=-1`, `session.upload_progress.enabled=0`.

## 5. Watch for signs of compromise

- PHP worker processes starting shells, interpreters or download tools.
- New or changed files in the web root, unknown cron jobs, new user accounts.
- If you suspect a breach: isolate the server and keep the web and PHP logs.

---

From the Explainbrew video about PHP2Shell. Facts checked against php.net and W3Techs on October 22, 2026.
