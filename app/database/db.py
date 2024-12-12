from sqlalchemy import create_engine, MetaData
from databases import Database
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
metadata = MetaData()

database = Database(DATABASE_URL)