# read more https://playwright.dev/python/docs/api/class-page#page-evaluate
def test_js(alice):
    height = alice.evaluate("window.innerHeight")
    assert height == 720
