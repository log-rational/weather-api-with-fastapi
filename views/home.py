import fastapi
from fastapi import templating
from fastapi.templating import JinJinja2Templates
import uvicorn

template = JinJinja2Templates()

api = fastapi.FastAPI()


@api.get('/')
def index():
    return {
        "message": "Hello World!",
        "status": "OK"
    }


uvicorn.run(api)
