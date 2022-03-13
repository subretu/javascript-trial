from starlette.templating import Jinja2Templates
from starlette.requests import Request
from fastapi import APIRouter
from main.connection import get_connection
from main.query import (
    get_date_summary,
    get_time_summary,
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
    result_data1 = get_time_summary(cur)
    result_data2 = get_date_summary(cur)

    labels1 = []
    values1 = []
    labels2 = []
    values2 = []
    for item1, item2 in result_data1:
        labels1.append(item1)
        values1.append(item2)

    for item1, item2 in result_data2:
        labels2.append(item1)
        values2.append(item2)

    cur.close()
    conn.close()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "values1": values1,
            "labels1": labels1,
            "values2": values2,
            "labels2": labels2,
        },
    )
