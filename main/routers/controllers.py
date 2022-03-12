from unittest import result
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from fastapi import APIRouter
from main.connection import get_connection
from main.query import (
    get_date_summary,
)


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
    conn = get_connection()
    cur = conn.cursor()
    result_data = get_date_summary(cur)

    labels = []
    values = []
    for item1, item2 in result_data:
        labels.append(item1)
        values.append(item2)

    cur.close()
    conn.close()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "values": values,
            "labels": labels,
        },
    )
