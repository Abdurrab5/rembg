from fastapi import FastAPI
from routes.bg_remove import router

app = FastAPI(
    title="BG Remove API",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "BG API running"}