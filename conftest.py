from pytest import fixture
from playwright.sync_api import sync_playwright

SLO_MO = None
HEADLESS = False


@fixture(scope='module')
def chromium():
    """
    Main fixture. Creates Chrome browser and yields it into tests
    Shows how to work with docs
    """
    with sync_playwright() as p:
        chromium = p.chromium.launch(headless=HEADLESS, slow_mo=SLO_MO)
        yield chromium
        chromium.close()


@fixture(scope='module')
def page(chromium):
    # base url provided for context, so goto method can user only endpoint
    context = chromium.new_context(permissions=["geolocation"],
                                   geolocation={"latitude": 48.8, "longitude": 2.3},
                                   base_url='http://127.0.0.1:8000')
    page = context.new_page()
    yield page
    page.close()
    context.close()


@fixture(scope='module')
def alice(page):
    page.goto('')
    page.fill('#id_username', 'alice')
    page.fill('id=id_password', 'Qamania123')
    page.click('text="Login"')
    return page
