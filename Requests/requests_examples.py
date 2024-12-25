import requests
import sys

def get_all():
    resp = requests.get("http://jsonplaceholder.typicode.com/posts/")
    if resp.status_code != 200:
        # This means something went wrong.
        raise Exception('GET /tasks/{}'.format(resp.status_code))
    for element in resp.json():
        print(element)

def get_one():
    resp = requests.get("http://jsonplaceholder.typicode.com/posts/1")
    if resp.status_code != 200:
        # This means something went wrong.
        raise Exception('GET /tasks/{}'.format(resp.status_code))
    print(resp.json())

def filter():
    resp = requests.get("http://jsonplaceholder.typicode.com/posts?userId=1")
    if resp.status_code != 200:
        # This means something went wrong.
        raise Exception('GET /tasks/{}'.format(resp.status_code))
    for element in resp.json():
        print(element)

def post():
    data = {
        'id': 101,
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    resp = requests.post("http://jsonplaceholder.typicode.com/posts/",data=data)
    if resp.status_code != 201:
        raise Exception('POST /posts/{}'.format(resp.status_code))
    print('Created task. ID: {}'.format(resp.json()))

def put():
    data = {
        'id': 1,
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    resp = requests.put("http://jsonplaceholder.typicode.com/posts/1",data=data)
    if resp.status_code != 200:
        raise Exception('PUT /posts/{}'.format(resp.status_code))
    print('Updated task. ID: {}'.format(resp.json()))

def patch():
    data = {
        'id': 1,
        'title': 'foo',
        'body': '...',
        'userId': 1
    }

    resp = requests.patch("http://jsonplaceholder.typicode.com/posts/1",data=data)
    if resp.status_code != 200:
        raise Exception('PATCH /posts/{}'.format(resp.status_code))
    print('Patched task. ID: {}'.format(resp.json()))

def delete():
    resp = requests.delete("http://jsonplaceholder.typicode.com/posts/1")
    if resp.status_code != 200:
        raise Exception('DELETE /posts/{}'.format(resp.status_code))
    print('Deleted task. ID: {}'.format(resp.json()))

if __name__ == '__main__':
    meth = sys.argv[1]

    if meth == 'getall':
        get_all()
    elif meth == 'getone':
        get_one()
    elif meth == 'filter':
        filter()
    elif meth == 'post':
        post()
    elif meth == 'put':
        put()
    elif meth == 'patch':
        patch()
    elif meth == 'delete':
        delete()