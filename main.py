from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from pydantic import BaseModel
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from app.detection_service import DetectionService
from app.model import YoloV8
from typing import Annotated

app = FastAPI()
yolo = YoloV8().get_model()
detection_service = DetectionService(model=yolo)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/upload")
async def upload_video(video: UploadFile):
    file_name = video.filename
    file_path = f"static/{file_name}"
    # Open the file in binary mode
    with open(file_path, "wb") as buffer:
        # Read and write the file in chunks to handle large files
        while chunk := await video.read(1024):
            buffer.write(chunk)


    # Call your pothole detection function here and get the annotated video path
    annotated_video_path = detection_service.trigger(vid_path=file_path, name=file_name)

    return {"annotated_video": f"http://localhost:8000/{annotated_video_path}"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
