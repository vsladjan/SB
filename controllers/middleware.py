from flask import Request, Response
from util.error import Error
from util.helper import Helper

class Middleware:

    def __init__(self, app):
        self.app = app
        self.helper = Helper()

    # check in middleware is X-username header there, if not return error
    def __call__(self, environ, start_response):
        request = Request(environ)

        HEADER_XUSERNAME = 'X-username'
        xusername = request.headers.get(HEADER_XUSERNAME)

        error = None
        if xusername:
            xusernameerror = not self.helper.checkRegex('^[a-zA-Z0-9_]{4,32}$', xusername)
            if xusernameerror:
                error = Error(400, 102, "Bad request, X-username header is not in valid format")
            else:
                environ['X-username'] = xusername
                return self.app(environ, start_response)
        else:
            error = Error(401, 102, "Username header is missing")
        
        response = Response(response=error.toJSON(), status=error.httpCode, mimetype="application/json")
        response.headers["Content-Type"] = "application/json"
        return response(environ, start_response)
        