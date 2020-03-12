class PythiaError(Exception):
    def __init__(self, msg = "", status = 500):
        self.msg = msg
        self.status = status
        
class Forbidden(PythiaError):
    def __init__(self, msg = "Action not permitted", status = 403):
        super(Forbidden, self).__init__(msg, status)
 
class Unauthorized(PythiaError):
    def __init__(self, msg = "Unauthorized", status = 401):
        super(Unauthorized, self).__init__(msg, status)
        
class BadRequest(PythiaError):
    def __init__(self, msg = "Client error", status = 422):
        super().__init__(msg, status)
        
class ServerError(PythiaError):
    def __init__(self, msg = "Server error", status = 500):
        super(ServerError, self).__init__(msg, status)