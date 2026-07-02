from contextlib import asynccontextmanager

from fastapi import FastAPI
from rembg import new_session

from routes.bg_remove import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the model once
    app.state.session = new_session("birefnet-general")

    yield

    # Cleanup (optional)
    app.state.session = None


app = FastAPI(
    title="BG Remove API",
    version="1.0",
    lifespan=lifespan,
)

app.include_router(router)


@app.get("/", tags=["Health"])
async def health():
    return {
        "status": "running",
        "model": "birefnet-general"
    }   
