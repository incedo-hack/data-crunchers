from database import MysqlManager
from recommendation import TFIDF
from cache import Redis
import pandas as pd
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

    all_product = "recommendaion:all_product"
    for index, row in data.iterrows():
        print(f"Recommendation for {index}:  {row['entity_id']}: {row['description']}")
        recommendations = tfidf.recommendation(row['entity_id'], data, trained_data)
        # recommendations = dict((str(product_id), score) for product_id, score in recommendations.items())
        generated = {}
        for product_id, score in recommendations.items():
            index = data.entity_id[data.entity_id == product_id].index.tolist()[0]
            generated[str(product_id)] = {
                "score": score,
                "product_name": data.at[index, 'name'],
                "product_price":  0 if pd.isnull(data.at[index, 'price']) else data.at[index, 'price'],
                "product_description": data.at[index, 'description']
            }
        print(generated)
        resp = redis.addin_hash(connection, all_product, row['entity_id'], json.dumps(generated))
        print(resp)


if __name__ == '__main__':
    main()
