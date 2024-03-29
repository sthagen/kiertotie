"""Detour (Finnish: kiertotie) per rsync proxy to https mirror node."""

import datetime as dti
import json
import logging
import os
import pathlib
from typing import List, Union, no_type_check

# [[[fill git_describe()]]]
__version__ = '2023.1.5+parent.ccac1ba7'
# [[[end]]] (checksum: 1658aff3b014e31e3ee3121c56f64e36)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

APP_ALIAS = str(pathlib.Path(__file__).parent.name)
APP_ENV = APP_ALIAS.upper()
APP_NAME = locals()['__doc__']
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = f'.{APP_ALIAS}.json'

BASE_URL = 'https://master.qt.io/'
DASH = '-'
EASING = 3
NL = '\n'
SP = ' '
ESP = '\\' + SP
URL_ENC_SP = '%20'
RATE = 2_000_000
TS_FORMAT = '%Y-%m-%d %H:%M:%S +00:00'
HTTP_404_FILE = """\
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
</body></html>
"""
HTTP_404_SIZE_BYTES = 196
HTTP_404_BYTES_TOKEN = b'<!DOCTYPE'
HTTP_404_BYTES_TOKEN_LENGTH = len(HTTP_404_BYTES_TOKEN)

DEFAULT_LF_ONLY = 'YES'
log = logging.getLogger()  # Module level logger is sufficient
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{APP_ALIAS}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO

TS_FORMAT_LOG = '%Y-%m-%dT%H:%M:%S'
TS_FORMAT_PAYLOADS = '%Y-%m-%d %H:%M:%S.%f UTC'

EntryType = dict[str, Union[int, str]]
DimensionType = dict[str, list[EntryType]]
ProxyType = dict[str, Union[int, DimensionType]]

__all__: List[str] = [
    'BASE_URL',
    'DASH',
    'EASING',
    'RATE',
    'ENCODING',
    'NL',
    'SP',
    'ESP',
    'URL_ENC_SP',
    'TS_FORMAT',
    'HTTP_404_FILE',
    'HTTP_404_SIZE_BYTES',
    'HTTP_404_BYTES_TOKEN',
    'HTTP_404_BYTES_TOKEN_LENGTH',
    'ProxyType',
    'load',
    'log',
]


@no_type_check
def formatTime_RFC3339(self, record, datefmt=None):  # noqa
    """HACK A DID ACK we could inject .astimezone() to localize ..."""
    return dti.datetime.fromtimestamp(record.created, dti.timezone.utc).isoformat()  # pragma: no cover


@no_type_check
def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global log  # pylint: disable=global-statement

    log_format = {
        'format': '%(asctime)s %(levelname)s [%(name)s]: %(message)s',
        'datefmt': TS_FORMAT_LOG,
        # 'filename': LOG_PATH,
        'level': LOG_LEVEL if level is None else level,
    }
    logging.Formatter.formatTime = formatTime_RFC3339
    logging.basicConfig(**log_format)
    log = logging.getLogger(APP_ENV if name is None else name)
    log.propagate = True


def load(data_path: Union[str, pathlib.Path]) -> ProxyType:
    """Load the data from JSON."""
    with open(data_path, 'rt', encoding=ENCODING) as handle:
        data: ProxyType = json.load(handle)
    return data


init_logger(name=APP_ENV, level=logging.DEBUG if DEBUG else None)
