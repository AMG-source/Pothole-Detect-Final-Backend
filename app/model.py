from ultralytics import YOLO
import os

class YoloV8:
    def __init__(self) -> None:
        self.__model_path = "data/model/best.pt"
        self.__model = YOLO(self.__model_path)

    def get_model(self):
        return self.__model