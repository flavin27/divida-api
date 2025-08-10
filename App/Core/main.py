from fastapi import FastAPI, Depends
from App.Http.Routes import cda

app = FastAPI()

app.include_router(cda.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

