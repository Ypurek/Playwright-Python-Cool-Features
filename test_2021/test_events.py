from playwright.sync_api import Dialog, ConsoleMessage, Page, Response
from contextlib import contextmanager
import json
import time


def dialog_handler(dialog: Dialog):
    # just to show it works
    time.sleep(2)
    print('\n\n====== close dialog ====== \n\n')
    dialog.accept()


def console_handler(message: ConsoleMessage):
    print(message.text)


@contextmanager
def catch_response(page: Page):
    def response_handler(response: Response):
        print(json.dumps(response.json(), indent=4))

    page.on('response', response_handler)
    yield
    page.remove_listener('response', response_handler)


# read more https://playwright.dev/python/docs/events
def test_events(alice):
    alice.on('dialog', dialog_handler)
    alice.on('console', console_handler)
    alice.click('[href="/demo/"]')
    alice.click('.newPage')
    # alice.click('[href="/"]')


# Example of event handling within context manager
def test_events_once(alice):
    alice.click('[href="/"]')
    alice.once('response', lambda response: print('hello world'))
    alice.click('.refresh input')
    alice.wait_for_timeout(1000)


# Example of event handling within context manager
def test_events_with_cm(alice):
    alice.click('[href="/"]')
    with catch_response(alice):
        alice.click('.refresh input')
        alice.wait_for_timeout(1000)
