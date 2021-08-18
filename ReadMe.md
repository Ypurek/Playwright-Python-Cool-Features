# Code Samples for QA Day 2021

By Oleksii Ostapov

## Useful links

- [Playwright website](https://playwright.dev/python/)
- [QA Mania Telegram Channel](https://t.me/qamania) <-- SUBSCRIBE 🥳
- [QA Mania blog](https://qamania.org/)
- [Playwright coding hints collection](https://qamania.org/hint/playwright/)
- [My Playwright + Python course](https://www.udemy.com/instructor/courses)

## Precondition

In order to run these tests locally you need

1. Install [Sample project](https://github.com/Ypurek/TestMe-TCM) which will be tested by tests. It is easy-to-run Test
   Case Management system created with Django with main purpose to be tested by autotests. There is installation guide
2. Install test dependencies using command `pip install -r requirements.txt`
3. Install Playwright web browser drivers using command `playwright install`. Check [guide](https://playwright.dev/python/docs/intro#installation)

## Overview
In order to simplify code [pytest](https://pytest.org/) is used. It is possible to run same code without, as it provided in official documentation.  
[conftest.py](conftest.py) contains main fixture with Playwright itself and page fixture, with already authenticated user  

## Tests
### Test scenario with multiple roles
**Documentation**: https://playwright.dev/python/docs/multi-pages  
**Test**: [test_context.py](test_context.py)  
**Description**: In this test 2 separate contexts created for different users. They act in the same test at the same time!

### Test with injecting JS
**Documentation**: https://playwright.dev/python/docs/api/class-page#page-evaluate   
**Test**: [test_evaluate.py](test_evaluate.py)  
**Description**: In this test JS directly in browser executed and value received back into test. Any king of complicated JS logic can be triggered directly  

### Test events
**Documentation**: https://playwright.dev/python/docs/events    
**Test**: [test_events.py](test_events.py)   
**Description**: In these tests different scenarios of events handling are shown. My favorite way - create context manager, because in this case you can control upcoming events better  

### Test routes
**Documentation**: https://playwright.dev/python/docs/network  
**Test**: [test_route.py](test_route.py)   
**Description**: In these tests different scenarios of handling browser HTTP requests are shown. You can abort, modify, mock or just log any browser request  

### Test selectors
**Documentation**: https://playwright.dev/python/docs/selectors  
**Test**: [test_selectors.py](test_selectors.py)   
**Description**: In this test the most awesome Playwright feature is displayed - Selectors. You have a lot of ways to locate you elements  

### Test waitings
**Documentation**: https://playwright.dev/python/docs/api/class-page#page-wait-for-selector  
**Test**: [test_waiting.py](test_waiting.py)  
**Description**: In these tests different scenarios shown on how you can wait for element, page load or any kind of event emitted by web browser    