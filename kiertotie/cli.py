"""Command line interface for detour (Finnish: kiertotie) per rsync proxy to https mirror node.."""
import argparse
import pathlib
import sys
from typing import List, Union

import kiertotie.dispatch as dispatch
from kiertotie import APP_ALIAS, APP_NAME


def parse_request(argv: List[str]) -> Union[int, argparse.Namespace]:
    """DRY."""
    parser = argparse.ArgumentParser(
        prog=APP_ALIAS, description=APP_NAME, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--proxy',
        '-p',
        dest='proxy',
        required=False,
        help='proxy data path',
    )
    parser.add_argument(
        'proxy_pos',
        nargs='?',
        default='',
        help='proxy data path',
    )
    parser.add_argument(
        '--updater',
        '-u',
        dest='update_path',
        required=False,
        default=None,
        help='update shell script path to write',
    )
    parser.add_argument(
        '--anchor',
        '-a',
        dest='anchor_path',
        required=False,
        default=None,
        help='absolute anchor path (webroot) below which we mirror',
    )
    parser.add_argument(
        '--span-tree',
        '-s',
        dest='span_folder_tree',
        default=False,
        action='store_true',
        help='span the folder tree from proxy data',
    )
    parser.add_argument(
        '--verbose',
        '-v',
        dest='verbose',
        default=False,
        action='store_true',
        help='be verbose in logging and write status info to shell scripts',
    )
    if not argv:
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if not options.proxy:
        if options.proxy_pos:
            options.proxy = options.proxy_pos
        else:
            options.proxy = str(pathlib.Path.cwd())

    proxy = pathlib.Path(options.proxy)
    if proxy.exists():
        if proxy.is_file():
            return options
        parser.error(f'requested proxy data path ({proxy}) is no file')

    parser.error(f'requested proxy data path ({proxy}) does not exist')


def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return dispatch.verify(options)
