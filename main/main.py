from fastapi import FastAPI
from main.routers.controllers import router as controllers
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    version="0.9 beta",
)

app.include_router(controllers)

app.mount("/static", StaticFiles(directory="static"), name="static")
