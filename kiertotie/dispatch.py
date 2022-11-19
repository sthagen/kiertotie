import argparse
import gettext

de = gettext.translation('base', localedir='locale', languages=['de'])
de.install()
_ = de.gettext  # German


def verify(options: argparse.Namespace) -> int:
    """Later alligator."""
    if options:
        print(_('YES'))
        return 0
    return 2
