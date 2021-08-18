from playwright.sync_api import Response


# read more https://playwright.dev/python/docs/api/class-page#page-wait-for-selector
def test_wait_state(alice):
    alice.click('a[href="/demo/"]')
    alice.click('.waitAjax')
    # waits for all ajax requests done
    alice.wait_for_load_state('networkidle')
    assert len(alice.query_selector_all('.ajaxResponses p')) == 5


def test_wait_selector(alice):
    alice.click('a[href="/demo/"]')
    alice.click('.waitAjax')
    # waits for selector exists
    alice.wait_for_selector('.ajaxResponses p >> nth=4')
    assert len(alice.query_selector_all('.ajaxResponses p')) == 5


def test_expect_navigation(alice):
    alice.click('a[href="/demo/"]')
    # stop test execution until navigation is not done
    with alice.expect_navigation(url="**/waitPage**"):
        alice.click('.waitPage')
    assert alice.is_visible('text="Status: ok after 5"')


def test_expect_response(alice):
    def response_predicate(response: Response):
        return response.status == 200 and response.request.method == 'GET'

    alice.click('a[href="/"]')
    # stop test execution until http response received with status code 200
    with alice.expect_response(response_predicate):
        alice.click('input[type=button]')


def test_expect_page(alice):
    alice.click('a[href="/demo/"]')
    # stop test execution until 2nd tab is openned
    with alice.context.expect_page() as page:
        alice.click('.newPage', modifiers=['Control'])
    assert page.value.url == 'http://127.0.0.1:8000/demo/'
    page.value.close()
