from app import app

def test_home():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200     # fixed!

def test_users():
    client = app.test_client()
    res = client.get('/users')
    assert res.status_code == 200      # fixed!