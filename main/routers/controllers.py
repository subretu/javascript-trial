from starlette.templating import Jinja2Templates
from starlette.requests import Request
from fastapi import APIRouter


router = APIRouter()

# テンプレート関連の設定 (jinja2)
templates = Jinja2Templates(directory="templates")
# Jinja2.Environment : filterやglobalの設定用
jinja_env = templates.env


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/barchart")
def barchart(request: Request):
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "values": values,
            "labels": labels,
        },
    )
