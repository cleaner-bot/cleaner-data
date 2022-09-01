import pytest

from cleaner_data.url import get_urls, has_url, remove_urls


def test_has_url() -> None:
    assert has_url("hello world http://test.com")
    assert has_url("hello worldhttps://test.com")
    assert not has_url("hello world ftp://test.com")
    assert not has_url("hello world")


def test_get_urls() -> None:
    data = "hello world http://test.com /pathhttp://test.org ftp://test.ftp"
    assert list(get_urls(data)) == ["http://test.com", "http://test.org"]


def test_remove_urls() -> None:
    data = "hello world http://test.com http://test.com/abcdef ftp://test.org"
    assert remove_urls(data) == "hello world   ftp://test.org"


@pytest.mark.parametrize(
    ("message", "expected"),
    (
        ("http://", "http://"),
        ("http://\\test.com", "http://test.com"),
        ("http://\\\\\\\\\\\\\\\\\\test.com", "http://test.com"),
        ("http://\\/test.com", "http://test.com"),
        ("http://\\/\\/\\/\\/\\/\\/\\/test.com", "http://test.com"),
        ("[test](http://test.com)", "http://test.com"),
        ("http://test.com)", "http://test.com"),
        ("http://test.com()", "http://test.com()"),
        ("http://test.com())", "http://test.com()"),
        ("http://test.com]", "http://test.com"),
        ("http://test.com[]", "http://test.com["),
        ("http://test.com])", "http://test.com]"),
        ("http://test.com[])", "http://test.com[]"),
        ("http://test.com))", "http://test.com)"),
        ("http://test.com(()", "http://test.com(()"),
        ("http://test.com(())", "http://test.com(())"),
        ("http://test.com(()))", "http://test.com(())"),
        ("http://test.com(()", "http://test.com(()"),
        ("http://test.com[[[[]]]", "http://test.com[[[["),
        ("http://test.com[[[[[]]]]])", "http://test.com[[[[[]]]]]"),
    ),
)
def test_markdown_url(message: str, expected: str) -> None:
    (url,) = list(get_urls(message))
    assert url == expected
