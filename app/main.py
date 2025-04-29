from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from app.database import engine, Base
from app.router import users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)

mcp = FastApiMCP(app)

mcp.mount()