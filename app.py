from http import HTTPStatus

from bottle import get, post, request, route, run

from application.user_manager import UserManager
from libs.http_utils import HttpUtils


@post('/user')
def add():
    body = request.json
    name = body.get('name')
    email = body.get('email')

    _id = UserManager.add(name, email)
    if type(_id) is int:
        result = {'id': _id}
        return HttpUtils.response_ok(result)
    else:
        return HttpUtils.response_status(HTTPStatus.BAD_REQUEST)


@post('/user/<_id:int>/permission')
def add_permission(_id):
    try:
        body = request.json
        permissions = body.get('permissions')

        successfully = UserManager.add_permission(_id, permissions)
        if successfully is True:
            return HttpUtils.response_status(HTTPStatus.OK)
        else:
            return HttpUtils.response_status(HTTPStatus.BAD_REQUEST)
    except AttributeError:
        return HttpUtils.response_status(HTTPStatus.BAD_REQUEST)


@get('/user')
def get():
    users = UserManager.get_users()
    return HttpUtils.response_ok(users)


@route('/user/<id_:int>')
def get_by_id(_id):
    user = UserManager.get_by_id(_id)
    if user is not None:
        return HttpUtils.response_ok(user)
    else:
        return HttpUtils.response_status(HTTPStatus.NOT_FOUND)


run(host='localhost', port=8082, debug=True)
