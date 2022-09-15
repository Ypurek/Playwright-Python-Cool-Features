from playwright.sync_api import expect
from pytest import fixture


@fixture
def test_case(alice):
    alice.goto('/tests')
    return alice


def test_locator_has_text(test_case):
    # find row locator by has_text, then find button locator
    row = test_case.locator('tbody tr', has_text='Successfull registration')
    row.locator('.passBtn').click()

    # same way with selectors chain and css pseudo class :has-text
    test_case.locator('tbody tr:has-text("Successfull registration") >> .passBtn').click()


def test_locator_has_locator(test_case):
    test_case.locator('tbody tr', has=test_case.locator('.delete_1')).locator('.passBtn').click()
    test_case.locator('tbody tr:has(.delete_1) .passBtn').click()


def test_locator_different_options(test_case):
    # if locator can be changed, you may put few, separated with coma. 1st found will be used
    test_case.locator('tbody tr:has-text("Successfull registration") >> .passBtn, pass_1, .aaa').click()


def test_locator_does_not_exist(test_case):
    not_existing_selector = '.not_existing_selector'

    # old fashion way
    assert test_case.query_selector(not_existing_selector) is None
    # brand-new with pytest assert
    assert test_case.locator(not_existing_selector).is_hidden()
    # brand-new with playwright expect
    expect(test_case.locator(not_existing_selector)).not_to_be_visible()


def test_locator_multiple_findings_handle(test_case):
    # click 1st button
    test_case.locator('.passBtn').first.click()
    # click 2nd button
    test_case.locator('.passBtn').nth(1).click()

    # first property work even if 1 locator found
    test_case.locator('.pass_1').first.click()


def test_locator_filter(test_case):
    # if locator still finds many elements, there is a way to filter them
    test_case.locator('tbody tr').filter(has=test_case.locator('.pass_1')).locator('.passBtn').click()


def test_locator_wait(alice):
    alice.goto('/demo')
    alice.locator('.waitAjaxRequests').fill('3')
    alice.locator('.waitAjax').click()
    last_record = alice.locator('p >> nth=2')
    # wait until element is visible
    # also we can wait it disappear
    # last_record.wait_for(state='hidden')
    last_record.wait_for()
    assert last_record.is_visible()
