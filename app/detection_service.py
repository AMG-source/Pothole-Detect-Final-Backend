import os
from app.utils.utility_functions import avi_to_mp4

class DetectionService:
    def __init__(self, model) -> None:
        self.model = model
    
    def trigger(self, vid_path: str, name: str):
        results = self.model.predict(source=vid_path, project="static", name="detections", save=True)
        save_dir = results[0].save_dir.replace('\\', '/')
        files = os.listdir(save_dir)
        files = [file for file in files if os.path.isfile(os.path.join(save_dir, file))]
        most_recent_file = max(files, key=lambda file: os.path.getmtime(os.path.join(save_dir, file)))
        path_to_avi = f"{save_dir}/{most_recent_file}"
        path_to_mp4 = f"{save_dir}/{most_recent_file[:-3]}mp4"
        avi_to_mp4(input_file=path_to_avi, output_file=path_to_mp4)
        os.remove(path_to_avi)
        return path_to_mp4