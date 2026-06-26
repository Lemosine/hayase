from __future__ import annotations

import json
from pathlib import Path


DEFAULT_CONFIG = Path("config.example.json")


def load_config(path: Path = DEFAULT_CONFIG) -> dict:
    if not path.exists():
        return {"feeds": [], "download_directory": "./downloads", "poll_interval_minutes": 30}
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    config = load_config()
    feed_count = len(config.get("feeds", [])) if isinstance(config.get("feeds", []), list) else 0
    print("Hayase starter is ready.")
    print(f"Configured feeds: {feed_count}")


if __name__ == "__main__":
    main()
