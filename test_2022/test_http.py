from playwright.sync_api import expect
from pytest import fixture


# import requests


# def test_http_old_fashion_way():
#     session = requests.session()
#     session.post('<full url>/login', {'username': 'user', 'password': 'password'})
#     response = session.get('<full url>/requested data')
#     data = response.json()
#     assert data['key'] == 'value'


def test_basic(alice):
    # no login in advance
    # no full url, base_url provided in the fixture
    response = alice.request.get('/getstat')
    expect(response).to_be_ok()


def test_full_url(alice):
    response = alice.request.get('https://github.com/Ypurek/')
    expect(response).to_be_ok()


def test_new_test_case(alice, http_post_condition):
    # get csrf token
    alice.goto('/test/new')
    csrf_token = alice.locator('form input[type=hidden]').get_attribute('value')
    test_name = 'shiny new test of http'

    alice.request.post('/test/new', form={'csrfmiddlewaretoken': csrf_token,
                                          'name': test_name,
                                          'description': 'nice'})

    alice.goto('/tests')
    new_test = alice.locator('tbody tr', has_text=test_name)
    expect(new_test).to_be_visible()


@fixture
def http_post_condition(alice):
    yield
    alice.goto('/tests')
    alice.locator('tbody tr:has-text("shiny new test of http") >> .deleteBtn').click()
