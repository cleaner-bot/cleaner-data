from .auto.name_blacklist import data as _blacklist_data
from .normalize import normalize


def is_name_blacklisted(
    name: str, collection: set[str] = None, normalize_name: bool = True
) -> bool:
    if normalize_name:
        name = normalize(name)
    if collection is None:
        collection = _blacklist_data
    return all(w in collection for w in name.split())


def name_blacklist_ratio(
    name: str, collection: set[str] = None, normalize_name: bool = True
) -> float:
    if normalize_name:
        name = normalize(name)
    if collection is None:
        collection = _blacklist_data
    words = name.split()
    return sum(1 for w in words if w in collection) / len(words)
