from fixture import client
from helpers import createJhonDoe, createUser, createJWT, getRole
from ms.repositories import UserRepository


def test_create(client):
    role = getRole('client')
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'phone': '1231231232',
        'email': 'jhon.doe.2@example.com',
        'password': 'secret',
        'role_id': role.id
    }
    response = client.post('/api/v1/users/admin', headers=headers, data=data)
    assert response.status_code == 200

def test_read(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.get(f'/api/v1/users/admin/{user.id}', headers=headers)
    assert response.status_code == 200

def test_update(client):
    role = getRole('client')
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'phone': '1231231232',
        'email': 'jhon.doe.2@example.com',
        'password': 'secret',
        'role_id': role.id
    }
    response = client.put(f'/api/v1/users/admin/{user.id}', headers=headers, data=data)
    assert response.status_code == 200

def test_active(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post(f'/api/v1/users/admin/{user.id}/activate', headers=headers)
    assert response.status_code == 204

def test_deactive(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.delete(f'/api/v1/users/admin/{user.id}/activate', headers=headers)
    assert response.status_code == 204

def test_softdelete(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.delete(f'/api/v1/users/admin/{user.id}', headers=headers)
    assert response.status_code == 204

def test_restore(client):
    userRepo = UserRepository()
    role = getRole('client')
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    new_user = userRepo.add({
        'phone': '1231231232',
        'email': 'jhon.doe.2@example.com',
        'password': 'secret',
        'role_id': role.id
    })
    userRepo.soft_delete(new_user.id)
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post(f'/api/v1/users/admin/{new_user.id}/restore', headers=headers)
    assert response.status_code == 204

def test_harddelete(client):
    userRepo = UserRepository()
    role = getRole('client')
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    user_to_delete = createUser({
        'phone': '1231231232',
        'email': 'jhon.doe+01@example.com',
        'password': 'secret',
        'role_id': role.id
    })
    userRepo.soft_delete(user_to_delete.id)
    response = client.delete(f'/api/v1/users/admin/{user_to_delete.id}/hard', headers=headers)
    assert response.status_code == 204
