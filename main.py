import json
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
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


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError):
    errors = exc.errors()
    extrafields = ''
    for error in errors:
        if not isinstance(error["loc"][1], int):
            extrafields += f'{error["loc"][1]}, '
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            # "detail": errors,
            "message": errors[0]["msg"],
            "extrafields": extrafields,
            "type": errors[0]["type"],
            # "body": exc.body,
            "success": False
        }),
    )


app.include_router(eess_router)
