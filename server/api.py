import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

load_dotenv()

from server.middlewares import add_process_time_header
from server.routes import router

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.getenv('DATABASE_URL'))
app.add_middleware(BaseHTTPMiddleware, dispatch=add_process_time_header)
app.include_router(router)
