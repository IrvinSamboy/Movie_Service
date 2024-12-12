from sqlalchemy import create_engine, MetaData
from databases import Database
import os

DATABASE_URL = 'postgresql://postgres:zanahoria12@localhost/movie_db'
engine = create_engine(DATABASE_URL)
metadata = MetaData()

database = Database(DATABASE_URL)