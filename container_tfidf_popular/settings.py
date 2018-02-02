mysql_host = '127.0.0.1'
mysql_port = 3306
mysql_username = 'root'
mysql_password = 'admin2008'
mysql_db = 'datacrunchers'

redis_host = '127.0.0.1'
redis_port = 6379
redis_db = 0

min_df = 0
max_df = .1
ngram_range = (1, 3)
stop_word = 'english'
lookup_id = 'product_id'
lookup_value = 'description'
no_of_recommendation = 15

product_query = f"select {lookup_id}, {lookup_value}, name from top_intrested_product where {lookup_value}\
                != 'NULL'"

