# Dotfiles

## Fish

The authoritative fish configuration lives in `fish/`. Install it with:

```sh
python3 install-fish.py
```

The installer symlinks the config, prompt, and theme files into
`~/.config/fish/` (or `$XDG_CONFIG_HOME/fish/`). Existing files are moved
into a timestamped `fish/backups/` directory under that config location.
Running the installer again leaves correct links alone.

Edit files in this repo or through their symlinks; both change the same files.
Fish's `fish_variables`, generated files, and backups stay local and are not
tracked. The two theme files load alphabetically: `fish_frozen_theme.fish`
provides the base, and `zz_nothing_to_fear.fish` applies the custom palette.

Open a new fish shell after installing to load the configuration.

## Kitty

`kitty/kitty.conf` is symlinked to `~/.config/kitty/kitty.conf` on this machine.
On another machine, back up any existing config and link this file into
`$XDG_CONFIG_HOME/kitty/kitty.conf` (default: `~/.config/kitty/kitty.conf`).
Restart Kitty after installation to enable transparency and dynamic opacity.
Use Ctrl+Shift+A, then 1 for an opaque background, or D to restore the configured
opacity. Ctrl+Shift+F5 reloads subsequent config edits.
