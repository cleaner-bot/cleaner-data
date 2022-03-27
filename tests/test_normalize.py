import pytest

from cleaner_data.normalize import normalize


testdata = (
    ("@everyone", ""),
    ("@here", ""),
    ("testhttp://test.com", "test"),
    ("a. b.cdef-gh", "a b cdef gh"),
    ("a\nb\nc", "a b c"),
    ("A B C", "a b c"),
    ("c b a", "a b c"),
    (" ".join("a" for _ in range(10000)), "a"),
)


@pytest.mark.parametrize("content, expected", testdata)
def test_normalize(content, expected):
    assert normalize(content) == expected
