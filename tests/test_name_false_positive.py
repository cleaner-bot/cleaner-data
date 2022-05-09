import pytest

from cleaner_data.name import is_name_blacklisted, name_blacklist_ratio

testdata = ("1234",)


@pytest.mark.parametrize("name", testdata)
def test_name_blacklist(name: str):
    assert not is_name_blacklisted(name)
    assert name_blacklist_ratio(name) == 0
