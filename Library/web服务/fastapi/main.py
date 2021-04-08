"""
@Author: Jonescyna@gmail.com
@Created: 2021/3/9
"""
from fastapi import FastAPI
from routers import router

app = FastAPI()

app.include_router(
    router=router,
    prefix='/api'
)
