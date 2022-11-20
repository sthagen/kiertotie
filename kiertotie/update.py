"""Prepare entry and gone transactions from comparing local hierarchy with proxy data."""
import datetime as dti
import pathlib
import random

from kiertotie import (
    BASE_URL,
    DASH,
    EASING,
    ENCODING,
    ESP,
    HTTP_404_BYTES_TOKEN,
    HTTP_404_BYTES_TOKEN_LENGTH,
    HTTP_404_FILE,
    HTTP_404_SIZE_BYTES,
    NL,
    RATE,
    SP,
    TS_FORMAT,
    URL_ENC_SP,
    EntryType,
    load,
    log,
)

DEFAULT_SCRIPT = 'update.sh'


def shell(path: str | pathlib.Path, commands: list[str]) -> None:
    """Dump the commands into a shell script at path."""
    with open(path, 'wt', encoding=ENCODING) as handle:
        handle.write(NL.join(commands))


def assess_files(
    upstreams: list[EntryType],
    anchor: pathlib.Path,
    root_folder: pathlib.Path,
    commands: list[str],
    verbose: bool = False,
) -> list[EntryType]:
    """DRY."""
    updates = []
    for n, entry in enumerate(upstreams, start=1):
        entry_path = entry['path']
        if entry_path == '.':
            continue
        path = pathlib.Path(str(entry_path))

        if not (anchor / root_folder / path.parent).is_dir():
            if verbose:
                commands.append(f'# - New file {root_folder}/{path} in new folder')
            updates.append(entry)
            continue

        if not (anchor / root_folder / path).is_file():
            if verbose:
                commands.append(f'# - New file {root_folder}/{path} in existing folder')
            updates.append(entry)
            continue

        stat_found = (anchor / root_folder / path).stat()
        size_bytes_found = stat_found.st_size
        log.debug(f'local path ({root_folder / path}) pointing to {size_bytes_found} bytes is interesting ...')
        if verbose:
            commands.append(
                f'# ... Local path {root_folder / path} pointing to {size_bytes_found} bytes is interesting ...'
            )
        sampled_bytes = b''
        removed_http_404 = False
        if size_bytes_found == HTTP_404_SIZE_BYTES:
            with open(anchor / root_folder / path, 'rb') as raw_reader:
                sampled_bytes = raw_reader.read(HTTP_404_BYTES_TOKEN_LENGTH)
                commands.append(
                    f'# ... ... Read initial {HTTP_404_BYTES_TOKEN_LENGTH} bytes'
                    f' from {root_folder / path} being {sampled_bytes}'  # type: ignore
                )
        if sampled_bytes and sampled_bytes == HTTP_404_BYTES_TOKEN:
            text_content = ''
            with open(anchor / root_folder / path, 'rt', encoding=ENCODING) as text_reader:
                text_content = text_reader.read()
            if text_content == HTTP_404_FILE:
                log.warning(
                    f'detected HTTP/404 response file ({root_folder / path})'
                    ' in local hierarchy and added removal command'
                )
                commands.append(f'echo Removing HTTP/404 response file {root_folder / path} from local hierarchy:')
                commands.append(f'rm -f {anchor / root_folder / path}')
                size_bytes_found = 0
                removed_http_404 = True

        size_bytes_upstream = entry['size']
        if size_bytes_found == size_bytes_upstream:
            if path.name not in ('timestamp.tx', 'timestamp.txt', 'md5sums.txt'):
                if verbose:
                    commands.append(f'# - Skipping same size file {root_folder}/{path} in existing folder')
                continue
            commands.append(f'# - Overwriting same size file {root_folder}/{path} in existing folder')
        elif removed_http_404:
            commands.append(
                f'# - Will replace HTTP/404 response file {root_folder}/{path} with {size_bytes_upstream} bytes'
                f' from upstream in existing folder'
            )
        else:
            if verbose:
                commands.append(
                    f'# - Different size file {root_folder}/{path} with {size_bytes_found}'
                    f' instead {size_bytes_upstream} bytes upstream in existing folder'
                )
        updates.append(entry)

    return updates


def process(
    proxy_data_path: str | pathlib.Path,
    anchor_path: str | pathlib.Path | None = None,
    script_path: str | pathlib.Path | None = None,
    verbose: bool = False,
) -> int:
    """Generate folder tree below current working directory according to proxy data."""
    anchor = pathlib.Path.cwd() if anchor_path is None else pathlib.Path(anchor_path)
    log.debug(f'assuming anchor as ({anchor}) in process update')

    store_path = pathlib.Path(proxy_data_path)
    log.debug(f'loading proxy data from ({store_path}) in process update')
    repo = load(store_path)

    root_folder_str = store_path.name.split(DASH)[1]
    if root_folder_str == 'development':
        root_folder_str += '_releases'
    root_folder = pathlib.Path(root_folder_str)
    log.debug(f'assuming root folder as ({root_folder}) below anchor ({anchor}) in process update')

    script_path = pathlib.Path(DEFAULT_SCRIPT) if script_path is None else pathlib.Path(script_path)
    log.debug(f'creating shell script at ({script_path})')

    actions = ['#! /usr/bin/env bash']
    actions.append(f'# Derived root folder to be ({root_folder}) below anchor ({anchor})')
    actions.append(f'echo "Initializing the tree below root folder with random waits between 1 and {EASING} secs"')

    present = set()
    actions.append(f'# Inventarizing storage folders below {root_folder}')
    shared_root_str = f'{root_folder}/'
    for path in root_folder.rglob('*'):
        if not path.is_dir():
            continue
        path_str = str(path)[len(shared_root_str) :]
        if path_str:
            present.add(path_str)
    actions.append(f'# * found {len(present)} storage folders below {root_folder}')

    possibly_gone = set(f for f in present)
    upstream_folders = [
        f for f in reversed(sorted(f['path'] for f in repo['tree']['folders'])) if f != '.'  # type: ignore
    ]
    upstream_folder_born = {
        f['path']: dti.datetime.strptime(f['timestamp'], TS_FORMAT).replace(tzinfo=dti.timezone.utc)  # type: ignore
        for f in repo['tree']['folders']  # type: ignore
    }
    folder_count = repo['count_folders']
    maybe_enter = set(upstream_folders)
    actions.append('# Subtracting folders present upstream from gone and update enter section')
    for local_name in upstream_folders:
        possibly_gone.discard(local_name)  # type: ignore
        if local_name in present:
            maybe_enter.discard(local_name)
    gone_count = len(possibly_gone)
    actions.append(f"# * found {gone_count} gone storage folder{'' if gone_count == 1 else 's'} below {anchor}:")
    if verbose:
        for f in sorted(possibly_gone):
            actions.append(f'#  - {root_folder}/{f}')
    enter_count = len(maybe_enter)
    actions.append(f"# * found {enter_count} enter folder{'' if gone_count == 1 else 's'} below {anchor}:")
    if verbose:
        for f in sorted(maybe_enter):  # type: ignore
            actions.append(f'#  + {root_folder}/{f} from {upstream_folder_born[f]}')

    candidate_count = repo['count_files']
    actions.append(
        f'# Detected {candidate_count} candidate entrie{"" if candidate_count == 1 else "s"}'
        f' from upstream across {folder_count} folders below {anchor / root_folder}'
    )

    updates = assess_files(
        repo['tree']['files'],  # type: ignore
        anchor=anchor,
        root_folder=root_folder,
        commands=actions,
        verbose=verbose,
    )

    transfers = len(updates)
    size_files_bytes = sum(entry['size'] for entry in updates)  # type: ignore
    bytes_cum = 0
    for n, entry in enumerate(updates, start=1):
        entry_path = entry['path']
        if entry_path == '.':
            continue
        path = pathlib.Path(str(entry_path))
        size_bytes_upstream = int(entry['size'])
        secs_est = int(size_bytes_upstream / RATE)
        secs_est_disp = 'less than a second' if secs_est < 1 else f'approx. {secs_est} seconds'
        bytes_cum += size_bytes_upstream
        nap = random.randint(1, EASING)  # nosec B311
        actions.append(f'echo sleeping for {nap} secs before transfering file {n} of {transfers}')
        actions.append(f'sleep {nap}')
        actions.append(f'mkdir -p "{anchor}/{root_folder}/{path.parent}" || exit 1')
        actions.append(f'cd "{anchor}/{root_folder}/{path.parent}" || exit 1')
        actions.append('pwd')
        actions.append(
            f'echo started the transfer {n} of {transfers} requesting {size_bytes_upstream} bytes'
            f' assuming {secs_est_disp} at "$(date +"%Y-%m-%d %H:%M:%S +00:00")"'
        )
        if SP not in str(path):
            actions.append(f"echo curl -kORLs --limit-rate 2000k '{BASE_URL}{root_folder}/{path}'")
            actions.append(f"curl -kORLs --limit-rate 2000k '{BASE_URL}{root_folder}/{path}'")
        else:
            path_url_enc = str(path).replace(SP, URL_ENC_SP)
            path_local = f'{str(path.name).replace(SP, ESP)}'
            actions.append(
                f"echo curl -kRLs --limit-rate 2000k '{BASE_URL}{root_folder}/{path_url_enc}' -o '{path_local}'"
            )
            actions.append(f"curl -kRLs --limit-rate 2000k '{BASE_URL}{root_folder}/{path_url_enc}' -o '{path_local}'")
        actions.append(
            f'echo transfer is complete {n} of {transfers} for cum. {bytes_cum} of'
            f' tot. {size_files_bytes} bytes at "$(date +"%Y-%m-%d %H:%M:%S +00:00")"'
        )

    actions.append('echo OK')
    actions.append('')  # Final newline at end of fetch script

    shell(script_path, actions)
    log.debug(f'created shell script with {len(actions) - 1} lines at ({script_path}) from process update')

    return 0
