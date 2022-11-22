import httpx
root_url = 'http://localhost:5000/'

def test_users_status():
    assert httpx.get(f'{root_url}users/').status_code == 200
    
def test_users_by_id_status():
    assert httpx.get(f'{root_url}users/1').status_code == 200
    
def test_users_create_status():
    payload =  { 
             'id': 7, 
             'username': 'teste_pytest', 
             'email': 'teste@testar.com', 
             'password': 'teste123' 
            }
    
    assert httpx.post(f'{root_url}users/', json=payload).status_code == 200

def test_users_edit_status():
    payload = {
        'id': 7,
        'username': 'teste_pytest_edita',
        'email': 'teste@testar.com',
        'password': 'teste123'
    }
    
    assert httpx.put(f'{root_url}users/7', json=payload)

def test_users_delete_status():
    assert httpx.delete(f'{root_url}users/7').status_code == 200

def test_posts_status():
    assert httpx.get(f'{root_url}posts/').status_code == 200

def test_posts_by_id_status():
    assert httpx.get(f'{root_url}posts/1').status_code == 200
    
    
