from database import MysqlManager
from recommendation import TFIDF
from cache import Redis
import json


def main():
    mysql = MysqlManager()
    engine = mysql.engine()
    data = mysql.export(engine)

    tfidf = TFIDF()
    classifier = tfidf.classifier()
    trained_data = tfidf.training(classifier, data)

    redis = Redis()
    connection = redis.connect()

    index_name = "recommendaion:popular_product"
    for index, row in data.iterrows():
        print(f"Recommendation for {index}:  {row['product_id']}: {row['description']}")
        recommendations = tfidf.recommendation(row['product_id'], data, trained_data)
        generated = {}
        for product_id, score in recommendations.items():
            index = data.product_id[data.product_id == product_id].index.tolist()[0]
            generated[str(product_id)] = {
                "score": score,
                "product_name": data.at[index, 'name'],
                "product_description": data.at[index, 'description']
            }
        print(generated)
        resp = redis.addin_hash(connection, index_name, row['product_id'], json.dumps(generated))
        print(resp)


if __name__ == '__main__':
    main()
