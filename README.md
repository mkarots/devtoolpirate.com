# devtoolpirate.com

Landing page for [Devtool Pirate](https://devtoolpirate.com), a weekly letter on tools, agentic papers, and engineering trends.

Editorial source of truth: the private `devtoolpirate` repo. This repo is only the public site.

## Subscribe

The form is a stub until an email vendor is chosen (Buttondown/Kit recommended; Astro stays canonical later). Set `form[action]` in `index.html` to the vendor embed URL when the list is live.

Until then, the button tells people to DM [@cepstrum9](https://x.com/cepstrum9).

## Local preview

```bash
python3 -m http.server 8080
```

## Tests

```bash
python3 -m unittest tests.test_site
```

## DNS

Same GitHub Pages apex as the other domains. Delete GoDaddy Website Builder on `@`, then:

| Type | Name | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

Leave `www` ? `devtoolpirate.com` if it already exists.
