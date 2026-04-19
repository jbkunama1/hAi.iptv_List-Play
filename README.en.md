# 🇩🇪🇦🇹🇨🇭 hAI.iptv_List&Play

A curated GitHub repository for **legal, publicly available IPTV sources** from **Germany, Austria and Switzerland**.

> 🧠 Project: **hAI.iptv_List&Play** – Repository: `https://github.com/jbkunama1/hAi.iptv_List-Play`
>
> ⚠️ Focus is explicitly on freely accessible, well-known projects such as `iptv-org`, `Free-TV/IPTV`, `kodinerds-iptv` and `iptv-ch`. No pay-TV or obviously illegal offers.

---

## 📁 Structure

- `dach-legal.m3u` – simple DACH master playlist (version 1)
- `de.m3u`, `at.m3u`, `ch.m3u` – separate country playlists (version 2)
- `dach.m3u` – aggregated DACH playlist (version 2)
- `favorites.m3u` – slim favourites list (public broadcasters focus, exemplary)
- `epg-links.md` / `epg-links.en.md` – EPG links & notes (DE/EN)
- `README.md` / `README.en.md` – documentation (DE/EN)
- `agent-flow.md` / `agent-flow.en.md` – agent flow for daily maintenance (DE/EN)
- `scripts/update_playlist.py` – generates/updates the core playlists
- `scripts/health_check.py` – simple health check of source playlists
- `.github/workflows/update.yml` – GitHub Actions workflow for daily updates
- `index.html` – landing page for GitHub Pages

---

## 🔗 Used projects / sources

- [iptv-org/iptv](https://github.com/iptv-org/iptv) – collection of publicly available IPTV channels worldwide
- [Free-TV/IPTV](https://github.com/Free-TV/IPTV) – M3U playlist for free TV channels around the world
- [jnk22/kodinerds-iptv](https://github.com/jnk22/kodinerds-iptv) – free and legal streams for Kodi
- [iptv-ch](https://iptv-ch.github.io) – playlists for Swiss providers and open CH channels
- `xmltv.ch` – XMLTV/EPG source for several Swiss channels

These repositories are only **referenced**, the actual content is hosted there.

---

## 🧾 Playlists

### Version 1 – compact DACH playlist

- `dach-legal.m3u`
  - points directly to the `iptv-org` country playlists (DE/AT/CH)
  - adds `tvopenchde.m3u` from `iptv-ch` for open German-speaking CH channels

### Version 2 – more fine-grained

- `de.m3u` – Germany
  - `iptv-org` country playlist
  - global Free-TV playlist from `Free-TV/IPTV`
  - `kodinerds-iptv` base list `clean.m3u`
- `at.m3u` – Austria
  - `iptv-org` country playlist
- `ch.m3u` – Switzerland
  - `iptv-org` country playlist
  - `tvopenchde.m3u` from `iptv-ch`
- `dach.m3u` – aggregates `de.m3u`, `at.m3u`, `ch.m3u`
- `favorites.m3u` – minimal favourite list focused on public broadcasters

---

## 📺 Usage

### In your player

- Load `dach-legal.m3u` or `dach.m3u` directly into players such as **VLC**, **IPTVnator**, **TiviMate** or Kodi (via suitable add-ons).

### As GitHub raw URL

After pushing to your repository you can use for example:

```text
https://raw.githubusercontent.com/jbkunama1/hAi.iptv_List-Play/main/dach.m3u
```

or

```text
https://raw.githubusercontent.com/jbkunama1/hAi.iptv_List-Play/main/de.m3u
https://raw.githubusercontent.com/jbkunama1/hAi.iptv_List-Play/main/at.m3u
https://raw.githubusercontent.com/jbkunama1/hAi.iptv_List-Play/main/ch.m3u
```

---

## 🧠 EPG

Clearly documented and stable (from the sources used):

- `https://xmltv.ch/xmltv/xmltv-tvsd.xml.gz` – for many Swiss channels (e.g. referenced in `iptv-ch` context)

For Germany and Austria there is **no** clearly documented, complete universal EPG in the used projects, therefore:

- central EPG URL only for CH in `dach-legal.m3u`
- additional per-channel/group EPG mapping is recommended in your player

Details are explained in `epg-links.md` / `epg-links.en.md`.

---

## 🤖 Automation (Agent & GitHub Actions)

- `scripts/update_playlist.py`
  - regenerates `dach-legal.m3u` and `epg-links`
- `scripts/health_check.py`
  - fetches the most important source lists and writes `health-report.md`
- `.github/workflows/update.yml`
  - runs daily via cron
  - executes `update_playlist.py` and `health_check.py`
  - commits changes automatically

**Agent flow** (see `agent-flow.md` / `agent-flow.en.md`):

- checks source URLs
- marks permanently failing sources
- optionally extends favourites

---

## 🌐 GitHub Pages

`index.html` serves as a landing page and can be published via GitHub Pages (branch `main`, path `/`).

Recommended configuration for this project:

- Repository: `jbkunama1/hAi.iptv_List-Play`
- Pages: source = `main` / root

---

## ⚖️ License

This project is intended to be licensed under the **MIT License**. You can add an MIT license file via the GitHub UI under "Add license".

---

## ⚖️ Legal notice

This repository:

- is intended to reference **freely accessible, legally retrievable sources** only
- does not claim completeness
- does not provide legal advice for all jurisdictions

Please observe:

- local laws and the terms of use of each provider
- usage rights may change at any time
