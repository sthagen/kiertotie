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
        '--facet',
        '-f',
        dest='facet',
        required=True,
        help='facet key of target document',
    )
    parser.add_argument(
        '--target',
        '-t',
        dest='target',
        required=True,
        help='target document key',
    )
    parser.add_argument(
        '--document-root',
        '-d',
        dest='doc_root',
        default='',
        help='Root of the document tree to visit. Optional\n(default: positional tree root value)',
        required=False,
    )
    parser.add_argument(
        'doc_root_pos',
        nargs='?',
        default='',
        help='Root of the document tree to visit. Optional\n(default: empty for PWD)',
    )
    parser.add_argument(
        '--verbose',
        '-v',
        dest='verbose',
        default=False,
        action='store_true',
        help='work logging more information along the way\n(default: False)',
    )
    if not argv:
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if not options.doc_root:
        if options.doc_root_pos:
            options.doc_root = options.doc_root_pos
        else:
            options.doc_root = str(pathlib.Path.cwd())

    doc_root = pathlib.Path(options.doc_root)
    if doc_root.exists():
        if doc_root.is_dir():
            return options
        parser.error(f'requested tree root at ({doc_root}) is not a folder')

    parser.error(f'requested tree root at ({doc_root}) does not exist')


def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return dispatch.verify(options)
