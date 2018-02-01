from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from settings import *


class TFIDF:
    def __init__(self):
        self.min_df = min_df
        self.max_df = max_df
        self.stop_word = stop_word
        self.ngram_range = ngram_range
        self.lookup_id = lookup_id
        self.lookup_value = lookup_value
        self.no_of_recommendation = no_of_recommendation

    def classifier(self):
        return TfidfVectorizer(analyzer='word', ngram_range=self.ngram_range, min_df=self.min_df, max_df=self.max_df,  stop_words=self.stop_word)

    def training(self, clfs, data):
        matrix = clfs.fit_transform(data[self.lookup_value])
        data_matrix = cosine_similarity(matrix, matrix)
        return data_matrix

    def recommendation(self, product_id, data, data_matrix):
        idx = data.entity_id[data.entity_id == product_id].index.tolist()[0]
        similar_indices = data_matrix[idx].argsort()[:(-self.no_of_recommendation - 2):-1]
        recommendations = [(data_matrix[idx][index], data[self.lookup_id][index]) for index in similar_indices]
        recommendations = recommendations[1:self.no_of_recommendation + 1]
        recommendations = list(map(lambda recommendation: tuple(reversed(recommendation)), recommendations))
        recommendations = dict(recommendations)
        return recommendations