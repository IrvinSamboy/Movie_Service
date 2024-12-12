from fastapi import APIRouter
from typing import List
from app.models.moviesModels import MovieIn, MovieOut, MovieUpdate
from app.controllers.movies import index_movieC, index_moviesC, add_movieC, del_movieC, update_movieC

movies = APIRouter()

@movies.get('/', response_model=List[MovieOut])
async def index():
        await index_moviesC()

@movies.get('/{id}', response_model=MovieOut)
async def index (id: int):
        await index_movieC(id)

@movies.post('/', status_code=201)
async def add_movie(payload: MovieIn):
        await add_movieC(payload)

@movies.put('/{id}')
async def update_movie(id: int, payload: MovieUpdate):
        await update_movieC(id, payload)

@movies.delete('/{id}')
async def del_movie(id: int):
        await del_movieC(id)