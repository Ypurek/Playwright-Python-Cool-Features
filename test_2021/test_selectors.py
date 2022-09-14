# read more https://playwright.dev/python/docs/selectors
def test_selectors(alice):
    # CSS selector + visible pseudo-class
    alice.click('a[href="/demo/"]:visible')
    # XPath selector
    alice.click('//a[@href="/tests/"]')
    # Chain of selectors + intermediate match
    test_case = alice.query_selector('xpath=//table >> *css=tr >> text="successfull login check"')
    for i in range(4):
        test_case.query_selector('.passBtn').click()
        test_case.query_selector('.failBtn').click()

    text = "empty"
    for i in range(4):
        # css selector + has pseudo-class
        alice.click(f'tr:has-text("{text}") .passBtn')
        alice.click(f'tr:has-text("{text}") .failBtn')

    for i in range(4):
        # Chain of selectors + nth selector (numeration from 0)
        alice.click('tr >> nth=1 >> .passBtn')
        alice.click('tr >> nth=1 >> .failBtn')
