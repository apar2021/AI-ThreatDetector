from fastapi import FastAPI
from pydantic import BaseModel
import motor.motor_asyncio

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient()

@app.get("/")
def root():
    # add user interface here and then move forward
    return {"message": "Hello World"}
@app.post("/traffic")
async def traffic():
    return {"Message":"Traffic Data Inserted Succesfully"}
@app.post("/analyze")
async def analyze():
    return {"Message":"Analyze Data Inserted Succesfully"}
@app.get("/traffic")
def get_traffic():
    return {"message": "Hello World"}
