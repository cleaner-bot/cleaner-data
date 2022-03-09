from cleaner_data.domains import (
    is_whitelisted,
    is_blacklisted,
    get_highest_blacklist_match,
)


def test_is_whitelisted():
    assert is_whitelisted("discord.com")
    assert is_whitelisted("cdn.discordapp.com")
    assert not is_whitelisted("baddomain.com")


def test_is_blacklisted():
    assert not is_blacklisted("discord.com")
    assert is_blacklisted("go-discord.com")
    assert is_blacklisted("test.go-discord.com")


def test_get_highest_match():
    assert 1 >= get_highest_blacklist_match("discord.com") >= 0.9
