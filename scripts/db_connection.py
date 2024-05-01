from sqlalchemy import create_engine
import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os

class Connection:
    def __init__(self):
        self.engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
        self.conn = self.engine.connect()

    def df_to_sql(self, df, tablename):
        "convert dataframe to sql data"
        df.to_sql(tablename,con = self.engine)
    
    def selectall(self):
        print (self.engine.table_names())