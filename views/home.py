import fastapi
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.requests import Request

templates = Jinja2Templates('templates')

router = APIRouter()


@router.get('/', include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request
    })
