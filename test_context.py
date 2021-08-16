from pytest import fixture
import random as r


@fixture(scope='module')
def bob(chromium):
    context = chromium.new_context(permissions=["geolocation"],
                                   geolocation={"latitude": 10, "longitude": 10})
    page = context.new_page()
    page.goto('http://127.0.0.1:8000')
    page.fill('#id_username', 'bob')
    page.fill('id=id_password', 'Qamania123')
    page.click('text="Login"')
    return page


# read more https://playwright.dev/python/docs/multi-pages
def test_roles(alice, bob):
    total = bob.text_content('.total span')

    alice.click('a[href="/test/new"]')
    alice.fill('#id_name', f'test name {r.random()}')
    alice.fill('#id_description', 'new test!')
    alice.click('.btn input')

    # make sure response received before checking text content
    with bob.expect_response(lambda response: response.status == 200):
        bob.click('.refresh input')
    new_total = bob.text_content('.total span')

    assert int(total) + 1 == int(new_total)
