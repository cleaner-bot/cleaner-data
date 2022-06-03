import typing

from Levenshtein import ratio  # type: ignore

from .auto.domain_blacklist import data as _blacklist_data
from .auto.domain_whitelist import data as _whitelist_data


def is_domain_whitelisted(domain: str) -> bool:
    return domain_in_list(domain, _whitelist_data)


def is_domain_blacklisted(domain: str) -> bool:
    return domain_in_list(domain, _blacklist_data)


def domain_in_list(domain: str, collection: set[str]) -> bool:
    if domain in collection:
        return True
    for hostname in collection:
        if domain.endswith("." + hostname):
            return True
    return False


def get_highest_domain_blacklist_match(
    domain: str, match: typing.Callable[[str, str], float] = ratio
) -> float:
    if domain in _blacklist_data:
        return 1
    return max(match(domain, x) for x in _blacklist_data)
