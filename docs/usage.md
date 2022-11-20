# Usage

## Help Screen

```console
❯ kiertotie --help
usage: kiertotie [-h] [--proxy PROXY] [--updater UPDATE_PATH] [--anchor ANCHOR_PATH] [--span-tree] [--verbose] [proxy_pos]

Detour (Finnish: kiertotie) per rsync proxy to https mirror node.

positional arguments:
  proxy_pos             proxy data path

options:
  -h, --help            show this help message and exit
  --proxy PROXY, -p PROXY
                        proxy data path
  --updater UPDATE_PATH, -u UPDATE_PATH
                        update shell script path to write
  --anchor ANCHOR_PATH, -a ANCHOR_PATH
                        absolute anchor path (webroot) below which we mirror
  --span-tree, -s       span the folder tree from proxy data
  --verbose, -v         be verbose in logging and write status info to shell scripts
```

## Some Example

```console
❯ python -m kiertotie bridge/qt-development-20221120T171240Z.json -u updater -v
2022-11-20T20:26:31.306356+00:00 DEBUG [KIERTOTIE]: assuming anchor as (/abs/path/to/cwd) in process update
2022-11-20T20:26:31.306640+00:00 DEBUG [KIERTOTIE]: loading proxy data from (bridge/qt-development-20221120T171240Z.json) in process update
2022-11-20T20:26:31.307683+00:00 DEBUG [KIERTOTIE]: assuming root folder as (development_releases) below anchor (/abs/path/to/cwd) in process update
2022-11-20T20:26:31.307710+00:00 DEBUG [KIERTOTIE]: creating shell script at (updater)
2022-11-20T20:26:31.330418+00:00 DEBUG [KIERTOTIE]: created shell script with 10629 lines at (updater) from process update
```

Best inspect the shell script (`updater`) before executing and if possible verify with `shellcheck`:

```console
❯ shellcheck updater
```

A less verbose logging and at the same time smaller shell script (less lines) results from:

```console
❯ python -m kiertotie gist/bridge/qt-development-20221120T171240Z.json -u updater
❯ wc -l updater
    9370 updater
```

Results may vary depending on the status of the local tree, upstream activity (changes),
as well as the size of the mirrored subtree.
