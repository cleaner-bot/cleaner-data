import pytest

from cleaner_data.unicode import normalize_unicode

testdata = (
    ("𝕙Ëʟp d𝓮šK", "hELp desK"),
    ("ＭＥＥ６ Ａｖａｔａｒｓ ＮＦＴ | Ｍｉｎｔ", "MEE6 Avatars NFT | Mint"),
    ("𝙈𝙀𝙀6 𝘼𝙫𝙖𝙩𝙖𝙧𝙨 𝙉𝙁𝙏 | 𝘽𝙊𝙏", "MEE6 Avatars NFT | BOT"),
    # samples from triviabot
    (
        "Ⅰn 1978 Rеѵ Jim ‐‐‐‐‐‐‐‐‐‐ lеаⅾs 911 pеοplе in sυiciⅾе in Jοnеstοѡn, Ԍυуаnа.",
        "In 1978 Rev Jim ---------- leads 911 people in suicide in Jonestown, Guyana.",
    ),
    (
        "Ԍеnеrаtiοn X Tοуs: Bυilⅾing tοοl nаmеⅾ аftеr Ciѵil Wаr prеsiⅾеnt",
        "Generation X toys: Building tool named after Civil War president",
    ),
    (
        "Nаmе Thе ʏеаr: Amеricаn sυffrаgist Sυsаn B. Anthοnу ⅾiеⅾ.",
        "Name The Year: American suffragist Susan B. Anthony died.",
    ),
    (
        "Nаmе thе Artist/Bаnⅾ thаt rеcοrⅾеⅾ this sοng: Ηigh Spееⅾ Dirt",
        "Name the Artist/Band that recorded this song: High Speed Dirt",
    ),
    ("ՍnscrаmЬlе this ѡοrⅾ: riοclthе", "Unscramble this word: rioclthe"),
    ("Whаt is Stаr‐Lοrⅾ's miⅾⅾlе nаmе?", "What is Star-Lord's middle name?"),
    (
        "Stаr Wаrs: Rаcеrs in thе Bοοntа Εѵе Clаssic",
        "Star Wars: Racers in the Boonta Eve Classic",
    ),
    (
        "Whаt nυmЬеr is signifiеⅾ Ьу thе prеfiх 'mеgа'",
        "What number is signified by the prefix 'mega'",
    ),
    (
        "Thе mеtаl pаrt аt thе еnⅾ οf а pеncil is 20% #####.",
        "The metal part at the end of a pencil is 20% #####.",
    ),
    (
        "Ⅰf sаnⅾ is mеltеⅾ ѡith limеstοnе аnⅾ sοⅾiυm cаrЬοnаtе ѡhаt is fοrmеⅾ",
        "If sand is melted with limestone and sodium carbonate what is formed",
    ),
    ("Whаt is thе chеmicаl sуmЬοl fοr gοlⅾ?", "What is the chemical symbol for gold?"),
)


@pytest.mark.parametrize("text,expected", testdata)
def test_normalize_unicode(text, expected):
    assert normalize_unicode(text) == normalize_unicode(expected)
