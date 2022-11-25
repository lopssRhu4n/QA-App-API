from pytest import mark
from tests.test_helper import RouteTester

root_url = 'http://localhost:5000/'

users_tester = RouteTester(f'{root_url}users')
payload_put = {
        'id': 7,
        'username': 'teste_pytest_edita',
        'email': 'teste@testar.com',
        'password': 'teste123'
    }

payload_post =  { 
             'id': 7, 
             'username': 'teste_pytest', 
             'email': 'teste@testar.com', 
             'password': 'teste123' 
            }

def test_users_route_status():
    assert users_tester.RouteGetStatus('/') == 200

def test_users_by_id_route_status():
    assert users_tester.RouteGetStatus('/1') == 200
    
def test_users_post_status():
    assert users_tester.RoutePostStatus('/', payload_post)

def test_users_put_status():
    assert users_tester.RoutePutStatus('/7', payload_put) == 200

def test_users_delete_status():
    assert users_tester.RouteDeleteStatus('/7')
    
    
