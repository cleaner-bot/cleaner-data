import pytest

from cleaner_data.domains import (
    is_whitelisted,
    is_blacklisted,
    get_highest_blacklist_match,
)


false_positives = (
    "gist.github.com",
    "discordpy.readthedocs.io",
    "discord.js.org",
)


@pytest.mark.parametrize("domain", false_positives)
def test_false_positive(domain):
    if is_whitelisted(domain):
        return

    assert not is_blacklisted(domain)
    assert get_highest_blacklist_match("gist.github.com") < 0.9
