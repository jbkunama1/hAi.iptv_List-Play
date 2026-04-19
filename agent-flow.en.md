# Agent flow: daily IPTV maintenance

## Goal

An agent checks daily whether the source playlists or the documented EPG hints have changed and updates the repository accordingly.

## Inputs

- `https://iptv-org.github.io/iptv/countries/de.m3u`
- `https://iptv-org.github.io/iptv/countries/at.m3u`
- `https://iptv-org.github.io/iptv/countries/ch.m3u`
- `https://iptv-ch.github.io/tvopenchde.m3u`
- `https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8`
- `https://raw.githubusercontent.com/jnk22/kodinerds-iptv/master/clean.m3u`
- `https://xmltv.ch/xmltv/xmltv-tvsd.xml.gz`

## Flow

1. Agent downloads all known source URLs.
2. Agent checks HTTP status, redirects and basic file size.
3. Agent validates that M3U content starts with `#EXTM3U`.
4. Agent regenerates `dach-legal.m3u`, `de.m3u`, `at.m3u`, `ch.m3u`, `dach.m3u`, `favorites.m3u`.
5. Agent rewrites `epg-links` files if documented EPG targets change.
6. Agent creates a commit if there are changes.
7. Agent optionally opens an issue if a source fails repeatedly.

## Rules

- If a source fails temporarily, keep it with a comment first.
- If a source fails repeatedly, mark it instead of deleting it immediately.
- CH provider playlists stay clearly labelled.
- Only publicly documented, freely reachable sources are used.

## Possible extensions

- Filter duplicates
- Generate a favourites-only list
- Separate `de.m3u`, `at.m3u`, `ch.m3u`, `dach.m3u` by genres
- Export a health check report as GitHub Actions artifact
