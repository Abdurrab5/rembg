from fastapi import HTTPException
from fastapi.concurrency import run_in_threadpool
from rembg import remove
import logging

logger = logging.getLogger(__name__)


def _remove_sync(image_bytes: bytes, session):
    return remove(image_bytes, session=session)


async def remove_bg(file, session):
    image_bytes = await file.read()

    if not image_bytes:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    try:
        return await run_in_threadpool(
            _remove_sync,
            image_bytes,
            session
        )
    except Exception:
        logger.exception("Background removal failed.")
        raise HTTPException(
            status_code=500,
            detail="Failed to remove background."
        ) 
