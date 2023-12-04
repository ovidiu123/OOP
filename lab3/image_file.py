from file_base import FileBase

class ImageFile(FileBase):
    def __init__(self, filename="", image_size=""):
        super().__init__(filename)
        self.image_size = image_size

    def info(self):
        super().info()
        print(f"Image size: {self.image_size}")
