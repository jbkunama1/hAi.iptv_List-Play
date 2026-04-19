from pathlib import Path

playlist = '''#EXTM3U x-tvg-url="https://xmltv.ch/xmltv/xmltv-tvsd.xml.gz"

# DACH IPTV – legale, öffentlich verfügbare Quellen (Version 1)
# Fokus: Deutschland, Österreich, Schweiz
# Automatisch erzeugt.

# --- Deutschland (iptv-org Länderplaylist) ---
#EXTINF:-1 group-title="Deutschland",Deutschland – iptv-org Länderplaylist
https://iptv-org.github.io/iptv/countries/de.m3u

# --- Österreich (iptv-org Länderplaylist) ---
#EXTINF:-1 group-title="Österreich",Österreich – iptv-org Länderplaylist
https://iptv-org.github.io/iptv/countries/at.m3u

# --- Schweiz (iptv-org Länderplaylist) ---
#EXTINF:-1 group-title="Schweiz",Schweiz – iptv-org Länderplaylist
https://iptv-org.github.io/iptv/countries/ch.m3u

# --- Schweiz DE offen (iptv-ch) ---
#EXTINF:-1 group-title="Schweiz",Schweiz – offene deutschsprachige Sender (iptv-ch)
https://iptv-ch.github.io/tvopenchde.m3u
'''

epg = '''# EPG-Links für DACH-IPTV

## Empfohlene EPG-Quellen

- Schweiz / viele CH-Sender: `https://xmltv.ch/xmltv/xmltv-tvsd.xml.gz`
- iptv-org Projektkontext: separates EPG-Projekt unter `https://github.com/iptv-org/epg`

## Hinweise

- Für die Schweiz ist `xmltv.ch` direkt als EPG-Quelle in Kombination mit iptv-ch dokumentiert.
- Für Deutschland und Österreich ist in dieser kompakten Repo-Vorlage kein einzelner vollständig belegter Universal-EPG-Link hinterlegt.
'''

Path('dach-legal.m3u').write_text(playlist, encoding='utf-8')
Path('epg-links.md').write_text(epg, encoding='utf-8')
