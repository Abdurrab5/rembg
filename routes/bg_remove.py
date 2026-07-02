from fastapi import APIRouter, UploadFile, File, Request, HTTPException
from fastapi.responses import StreamingResponse
from services.bg_service import remove_bg
import io
import time

router = APIRouter()


@router.post("/bg-remove")
async def bg_remove(request: Request, file: UploadFile = File(...)):
    start = time.perf_counter()

    session = request.app.state.session

    output = await remove_bg(file, session)

    print(f"Processing took {time.perf_counter() - start:.2f} seconds")

    return StreamingResponse(
        io.BytesIO(output),
        media_type="image/png"
    )
 
