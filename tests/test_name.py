import pytest

from cleaner_data.auto.name_blacklist import data
from cleaner_data.name import is_name_blacklisted, name_blacklist_ratio
from cleaner_data.unicode import normalize_unicode

testdata = (
    "Moderator Academy Exam",
    "Moderator Exam",
    "Exam Moderator",
    "Partners Moderator",
    "Developer Moderator",
    "Developers Moderator",
    "D𝗂scord Moderators",
    "D𝗂scord Moderator",
    "D𝗂scord Exam Moderators",
    "D𝗂scord Exam Moderator",
    "D𝗂scord Academy Moderators",
    "Support Moderator",
    "Support Mod",
    "Discord Message",
    "Discord API Intents",
    "Developer Message",
    "Hypesquad",
    "Partners",
    "Mod Academy",
    "Moderation Academy",
    "Moderator Academy",
    "Academy Moderator",
    "Partner Moderator",
    "Discord Moderator",
    "Support",
    "Discord Moderator Academy",
    "Hypesquad Events",
    "Intents Devbot",
)


@pytest.mark.parametrize("name", testdata)
def test_name_blacklist(name: str) -> None:
    assert is_name_blacklisted(name)
    assert name_blacklist_ratio(name) == 1


@pytest.mark.parametrize("name", data)
def test_all_are_normalized(name: str) -> None:
    assert name == normalize_unicode(name)
