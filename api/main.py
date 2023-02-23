from fastapi import FastAPI
import model
from db_config import engine
import routes
import json
model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def Home():
    return "Welcome to the club buddy"

# use this to get openapi.json file
# @app.on_event("startup")
# def save_openapi_json():
#     openapi_data = app.openapi()
#     with open("openapi.json", "w") as file:
#         json.dump(openapi_data, file)


app.include_router(routes.router, prefix="/user", tags=["user"])
