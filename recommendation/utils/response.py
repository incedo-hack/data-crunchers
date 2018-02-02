class Response:
    def __init__(self, body=None, headers=None, status_code=200):
        self.body = body
        if headers is None:
            headers = {}
        self.headers = headers
        self.status_code = status_code

    def to_dict(self):
        response = {
            'headers': self.headers,
            'statusCode': self.status_code,
            'body': self.body
        }
        return response
