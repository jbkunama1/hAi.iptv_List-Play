# Agent-Flow: tägliche IPTV-Pflege

## Ziel

Ein Agent prüft täglich, ob sich die Quell-Playlists oder die dokumentierten EPG-Hinweise geändert haben, und aktualisiert danach das Repository.

## Eingaben

- `https://iptv-org.github.io/iptv/countries/de.m3u`
- `https://iptv-org.github.io/iptv/countries/at.m3u`
- `https://iptv-org.github.io/iptv/countries/ch.m3u`
- `https://iptv-ch.github.io/tvopenchde.m3u`
- `https://xmltv.ch/xmltv/xmltv-tvsd.xml.gz`

## Ablauf

1. Agent lädt die bekannten Quell-URLs.
2. Agent prüft HTTP-Status, Redirects und grobe Dateigröße.
3. Agent validiert, ob M3U-Inhalte mit `#EXTM3U` beginnen.
4. Agent schreibt daraus `dach-legal.m3u` neu.
5. Agent schreibt `epg-links.md` neu, falls sich dokumentierte EPG-Ziele ändern.
6. Agent erstellt bei Änderungen einen Commit.
7. Agent öffnet optional einen Issue, wenn eine Quelle dauerhaft fehlschlägt.

## Entscheidungsregeln

- Wenn eine Quelle nur temporär ausfällt, bleibt sie zunächst mit Kommentar erhalten.
- Wenn eine Quelle mehrfach fehlschlägt, wird sie markiert statt sofort gelöscht.
- Providergebundene CH-Listen bleiben klar gekennzeichnet.
- Nur öffentlich dokumentierte, frei erreichbare Quellen werden aufgenommen.

## Erweiterungen

- Senderduplikate filtern
- Favoritenliste erzeugen
- getrennte Dateien `de.m3u`, `at.m3u`, `ch.m3u`, `dach.m3u`
- Health-Check-Report als GitHub Actions Artifact
