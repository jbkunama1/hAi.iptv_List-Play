import requests
from pathlib import Path

TIMEOUT = 5

SOURCES = {
    "de": "https://iptv-org.github.io/iptv/countries/de.m3u",
    "at": "https://iptv-org.github.io/iptv/countries/at.m3u",
    "ch": "https://iptv-org.github.io/iptv/countries/ch.m3u",
    "ch_open_de": "https://iptv-ch.github.io/tvopenchde.m3u",
    "free_tv": "https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8",
    "kodinerds_clean": "https://raw.githubusercontent.com/jnk22/kodinerds-iptv/master/clean.m3u",
}


def check_source(name: str, url: str) -> str:
    try:
        r = requests.get(url, timeout=TIMEOUT)
        status = r.status_code
        ok = 200 <= status < 400
        return f"- {name}: {'OK' if ok else 'PROBLEM'} (HTTP {status})\n"
    except Exception as e:
        return f"- {name}: ERROR ({e})\n"


def main() -> None:
    lines = ["# Health Check Report\n\n"]
    for name, url in SOURCES.items():
        lines.append(check_source(name, url))
    Path("health-report.md").write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
