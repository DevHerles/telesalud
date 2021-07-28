from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.eess import router as eess_router

from api.settings import api_settings as settings

app = FastAPI(title=settings.title)

origins = [
    'https://localhost:3000',
    'http://localhost:11501',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return "(C) MINSA - 2021"


app.include_router(eess_router)
