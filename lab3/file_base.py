from datetime import datetime

class FileBase:
    def __init__(self, filename=""):
        self.filename = filename
        self.created_time = datetime.now()
        self.updated_time = None

    def update_snapshot(self):
        self.updated_time = datetime.now()

    def info(self):
        print(f"{self.filename}: Created at {self.created_time}, Last updated at {self.updated_time}")
