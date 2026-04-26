[![Buy me a coffee](https://cdn.buymeacoffee.com/buttons/default-orange.png)](https://www.buymeacoffee.com/highfish)

# 🇩🇪🇦🇹🇨🇭 hAI.iptv_List&Play

Ein kuratiertes GitHub-Repository für **legale, öffentlich verfügbare IPTV-Quellen** aus **Deutschland, Österreich und der Schweiz**.

> 🧠 Projekt: **hAI.iptv_List&Play** – Repository: `https://github.com/jbkunama1/hAi.iptv_List-Play`
>
> ⚠️ Fokus liegt explizit auf frei zugänglichen, bekannten Projekten wie `iptv-org`, `Free-TV/IPTV`, `kodinerds-iptv` und `iptv-ch`. Keine Pay-TV- oder offensichtlich illegalen Angebote.

---

## 📁 Struktur

- `dach-legal.m3u` – einfache DACH-Gesamtplaylist (Version 1)
- `de.m3u`, `at.m3u`, `ch.m3u` – getrennte Länderlisten (Version 2)
- `dach.m3u` – Aggregation von DE/AT/CH (Version 2)
- `favorites.m3u` – schlanke Favoritenliste (öffentlich‑rechtlicher Fokus, exemplarisch)
- `epg-links.md` / `epg-links.en.md` – EPG-Links & Hinweise (DE/EN)
- `README.md` / `README.en.md` – Dokumentation (DE/EN)
- `agent-flow.md` / `agent-flow.en.md` – Agent-Flow für tägliche Pflege (DE/EN)
- `scripts/update_playlist.py` – erzeugt/aktualisiert die Kern-Playlists
- `scripts/health_check.py` – einfacher Health-Check der Quell-Playlists
- `.github/workflows/update.yml` – GitHub Actions Workflow für tägliche Updates
- `index.html` – Landingpage für GitHub Pages

---

## 🔗 Genutzte Projekte / Quellen

- [iptv-org/iptv](https://github.com/iptv-org/iptv) – Sammlung öffentlich verfügbarer IPTV-Kanäle weltweit
- [Free-TV/IPTV](https://github.com/Free-TV/IPTV) – M3U-Playlist für weltweite Free-TV-Channels
- [jnk22/kodinerds-iptv](https://github.com/jnk22/kodinerds-iptv) – freie und legale Streams für Kodi
- [iptv-ch](https://iptv-ch.github.io) – Playlists für Schweizer Provider und offene CH-Sender
- `xmltv.ch` – XMLTV/EPG-Quelle u. a. für Schweizer Sender

Diese Repos werden nur **referenziert**, der tatsächliche Inhalt liegt dort.

---

## 🧾 Playlists

### Version 1 – kompakte DACH-Playlist

- `dach-legal.m3u`
  - verweist direkt auf die Länder-Playlists von `iptv-org` (DE/AT/CH)
  - ergänzt um `tvopenchde.m3u` aus `iptv-ch` für offene deutschsprachige CH-Sender

### Version 2 – feinere Struktur

- `de.m3u` – Deutschland
  - `iptv-org` Länderplaylist
  - globale Free-TV-Playlist von `Free-TV/IPTV`
  - `kodinerds-iptv` Basisliste `clean.m3u`
- `at.m3u` – Österreich
  - `iptv-org` Länderplaylist
- `ch.m3u` – Schweiz
  - `iptv-org` Länderplaylist
  - `tvopenchde.m3u` von `iptv-ch`
- `dach.m3u` – verweist auf `de.m3u`, `at.m3u`, `ch.m3u`
- `favorites.m3u` – minimalistische Favoritenliste mit Fokus auf öffentlich-rechtliche Angebote

---

## 📺 Verwendung

### Im Player

- `dach-legal.m3u` oder `dach.m3u` direkt in Player wie **VLC**, **IPTVnator**, **TiviMate** oder Kodi (über passende Add-ons) laden.

### Als GitHub-Raw-URL

Nach dem Push in dein Repo kannst du z. B. folgende URLs nutzen:

```text
https://raw.githubusercontent.com/jbkunama1/hAi.iptv_List-Play/main/dach.m3u
```

bzw.

```text
https://raw.githubusercontent.com/jbkunama1/hAi.iptv_List-Play/main/de.m3u
https://raw.githubusercontent.com/jbkunama1/hAi.iptv_List-Play/main/at.m3u
https://raw.githubusercontent.com/jbkunama1/hAi.iptv_List-Play/main/ch.m3u
```

---

## 🧠 EPG

Stabil belegbar ist insbesondere:

- `https://xmltv.ch/xmltv/xmltv-tvsd.xml.gz` – für viele Schweizer Sender (z. B. im Kontext von `iptv-ch` dokumentiert)

Für Deutschland und Österreich gibt es **kein** in den genutzten Projekten klar dokumentiertes, vollständiges Universal-EPG, daher:

- zentrale EPG-URL nur für CH in `dach-legal.m3u`
- zusätzliche EPG-Zuordnung pro Sender/Gruppe wird im Player empfohlen

Details und Hinweise stehen in `epg-links.md` / `epg-links.en.md`.

---

## 🤖 Automatisierung (Agent & GitHub Actions)

- `scripts/update_playlist.py`
  - erzeugt `dach-legal.m3u` und `epg-links` neu
- `scripts/health_check.py`
  - ruft die wichtigsten Quelllisten auf und schreibt `health-report.md`
- `.github/workflows/update.yml`
  - läuft täglich per Cron
  - führt `update_playlist.py` und `health_check.py` aus
  - committed Änderungen automatisch

**Agent-Flow** (siehe `agent-flow.md` / `agent-flow.en.md`):

- prüft Quell-URLs
- markiert dauerhaft fehlerhafte Quellen
- erweitert ggf. Favoriten

---

## 🌐 GitHub Pages

Die Datei `index.html` dient als Landingpage und kann über GitHub Pages veröffentlicht werden (Branch `main`, Pfad `/`).

Empfohlene Konfiguration für dieses Projekt:

- Repository: `jbkunama1/hAi.iptv_List-Play`
- Pages: Source = `main` / root

---

## ⚖️ Lizenz

Dieses Projekt ist unter der **MIT-Lizenz** vorgesehen. Du kannst im GitHub-UI unter "Settings → General → Licensing" bzw. "Add license" eine MIT-Lizenzdatei hinzufügen.

---

## ⚖️ Rechtlicher Hinweis

Dieses Repository:

- soll ausschließlich auf **frei zugängliche, legal abrufbare Quellen** verweisen
- beansprucht keine Vollständigkeit
- trifft keine Aussage über die Rechtssituation in allen Ländern

Bitte beachte:

- lokale Gesetze und Nutzungsbedingungen der jeweiligen Anbieter
- Änderungen der Nutzungsrechte können jederzeit auftreten
