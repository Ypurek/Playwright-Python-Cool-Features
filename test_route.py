import json

from playwright.sync_api import Route, Request


# read more https://playwright.dev/python/docs/network
def test_review(alice):
    # use list as reference object to transfer data from handler to test
    request_data = list()

    def handler(route: Route, request: Request):
        request_data.append(request.post_data_json)
        route.continue_()

    # can be done in context manager
    alice.goto('/tests/')

    alice.route('**/status', handler)
    alice.click('tbody tr >> nth=0 >> .passBtn')
    alice.unroute('**/status', handler)

    assert request_data[0] == {'status': 'PASS'}


def test_fulfill(alice):
    def handler(route: Route, request: Request):
        route.fulfill(status=200, body=json.dumps({"runId": 1000}))

    # can be done in context manager
    alice.goto('/tests/')

    alice.click('tbody tr >> nth=0 >> .passBtn')
    alice.route('**/status', handler)
    alice.click('tbody tr >> nth=0 >> .failBtn')
    alice.unroute('**/status', handler)
    alice.reload()

    assert alice.text_content('.testRow_1 .ttStatus') == 'PASS'


def test_modify(alice):
    def handler(route: Route, request: Request):
        route.continue_(post_data=json.dumps({'status': 'FAIL'}))

    # can be done in context manager
    alice.goto('/tests/')

    alice.route('**/status', handler)
    alice.click('tbody tr >> nth=0 >> .passBtn')
    alice.unroute('**/status', handler)
    alice.reload()

    assert alice.text_content('.testRow_1 .ttStatus') == 'FAIL'


def test_abort(alice):
    def handler(route: Route, request: Request):
        route.abort()

    # can be done in context manager
    alice.goto('/tests/')
    alice.click('.testRow_1 .passBtn')

    alice.route('**/status', handler)
    alice.click('tbody tr >> nth=0 >> .failBtn')
    alice.unroute('**/status', handler)
    alice.reload()

    assert alice.text_content('.testRow_1 .ttStatus') == 'PASS'
