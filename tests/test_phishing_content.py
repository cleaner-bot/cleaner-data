import textwrap

import pytest

from cleaner_data.auto.phishing_content import data
from cleaner_data.normalize import normalize
from cleaner_data.phishing_content import get_highest_phishing_match


def test_get_highest_match():
    input = textwrap.dedent(
        """@everyone
    • Free Discord Nitro AirDrop from Steam!
    • Share your screen in HD
    • Collect or create your own custom and animated emoji
    • Support the server and let everyone know about your support
    https://redacted.com/welcomes"""
    )

    assert get_highest_phishing_match(input) == 1
    assert get_highest_phishing_match(input[20:]) >= 0.9


@pytest.mark.parametrize("name", data)
def test_all_are_normalized(name):
    assert name == normalize(name, normalize_unicode=False)
