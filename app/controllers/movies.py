from fastapi import HTTPException
from app.database.managers.movies import get_movie, get_movies, put_movie, delete_movie, insert_movie
from app.models.moviesModels import MovieIn, MovieUpdate


async def index_moviesC():
        movies = await get_movies()
        if len(movies) == 0:
                raise HTTPException(status_code=404, detail='There are no movies in the system') 
        return movies
    
async def index_movieC(id: int):
        if id < 0: 
                raise HTTPException(status_code=400, detail='Invalid id')
        movie = await get_movie(id)
        if not movie: 
                raise HTTPException(status_code=404, detail='Not found')
        return movie
    
async def add_movieC(payload: MovieIn):
        movie_id = await insert_movie(payload)
        return {'id': movie_id, **payload.model_dump()}
    
async def update_movieC(id: int, payload: MovieUpdate):
        if id < 0: 
                raise HTTPException(status_code=400, detail='Invalid id')
        movie = await get_movie(id)
        if not movie: 
                raise HTTPException(status_code=404, detail='Not found')
        
        update_data = payload.model_dump(exclude_unset=True)
        movie_in_db = MovieUpdate(**movie)
        updated_movie = movie_in_db.model_copy(update=update_data)
        await put_movie(id, updated_movie)
        return {'message': "Movie updated"}

async def del_movieC(id: int):
        if id < 0: 
                raise HTTPException(status_code=400, detail='Invalid id')
        movie = await get_movie(id)
        if not movie: 
                raise HTTPException(status_code=404, detail='Not found')
        await delete_movie(id)
        return  {'message': "Movie deleted"}