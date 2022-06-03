import typing

from .unicode import normalize_unicode as _normalize_unicode
from .url import remove_urls as _remove_urls


def normalize(
    content: str,
    *,
    remove_urls: bool = True,
    remove_mentions: bool = True,
    lowercase_content: bool = True,
    normalize_unicode: bool = True,
    normalize_words: bool = True,
) -> str:
    if remove_mentions:
        content = content.replace("@everyone", "").replace("@here", "").strip()
    if remove_urls:
        content = _remove_urls(content).strip()
    if normalize_unicode:
        content = _normalize_unicode(content)
    if lowercase_content:
        content = content.lower()
    if normalize_words:
        words = split_at_non_alpha(content)
        content = " ".join(x for x in sorted(set(words)) if x)
    return content


def split_at_non_alpha(word: str) -> typing.Generator[str, None, None]:
    start = 0
    for end, char in enumerate(word):
        if not char.isalpha():
            if end > start:
                yield word[start:end]
            start = end + 1

    if start < len(word):
        yield word[start:]
