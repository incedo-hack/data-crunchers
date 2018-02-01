from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import create_engine
import pandas as pd


class TFIDF:
    def __init__(self):
        self.stop_word = 'english'
        self.min_df = 0
        self.ngram_range = (1, 3)
        self.lookup_attr = 'rating_code'
        self.uuid = 'uuid'
        self.no_of_recommendation = 20

    def classifier(self):
        return TfidfVectorizer(analyzer='word', ngram_range=self.ngram_range, min_df=self.min_df, stop_words=self.stop_word)

    def training(self, clfs, data):
        matrix = clfs.fit_transform(data[self.lookup_attr])
        data_matrix = cosine_similarity(matrix, matrix)
        return data_matrix

    def recommendation(self, product_id, data, data_matrix):
        pass


# Get product data from mysql
engine = create_engine('mysql+pymysql://root:admin2008@127.0.0.1:3306/datacrunchers',
                       echo=False)
query = "select * from rating"
data = pd.read_sql_query(query, engine)
print(data)
print(data.shape)

tfidf = TFIDF()
# Run the classifier
classifier = tfidf.classifier()

# Train the data
data_matrix = tfidf.training(classifier, data)
print(data_matrix)
# Generate the recommendation
