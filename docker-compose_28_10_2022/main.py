import sqlite3

from fastapi import FastAPI
from redis import Redis

app = FastAPI(docs_url="/")
r = Redis(host="cache")


@app.get("/home")
def home():
    return "Hello World"


@app.get("/keys")
def get_keys():
    return r.keys()


@app.post("/add")
def add_data(key, value):
    r.set(key, value)
    return f"set {key}:{value}"


@app.get("/get")
def get_key(key):
    value = r.get(key)
    return {key: value}


@app.get("/actors")
def get_actors():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        results = cursor.execute("""SELECT * FROM actor;""")
        actors = results.fetchall()
        return actors
