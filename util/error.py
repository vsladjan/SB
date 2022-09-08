import json

class Error:

    def __init__(self):
        self.httpCode = 404
        self.errorCode = 0
        self.message = "Requested location doesn't exists."

    def __init__(self, httpCode, errorCode, message):
        self.httpCode = httpCode
        self.errorCode = errorCode
        self.message = message

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        