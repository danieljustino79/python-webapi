from bottle import response
from json import dumps


class HttpUtils:
    @staticmethod
    def response_ok(data):
        return HttpUtils.response_data(200, data)

    @staticmethod
    def response_status(status):
        response.status = status
        response.content_type = 'application/json'
        return None

    @staticmethod
    def response_data(status, data):
        response.status = status
        response.content_type = 'application/json'
        return dumps(data)
