# make a .post entry.
from fastapi import FastAPI, HTTPException

# app = FastAPI(doc_url="/")
app = FastAPI(doc_url="/prerana")
@app.get("/login/{password}")

def login(password):
    if password == "superman":
        return "login succsessful"
    else:
        raise HTTPException(status_code = 403, detail="incorrect password")

@app.post("/test")
def testingpost(username):
    return f"your username is {username}"
