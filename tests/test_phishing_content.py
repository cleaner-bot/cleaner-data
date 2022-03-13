import textwrap

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
