from flask import Flask, jsonify
from utils.logs import Logger
from handlers.all_product import AllProductRecommendation
from handlers.popular_product import PopularProductRecommendation
import json

logger = Logger().get_logger()
app = Flask(__name__)


class Context:
    aws_request_id = 1


@app.route('/all/product/recommendation/<int:product_id>', methods=['GET'])
def recommendation_on_all_products(product_id):
    event = {'queryStringParameters': {"product_id": product_id}}
    resp = AllProductRecommendation().response(event, Context)
    print(resp)
    message = resp.get('body', {}).get('message')
    message = json.loads(message)
    return jsonify({'content': message})


@app.route('/popular/product/recommendation/<int:product_id>', methods=['GET'])
def recommendation_on_popular_products(product_id):
    event = {'queryStringParameters': {"product_id": product_id}}
    resp = PopularProductRecommendation().response(event, Context)
    print(resp)
    message = resp.get('body', {}).get('message')
    message = json.loads(message)
    return jsonify({'content': message})


if __name__ == '__main__':
    app.run(debug=True)
