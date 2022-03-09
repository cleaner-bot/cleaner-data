from .unicode import normalize_unicode as _normalize_unicode
from .url import remove_urls as _remove_urls


def normalize(
    content: str,
    *,
    remove_urls: bool = True,
    remove_mentions: bool = True,
    normalize_unicode: bool = True,
    normalize_words: bool = True,
):
    if remove_mentions:
        content = content.replace("@everyone", "").replace("@here", "").strip()
    if remove_urls:
        content = _remove_urls(content).strip()
    if normalize_unicode:
        content = _normalize_unicode(content)
    if normalize_words:
        words = content.split()
        content = " ".join(
            x for x in sorted(set(normalize_word(w) for w in words)) if x
        )
    return content


def normalize_word(word: str) -> str:
    return "".join(x.lower() for x in word if x.isalpha())
