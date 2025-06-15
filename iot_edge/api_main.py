from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/api/validate", response_class=PlainTextResponse)
def validate_user(user: str = Query(...)):
    autorizados = ["alejandro", "carmen", "juan"]
    if user.lower() in autorizados:
        return "true"
    return "false"
