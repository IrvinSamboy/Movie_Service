from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, ARRAY
from app.database.db import metadata

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('gender', ARRAY(String)),
    Column('casts', ARRAY(String))
)

