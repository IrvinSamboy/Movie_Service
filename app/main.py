from fastapi import FastAPI
from app.routes.movies import movies

app = FastAPI()

app.include_router(movies)

