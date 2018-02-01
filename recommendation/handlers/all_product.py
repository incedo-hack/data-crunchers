from utils.cache import Redis
from utils.logs import Logger
logger = Logger().get_logger()


class AllProductRecommendation:
    def __init__(self):
        self.name = "recommendaion:all_product"

    def response(self, event, context, **resp):
        logger.debug(f'Event: {event}')
        resp_body = {'request_id': context.aws_request_id}
        product_id = event.get('queryStringParameters', {}).get('product_id')

        redis = Redis()
        connection = redis.connect()
        data = redis.getfrom_hash(connection, self.name, product_id)
        if data:
            status_code = 200
            resp_body.update({
                'message': data,
            })
        else:
            status_code = 401
            resp_body.update({
                'message': "{}"
            })

        resp['status_code'] = status_code
        resp['body'] = resp_body
        return resp

