from cleaner_data.domains import (
    get_highest_domain_blacklist_match,
    is_domain_blacklisted,
    is_domain_whitelisted,
)


def test_is_whitelisted():
    assert is_domain_whitelisted("discord.com")
    assert is_domain_whitelisted("cdn.discordapp.com")
    assert not is_domain_whitelisted("baddomain.com")


def test_is_blacklisted():
    assert not is_domain_blacklisted("discord.com")
    assert is_domain_blacklisted("go-discord.com")
    assert is_domain_blacklisted("test.go-discord.com")


def test_get_highest_match():
    assert 1 >= get_highest_domain_blacklist_match("discord.com") >= 0.9
    assert get_highest_domain_blacklist_match("go-discord.com") == 1
