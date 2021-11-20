# read more https://playwright.dev/python/docs/api/class-page#page-evaluate
def test_js(alice):
    result = alice.evaluate('''
    var aaa = function(x, y){
        return x + y;
    }
    aaa(2, 3);
    ''')
    assert result == 5
