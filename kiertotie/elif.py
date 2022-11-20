#! /usr/bin/env python
"""Creating the fetch script for the files in the hierarchy from JSON proxy data."""
import json
import pathlib
import random
import sys

BASE_URL = 'https://master.qt.io/'
DASH = '-'
ACTIONS = []
DEFAULT_SCRIPT = 'fetch.sh'
EASING = 3
NL = '\n'
SP = ' '
ESP = '\\' + SP
URL_ENC_SP = '%20'
RATE = 2_000_000
ENCODING = 'utf-8'
TS_FORMAT = '%Y-%m-%d %H:%M:%S +00:00'

if len(sys.argv) != 2:
    print('elif.py json-file', file=sys.stderr)
    sys.exit(2)

store_path = pathlib.Path(sys.argv[1])
with open(store_path, 'rt', encoding=ENCODING) as handle:
    repo = json.load(handle)

root_folder = store_path.name.split(DASH)[1]
if root_folder == 'development':
    root_folder += '_releases'

folder_count = repo['count_folders']
ACTIONS.append('#! /usr/bin/env bash')
ACTIONS.append(f'# Derived root folder to be ({root_folder})')
ACTIONS.append(f'echo "Initializing the tree below root folder with random waits between 1 and {EASING} secs"')
transfers = repo['count_files']
size_files_bytes = repo['size_files_bytes']
ACTIONS.append(
    f'# Detected {transfers} files with {size_files_bytes} bytes across {folder_count} folders below {root_folder}'
)
anchor = pathlib.Path.cwd()
bytes_cum = 0
for n, entry in enumerate(repo['tree']['files'], start=1):
    entry_path = entry['path']
    if entry_path == '.':
        continue
    path = pathlib.Path(entry_path)
    size_bytes = entry['size']
    secs_est = int(size_bytes / RATE)
    secs_est_disp = 'less than a second' if secs_est < 1 else f'approx. {secs_est} seconds'
    bytes_cum += size_bytes
    nap = random.randint(1, EASING)  # nosec B311
    ACTIONS.append(f'echo sleeping for {nap} secs before transfering file {n} of {transfers}')
    ACTIONS.append(f'sleep {nap}')
    ACTIONS.append(f'cd {anchor}/{root_folder}/{path.parent} || exit 1')
    ACTIONS.append('pwd')
    ACTIONS.append(
        f'echo started the transfer {n} of {transfers} requesting {size_bytes} bytes'
        f' assuming {secs_est_disp} at "$(date +"%Y-%m-%d %H:%M:%S +00:00")"'
    )
    if SP not in str(path):
        ACTIONS.append(f"echo curl -kORLs --limit-rate 2000k '{BASE_URL}{root_folder}/{path}'")
        ACTIONS.append(f"curl -kORLs --limit-rate 2000k '{BASE_URL}{root_folder}/{path}'")
    else:
        path_url_enc = str(path).replace(SP, URL_ENC_SP)
        path_local = f'{str(path.name).replace(SP, ESP)}'
        ACTIONS.append(f"echo curl -kRLs --limit-rate 2000k '{BASE_URL}{root_folder}/{path_url_enc}' -o '{path_local}'")
        ACTIONS.append(f"curl -kRLs --limit-rate 2000k '{BASE_URL}{root_folder}/{path_url_enc}' -o '{path_local}'")
    ACTIONS.append(
        f'echo transfer is complete {n} of {transfers} for cum. {bytes_cum} of'
        f' tot. {size_files_bytes} bytes at "$(date +"%Y-%m-%d %H:%M:%S +00:00")"'
    )

ACTIONS.append('echo OK')
ACTIONS.append('')  # Final newline at end of fetch script

with open(DEFAULT_SCRIPT, 'wt', encoding=ENCODING) as handle:
    handle.write(NL.join(ACTIONS))
