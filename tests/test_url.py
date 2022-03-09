from cleaner_data.url import has_url, get_urls, remove_urls


def test_has_url():
    assert has_url("hello world http://test.com")
    assert has_url("hello worldhttps://test.com")
    assert not has_url("hello world ftp://test.com")
    assert not has_url("hello world")


def test_get_urls():
    data = "hello world http://test.com /pathhttp://test.org ftp://test.ftp"
    assert list(get_urls(data)) == ["http://test.com", "http://test.org"]


def test_remove_urls():
    data = "hello world http://test.com http://test.com/abcdef ftp://test.org"
    assert remove_urls(data) == "hello world   ftp://test.org"
