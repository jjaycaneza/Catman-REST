#!C:\xampp\htdocs\python-api\Scriptspython.exe
# print("Content-Type: application/json\n")
# print ("Hello Python Web Browser!! This is cool!!")
import requests

import models
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import json


class User(BaseModel):
    username:str
    password:str

app = FastAPI()

@app.get("/countsheet")
def get_countsheet():
    return models.get_countSheet()
@app.post("/users/signin")
def signin(user:User):
    return models.signin(user.username,user.password)
@app.post("/users/signup")
def login(user:User):
    return models.login(user.username,user.password)

@app.put("/users/{item_id}")
def update_user(item_id:int,user:User):
    return "update"
@app.delete("/users/{item_id}")
def delete_user(item_id:int):
    return "deleting"