from app.models.moviesModels import MovieIn, MovieOut, MovieUpdate
from app.database.db import database
from app.database.tables.movies import movies

async def add_movie(payload: MovieIn):
    query = movies.insert().values(**payload.model_dump())
    return await database.execute(query)

async def get_movie(id: int):
    query = movies.select(movies.c.id == id)
    return await database.fetch_one(query)

async def get_movies():
    query = movies.select()
    return await database.fetch_all(query)

async def update_movie(id: int, payload: MovieIn):
    query = movies.update().where(movies.c.id == id).values(**payload.model_dump())
    return await database.execute(query)

async def delete_movie(id: int):
    query = movies.delete().where(movies.c.id == id)
    return await database.execute(query)