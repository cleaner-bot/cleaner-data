import pytest

from cleaner_data.unicode import normalize_unicode


testdata = (
    ("𝕙Ëʟp d𝓮šK", "hELp desK"),
    ("ＭＥＥ６ Ａｖａｔａｒｓ ＮＦＴ | Ｍｉｎｔ", "MEE6 Avatars NFT | Mint"),
    ("𝙈𝙀𝙀6 𝘼𝙫𝙖𝙩𝙖𝙧𝙨 𝙉𝙁𝙏 | 𝘽𝙊𝙏", "MEE6 Avatars NFT | BOT"),
)


@pytest.mark.parametrize("text,expected", testdata)
def test_normalize_unicode(text, expected):
    assert normalize_unicode(text) == expected
