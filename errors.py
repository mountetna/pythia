class BaseError(Exception):
    def __init__(self, msg = "", status = 500):
        self.msg = msg
        self.status = status
        
class Forbidden(BaseError):
    def __init__(self, msg = "Action not permitted", status = 403):
        super(Forbidden, self).__init__(msg, status)
 
class Unauthorized(BaseError):
    def __init__(self, msg = "Unauthorized", status = 401):
        super(Unauthorized, self).__init__(msg, status)
        
class BadRequest(BaseError):
    def __init__(self, msg = "Client error", status = 422):
        super(BadRequest, self).__init__(msg, status)
        
class ServerError(BaseError):
    def __init__(self, msg = "Server error", status = 500):
        super(ServerError, self).__init__(msg, status)