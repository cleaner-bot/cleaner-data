import pytest

from cleaner_data.domains import (
    get_highest_domain_blacklist_match,
    is_domain_blacklisted,
    is_domain_whitelisted,
)

false_positives = (
    "gist.github.com",
    "discordpy.readthedocs.io",
    "discord.js.org",
)


@pytest.mark.parametrize("domain", false_positives)
def test_false_positive(domain):
    if is_domain_whitelisted(domain):
        return

    assert not is_domain_blacklisted(domain)
    assert get_highest_domain_blacklist_match("gist.github.com") < 0.9
