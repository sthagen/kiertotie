#! /usr/bin/env python
"""Creating the folders for the hierarchy if they do not exist from the proxy data."""
import datetime as dti
import os
import pathlib

from kiertotie import DASH, TS_FORMAT, load, log


def span(
    proxy_data_path: str | pathlib.Path,
    anchor_path: str | pathlib.Path | None = None,
    verbose: bool = False,
) -> int:
    """Span the folder tree per proxy folder data."""
    anchor = pathlib.Path.cwd() if anchor_path is None else pathlib.Path(anchor_path)
    log.debug(f'assuming anchor as ({anchor}) in span tree')

    store_path = pathlib.Path(proxy_data_path)
    log.debug(f'loading proxy data from ({store_path}) in span tree')
    repo = load(store_path)

    root_folder_str = store_path.name.split(DASH)[1]
    if root_folder_str == 'development':
        root_folder_str += '_releases'
    root_folder = pathlib.Path(root_folder_str)
    log.debug(f'assuming root folder as ({root_folder}) below anchor ({anchor}) in span tree')

    folder_count = repo['count_folders']
    log.debug(f'creating {folder_count} folders below the root')
    for folder in repo['tree']['folders']:  # type: ignore
        folder_path = folder['path']
        if folder_path == '.':
            continue
        path = anchor / root_folder / folder_path  # type: ignore
        path.mkdir(parents=True, exist_ok=True)
        ts = (
            dti.datetime.strptime(folder['timestamp'], TS_FORMAT)  # type: ignore
            .replace(tzinfo=dti.timezone.utc)
            .timestamp()
        )
        os.utime(path, times=(ts, ts))

    log.debug('folder hiearchy is complete in span tree')
    return 0
