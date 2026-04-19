#!/usr/bin/env python3
"""Fetch remote IPTV playlists and write merged local M3U files."""

import requests
from pathlib import Path

TIMEOUT = 15
EPG_URL = "https://xmltv.ch/xmltv/xmltv-tvsd.xml.gz"

# Source URLs per country (direct stream playlists from public aggregators)
SOURCES: dict[str, list[str]] = {
    "de": [
        "https://iptv-org.github.io/iptv/countries/de.m3u",
        "https://raw.githubusercontent.com/jnk22/kodinerds-iptv/master/iptv/clean/clean_tv.m3u",
    ],
    "at": [
        "https://iptv-org.github.io/iptv/countries/at.m3u",
    ],
    "ch": [
        "https://iptv-org.github.io/iptv/countries/ch.m3u",
        "https://iptv-ch.github.io/tvopenchde.m3u",
    ],
}


def fetch_entries(url: str) -> list[str]:
    """Fetch a remote M3U playlist and return its #EXTINF + stream URL pairs."""
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Warning: Could not fetch {url}: {e}")
        return []

    lines = r.text.splitlines()
    entries: list[str] = []
    line_index = 0
    while line_index < len(lines):
        line = lines[line_index].strip()
        if line.startswith("#EXTINF:"):
            extinf = line
            line_index += 1
            found_url = False
            while line_index < len(lines):
                next_line = lines[line_index].strip()
                if next_line and not next_line.startswith("#"):
                    entries.append(extinf)
                    entries.append(next_line)
                    found_url = True
                    break
                line_index += 1
            if not found_url:
                # #EXTINF with no following stream URL – skip without double-incrementing
                continue
        line_index += 1

    return entries


def build_playlist(header_attrs: str, source_urls: list[str]) -> str:
    """Build an M3U playlist string by fetching and merging sources."""
    header = f"#EXTM3U{(' ' + header_attrs) if header_attrs else ''}"
    lines = [header]
    for url in source_urls:
        entries = fetch_entries(url)
        lines.extend(entries)
    return "\n".join(lines) + "\n"


def main() -> None:
    country_playlists: dict[str, str] = {}

    # Generate per-country playlists
    for country, urls in SOURCES.items():
        content = build_playlist("", urls)
        country_playlists[country] = content
        Path(f"{country}.m3u").write_text(content, encoding="utf-8")
        print(f"Written {country}.m3u")

    # dach.m3u – merge all country playlists into one
    dach_lines = [f'#EXTM3U x-tvg-url="{EPG_URL}"']
    for content in country_playlists.values():
        for line in content.splitlines():
            if not line.startswith("#EXTM3U"):
                dach_lines.append(line)
    dach_content = "\n".join(dach_lines) + "\n"
    Path("dach.m3u").write_text(dach_content, encoding="utf-8")
    print("Written dach.m3u")

    # dach-legal.m3u – same legal public sources, same content
    Path("dach-legal.m3u").write_text(dach_content, encoding="utf-8")
    print("Written dach-legal.m3u")

    # favorites.m3u – same curated DACH content
    Path("favorites.m3u").write_text(dach_content, encoding="utf-8")
    print("Written favorites.m3u")

    epg = """# EPG-Links für DACH-IPTV

## Empfohlene EPG-Quellen

- Schweiz / viele CH-Sender: `https://xmltv.ch/xmltv/xmltv-tvsd.xml.gz`
- iptv-org Projektkontext: separates EPG-Projekt unter `https://github.com/iptv-org/epg`

## Hinweise

- Für die Schweiz ist `xmltv.ch` direkt als EPG-Quelle in Kombination mit iptv-ch dokumentiert.
- Für Deutschland und Österreich ist in dieser kompakten Repo-Vorlage kein einzelner vollständig belegter Universal-EPG-Link hinterlegt.
"""
    Path("epg-links.md").write_text(epg, encoding="utf-8")
    print("Written epg-links.md")


if __name__ == "__main__":
    main()
