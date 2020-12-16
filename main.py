import fastapi
from fastapi import applications
from fastapi.templating import Jinja2Templates
import uvicorn
from starlette.requests import Request

from api import weather
from views import home

api = fastapi.FastAPI()


def configure():
    api.include_router(home.router)
    api.include_router(weather.router)


configure()

if __name__ == '__main__':
    uvicorn.run(api)
