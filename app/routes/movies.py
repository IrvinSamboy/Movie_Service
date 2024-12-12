from fastapi import APIRouter, HTTPException
from typing import List
from app.models.moviesModels import Movies

fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order once again.',
        'genders': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]

movies = APIRouter()

@movies.get('/', response_model=List[Movies])
async def index(): 
        return fake_movie_db

@movies.post('/', status_code=201)
async def add_movie(payload: Movies):
        movie = payload.model_dump()
        fake_movie_db.append(movie)
        return {'id': len(fake_movie_db) -1}

@movies.put('/{id}')
async def update_movie(id: int, payload: Movies):
        movieForEddit = payload.model_dump()
        if id >= 0 and id <= len(fake_movie_db):
                fake_movie_db[-id] = movieForEddit
                return fake_movie_db[id]
        raise HTTPException(status_code=404, detail="Movie with given id not found")

@movies.delete('/{id}')
async def delete_movie(id: int):
        if id >= 0 and id <= len(fake_movie_db): 
                del fake_movie_db[-id]
                return {'message': "Movie delete from databse"}
        raise HTTPException(status_code=404, detail="Movie with given id not found")
