import os

from datetime import datetime
from os.path import splitext
from PIL import Image
from file_base import FileBase
from image_file import ImageFile
from text_file import TextFile
from program_file import ProgramFile

class FolderMonitor:
    def __init__(self):
        self.snapshot_time = None
        self.files = {}

    def commit(self):
        self.snapshot_time = datetime.now()
        for file in self.files.values():
            file.update_snapshot()

    def add_file(self, filename):
        _, extension = splitext(filename)
        extension = extension.lower()  # Convert extension to lowercase
        if extension == ".txt":
            self.files[filename] = TextFile(filename)
        elif extension in (".png", ".jpg"):
            image_size = self.get_image_size(filename)
            self.files[filename] = ImageFile(filename, image_size)
        elif extension in (".py", ".java"):
            self.files[filename] = ProgramFile(filename)
        else:
            self.files[filename] = FileBase(filename)
        self.files[filename].created_time = datetime.now()

    def get_image_size(self, filename):
        try:
            with Image.open(filename) as img:
                width, height = img.size
                return f"{width}x{height}"
        except Exception as e:
            print(f"Error getting image size: {e}")
            return ""

    def status(self):
        if self.snapshot_time is None:
            print("No snapshot taken yet.")
            return

        print(f"Snapshot taken at: {self.snapshot_time}")
        for filename, file in self.files.items():
            # Check if the file still exists
            file_exists = os.path.exists(filename)

            if not file_exists:
                status = "Changed (Deleted)"
            else:
                status = "No Change" if file.updated_time is None or (
                        file.created_time <= file.updated_time <= self.snapshot_time) else "Changed"

            print(f"{filename} - {status}")

    def info(self, filename):
        file = self.files.get(filename)
        if file:
            file.info()
        else:
            print(f"File '{filename}' not found in the monitored folder.")
