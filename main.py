from fastapi import FastAPI
import model
from db_config import engine
import routes

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def Home():
    return "Welcome to the club buddy"

app.include_router(routes.router, prefix="/user", tags=["user"])
