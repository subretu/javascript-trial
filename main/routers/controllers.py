from starlette.templating import Jinja2Templates
from starlette.requests import Request
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from main.connection import get_connection
from main.query import (
    get_date_summary,
    get_time_summary,
    get_date_stack_summary,
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
    result_data_time = get_time_summary(cur)
    result_data_day = get_date_summary(cur)

    labels1, labels2, values1, values2, values3 = [], [], [], [], []
    for item1, item2 in result_data_time:
        labels1.append(item1)
        values1.append(item2)

    for item1, item2 in result_data_day:
        labels2.append(item1)
        values2.append(item2)

    for item1, item2 in get_date_stack_summary:
        values3.append(item2)

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
            "values3": values3,
        },
    )


@router.get("/test")
def day(request: Request):
    conn = get_connection()
    cur = conn.cursor()
    result_data_day = get_date_summary(cur)

    labels1, values1 = [], []

    for item1, item2 in result_data_day:
        labels1.append(item1.strftime("%Y-%m-%d"))
        values1.append(item2)

    cur.close()
    conn.close()

    return JSONResponse(
        content={
            "label": labels1,
            "data": values1,
        }
    )


from starlette.templating import Jinja2Templates
from starlette.requests import Request
from fastapi import APIRouter
from fastapi.responses import JSONResponse
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
    result_data_time = get_time_summary(cur)
    result_data_day = get_date_summary(cur)

    labels1, labels2, values1, values2 = [], [], [], []
    for item1, item2 in result_data_time:
        labels1.append(item1)
        values1.append(item2)

    for item1, item2 in result_data_day:
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


@router.get("/day")
def get_day(request: Request):
    conn = get_connection()
    cur = conn.cursor()
    result_data_day = get_date_summary(cur)

    labels1, values1 = [], []

    for item1, item2 in result_data_day:
        labels1.append(item1.strftime("%Y-%m-%d"))
        values1.append(item2)

    cur.close()
    conn.close()

    return JSONResponse(
        content={
            "label": labels1,
            "data": values1,
        }
    )


@router.get("/time")
def get_time(request: Request):
    conn = get_connection()
    cur = conn.cursor()
    result_data_time = get_time_summary(cur)

    labels1, values1 = [], []

    for item1, item2 in result_data_time:
        labels1.append(item1.strftime("%Y-%m-%d %H:%M:%S"))
        values1.append(item2)

    cur.close()
    conn.close()

    return JSONResponse(
        content={
            "label": labels1,
            "data": values1,
        }
    )
