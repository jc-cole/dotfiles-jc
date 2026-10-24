#!/usr/bin/env python3
"""Link the fish config into XDG_CONFIG_HOME, preserving existing files."""

import os
from datetime import datetime
from pathlib import Path


def main():
    source = Path(__file__).resolve().parent / "fish"
    target = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / "fish"
    backup = target / "backups" / datetime.now().strftime("before-dotfiles-%Y%m%d-%H%M%S-%f")
    for relative in (
        "config.fish",
        "functions/fish_prompt.fish",
        "conf.d/fish_frozen_theme.fish",
        "conf.d/zz_nothing_to_fear.fish",
    ):
        src = source / relative
        dst = target / relative
        if not src.is_file():
            raise FileNotFoundError(src)
        if dst.is_symlink() and dst.resolve() == src:
            print(f"Already linked: {dst}")
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists() or dst.is_symlink():
            saved = backup / relative
            saved.parent.mkdir(parents=True, exist_ok=True)
            dst.rename(saved)
            print(f"Backup: {saved}")
        dst.symlink_to(src)
        print(f"Linked: {dst} -> {src}")


if __name__ == "__main__":
    main()
