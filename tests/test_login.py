from tests.test_helper import RouteTester

tester = RouteTester('http://localhost:5000/login')

payload = {
    'email': 'rhuanlopes536@gmail.com',
    'password': '12345678'
}

def test_login():
    assert tester.RoutePostStatus('/', payload) == 200