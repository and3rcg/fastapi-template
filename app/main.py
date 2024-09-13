from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import users
from .database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # you can put setup and teardown code here before and after the yield, respectively
    # documentation: https://fastapi.tiangolo.com/advanced/events/#lifespan-function
    print(app.description)
    init_db()
    yield
    print("Using lifespan to shut down the server...")


app = FastAPI(lifespan=lifespan, description="FastAPI template by Anderson Caminha")

# setting up CORS based on https://fastapi.tiangolo.com/tutorial/cors/

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
# add more routers here...
