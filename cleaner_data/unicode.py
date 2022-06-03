import unicodedata

from .auto.unicode import data as _unicode_rawdata

_unicode_data: dict[str, str] = {}


def normalize_unicode(normalize_unicode: str) -> str:
    return (
        "".join(
            _unicode_data.get(x, unicodedata.normalize("NFKD", x))
            for x in normalize_unicode
        )
        .lower()
        .replace("1", "i")
        .replace("3", "e")
        .replace("0", "o")
        .replace("v", "u")
        .replace("w", "u")
        .replace("q", "o")
    )


def _init_unicode_data() -> None:
    for key, value in _unicode_rawdata.items():
        for variation in value:
            _unicode_data[variation] = key


_init_unicode_data()
del _init_unicode_data
