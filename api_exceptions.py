class BadRequest(Exception):
    status_code = 400

    def __init__(self, message, inner):
        Exception.__init__(self)
        self.message = message
        self.inner = inner
        
    def to_dict(self):
        d = dict()
        d["message"] = self.message
        d["inner"] = self.inner
        return d