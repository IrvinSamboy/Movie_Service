from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes.movies import movies
from app.database.db import engine, metadata, database

metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI): 
    
    await database.connect()
    
    yield 
    
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(movies)

