from fixture import app, client
from helpers import createJhonDoe, createJWT


def test_profile(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    res = client.get('/api/v1/users/profile', headers=headers)
    assert res.status_code == 200
