from rembg import remove
from fastapi.concurrency import run_in_threadpool

async def remove_bg(file):
    input_image = await file.read()
    output_image = await run_in_threadpool(remove, input_image)
    return output_image