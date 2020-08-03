from bottle import get, post, request, route, run
from application.user import User


@post('/user')
def add():
    body = request.json
    name = body.get('name')
    email = body.get('email')

    _user = User()
    _id = _user.add(name, email)
    if isinstance(_id, int):
        return str(_id)
    else:
        return 'error'


@post('/user/<id_:int>/permission')
def add_permission(id_):
    body = request.json
    permissions = body.get('permissions')

    _user = User()
    id_validate = _user.add_permission(id_, permissions)
    if isinstance(id_validate, int):
        return str(id_validate)
    else:
        return 'error'


@get('/user')
def get():
    _user = User()
    return _user.get_users()


@route('/user/<id_:int>')
def get_by_id(id_):
    _user = User()
    _obj = _user.get_by_id(id_)
    if isinstance(_obj, object):
        return _obj
    else:
        return 'error'


run(host='localhost', port=8081, debug=True)
