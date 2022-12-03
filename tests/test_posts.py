from tests.test_helper import RouteTester
from pytest import mark

root_url = 'http://localhost:5000/'

tester = RouteTester(f'{root_url}posts')
payload_put = {
                "author": "test", 
                 "id": 5, 
                 "content": "Como testar testar testar testar?",
                 "title": "Test Test Test"
            }

payload_post =  {
            
                "author": "test", 
                 "id": 5, 
                 "content": "Como testar testar testar testar?",
                 "title": "Test"
            }

@mark.parametrize(
    'endpoint, status',
    [('/',200), ('', 308)]
)
def test_posts_route_status(endpoint, status):
    assert tester.RouteGetStatus(endpoint) == status

def test_posts_by_id_route_status():
    assert tester.RouteGetStatus('/1') == 200
    
def test_posts_post_status():
    assert tester.RoutePostStatus('/', payload_post)

def test_posts_put_status():
    assert tester.RoutePutStatus('/5', payload_put) == 200

def test_posts_delete_status():
    assert tester.RouteDeleteStatus('/5')
    
    
