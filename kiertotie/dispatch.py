import argparse
import gettext
import logging

import kiertotie.tree as tree
import kiertotie.update as update
from kiertotie import log

lang = gettext.translation('messages', localedir='locale', languages=['de_DE'])
lang.install()
_ = lang.gettext  # German


def verify(options: argparse.Namespace) -> int:
    """Later alligator."""
    if options:
        verbose = options.verbose
        if verbose:
            logging.getLogger().setLevel(logging.DEBUG)

        if options.span_folder_tree:
            code = tree.span(
                proxy_data_path=options.proxy,
                anchor_path=options.anchor_path,
                verbose=verbose,
            )
            if code:
                log.error(f'span tree action returned with code ({code})')
                return code
        return update.process(
            proxy_data_path=options.proxy,
            anchor_path=options.anchor_path,
            script_path=options.update_path,
            verbose=verbose,
        )
    log.error(_('YES'))
    return 2
