import argparse
import gettext

import kiertotie.update as update
from kiertotie import log

lang = gettext.translation('messages', localedir='locale', languages=['de_DE'])
lang.install()
_ = lang.gettext  # German


def verify(options: argparse.Namespace) -> int:
    """Later alligator."""
    if options:
        update.process(
            proxy_data_path=options.proxy,
            anchor_path=options.anchor_path,
            script_path=options.update_path,
        )
        return 0
    log.error(_('YES'))
    return 2
