import requests

token = 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ5MjA3MTk1MCwiaWF0IjoxNDkxNDY3MTUwfQ.eyJpZCI6Mn0.k8HWGAUUJtsk9bTN6z3E7BenoYfrv-LsI-RReYSJTEA'

def test_auth():
    url = 'http://127.0.0.1:5000/api/auth'
    data = {
        'username': 'vic',
        'password': 'Dd112211'
    }
    res = requests.post(url=url, data=data)
    print(res.status_code)
    print(res.content)
    print(res.headers)

def test_get_post():
    url = 'http://127.0.0.1:5000/api/post'
    data = {'page': 1, 'user': 'vic'}
    res = requests.get(url=url, data=data)
    print(res.status_code)
    print(res.content)

def test_post_post():
    url = 'http://127.0.0.1:5000/api/post'
    data = {'token': token, 'title': 'Test Restful api', 'text': 'Test post by rest........', 'tags': 'rest'}
    res = requests.post(url=url, data=data)
    print(res.status_code)
    print(res.content)

def test_put_post():
    url = 'http://127.0.0.1:5000/api/post/28'
    data = {'token': token, 'text': 'Test post by rest..... test put.....'}
    res = requests.put(url=url, data=data)
    print(res.status_code)
    print(res.content)

def test_delete_post():
    url = 'http://127.0.0.1:5000/api/post/28'
    data = {'token': token}
    res = requests.delete(url=url, data=data)
    print(res.status_code)
    print(res.content)

if __name__ == '__main__':
    test_get_post()