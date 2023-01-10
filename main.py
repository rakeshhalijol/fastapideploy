from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
import db
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello():
    return {"data":"Welcome to student management api"}

@app.post("/student")
async def create_student(data:models.Student):
    print(data)
    inserted_id = db.create(data)
    return {"Status":"Successful","inserted_id":str(inserted_id)}

@app.get("/all")
async def get_students():
    responses = db.get_all()
    return {"status":"Success","response":responses}