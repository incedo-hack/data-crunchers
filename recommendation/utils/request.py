import base64
import json


class Request:
    @staticmethod
    def body_to_dict(event):
        is_base64_encoded = event.get('isBase64Encoded', False)
        body = event.get('body')
        body = base64.b64decode(body) if is_base64_encoded else body
        body = json.loads(body) if isinstance(body, str) else body
        return body
