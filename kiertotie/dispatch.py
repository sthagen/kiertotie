import argparse
import gettext

lang = gettext.translation('messages', localedir='locale', languages=['de_DE'])
lang.install()
_ = lang.gettext  # German


def verify(options: argparse.Namespace) -> int:
    """Later alligator."""
    if options:
        print(_('YES'))
        return 0
    return 2
