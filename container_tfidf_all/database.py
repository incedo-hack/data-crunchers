from sqlalchemy import create_engine
from settings import *
import pandas as pd


class MysqlManager:
    def __init__(self):
        self.username = mysql_username
        self.password = mysql_password
        self.host = mysql_host
        self.port = mysql_port
        self.database = mysql_db
        self.query = product_query

    def _connection_string(self):
        return f"mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

    def engine(self):
        return create_engine(self._connection_string())

    def export(self, engine):
        return pd.read_sql_query(self.query, engine)