from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello World !"}

@app.get("/name")
def name():
    return {"message":"My name is Sakshi Shimpi\n I am a AI ML Engineer"}