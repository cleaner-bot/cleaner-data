import unicodedata

from .auto.unicode import data as _unicode_rawdata


_unicode_data = {}


def normalize_unicode(normalize_unicode: str) -> str:
    return "".join(
        _unicode_data.get(x, unicodedata.normalize("NFKD", x))
        for x in normalize_unicode
    )


def _init_unicode_data():
    for key, value in _unicode_rawdata.items():
        for variation in value:
            _unicode_data[variation] = key


_init_unicode_data()
del _init_unicode_data
