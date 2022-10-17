#uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "hello, my fastapi program, enjoying it and running it again. What a fun!!!" 

@app.get("/tournaments")
def list_tournaments():
    return [1,2,3]

@app.get("/stats")
def stats():
    return {
            "mvp" : "Jordan",
            "points_scored" : 9001,
    }
