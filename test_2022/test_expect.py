from playwright.sync_api import expect
from pytest import fixture


@fixture
def alice_tc(alice):
    alice.goto('/tests')
    alice.locator('.passBtn.pass_1').click()
    return alice


def test_expect_basic(alice_tc):
    status = alice_tc.locator('.testStatus_1')

    # assert 'PASS' in status.text_content()
    expect(status).to_have_text('PASS', timeout=5000)

    # assert status.is_visible()
    expect(status).to_be_visible()

    # assert not status.is_hidden()
    expect(status).not_to_be_hidden()

    # assert '123456' not in status.get_attribute('class')
    expect(status).not_to_have_class('123456')

    # assert 'testStatus_1 PASS' == status.get_attribute('class')
    expect(status).to_have_class('testStatus_1 PASS')


def test_expect_details(alice_tc):
    pass_btn = alice_tc.locator('.passBtn.pass_1')
    # name and value are mandatory

    # assert pass_btn.get_attribute('onclick') == "setStatus(1, 'PASS')"
    expect(pass_btn).to_have_attribute(name='onclick', value="setStatus(1, 'PASS')")

    # no way to get css from locator ¯\_(ツ)_/¯
    expect(pass_btn).to_have_css(name='margin', value='0px 5px 0px 0px')


def test_expect_count(alice_tc):
    menu_items = alice_tc.locator('.menuInner li')

    # assert menu_items.count() == 5
    expect(menu_items).to_have_count(5)


def test_input(alice):
    text = 'hello world'
    alice.goto('/test/new')
    test_name = alice.locator('#id_name')
    test_name.type(text)

    # assert test_name.input_value() == text
    # check input value without overhead :)
    expect(test_name).to_have_value(text)
