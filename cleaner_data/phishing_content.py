from Levenshtein import ratio  # type: ignore

from .auto.phishing_content import data as _phishing_data
from .normalize import normalize


def get_highest_phishing_match(content: str, match=ratio) -> float:
    content = normalize(content)
    if content in _phishing_data:
        return 1
    return max(match(content, message) for message in _phishing_data)
