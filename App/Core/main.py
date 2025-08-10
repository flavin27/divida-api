from fastapi import FastAPI, Depends
from App.Http.Routes import cda, resumo

app = FastAPI()

app.include_router(cda.router)
app.include_router(resumo.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

