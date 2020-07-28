from application import user
from bottle import get, post, request, route, run
#import json


@post('/user')
def add():
    '''
    name = request.forms.get('name')
    email = request.forms.get('email')
    '''

    body = request.json
    name = body.get('name')
    email = body.get('email')

    if user.add(name, email):
        return 'ok'
    else:
        return 'error'


@post('/user/<id:int>/permission')
def add_permission(id):
    body = request.json
    permissions = body.get('permissions')

    if user.add_permission(id,  permissions):
        return 'ok'
    else:
        return 'error'


@get('/user')
def get():
    return user.get()


@route('/user/<id:int>')
def getbyid(id):
    return user.get_by_id(id)




run(host='localhost', port=8081, debug=True)
