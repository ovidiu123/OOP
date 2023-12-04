import datetime
class File:
    def __init__(self, filename, extension):
        self.filename = filename
        self.extension = extension
        self.created_time = datetime.datetime.now()
        self.updated_time = self.created_time
        self.content = ""

    def update_content(self, new_content):
        self.content = new_content
        self.updated_time = datetime.datetime.now()

    def get_info(self):
        return f"{self.filename} - {self.extension}"

    def get_status(self, snapshot_time):
        if self.updated_time <= snapshot_time:
            return "No change"
        else:
            return "Changed"


class TextFile(File):
    def __init__(self, filename):
        super().__init__(filename, "txt")
        self.line_count = 0
        self.word_count = 0
        self.character_count = 0

    def analyze_content(self):
        if self.content:
            self.line_count = len(self.content.split('\n'))
            self.word_count = len(self.content.split())
            self.character_count = len(self.content)

    def get_info(self):
        return f"{super().get_info()} - Lines: {self.line_count}, Words: {self.word_count}, Characters: {self.character_count}"


class ImageFile(File):
    def __init__(self, filename):
        super().__init__(filename, "png")
        self.image_size = "Unknown"

    def analyze_content(self):
        # Assuming image content analysis here
        self.image_size = "1024x860"  # Replace with actual analysis

    def get_info(self):
        return f"{super().get_info()} - Image Size: {self.image_size}"


class ProgramFile(File):
    def __init__(self, filename):
        super().__init__(filename, "py")
        self.line_count = 0
        self.class_count = 0
        self.method_count = 0

    def analyze_content(self):
        # Assuming program content analysis here
        self.line_count = 100  # Replace with actual analysis
        self.class_count = 5  # Replace with actual analysis
        self.method_count = 20  # Replace with actual analysis

    def get_info(self):
        return f"{super().get_info()} - Lines: {self.line_count}, Classes: {self.class_count}, Methods: {self.method_count}"


class Snapshot:
    def __init__(self):
        self.time = datetime.datetime.now()

    def update_snapshot(self):
        self.time = datetime.datetime.now()

import os
import datetime
class File:
    def __init__(self, filename, extension):
        self.filename = filename
        self.extension = extension
        self.created_time = datetime.datetime.now()
        self.updated_time = self.created_time
        self.content = ""

    def update_content(self, new_content):
        self.content = new_content
        self.updated_time = datetime.datetime.now()

    def get_info(self):
        return f"{self.filename} - {self.extension}"

    def get_status(self, snapshot_time):
        if self.updated_time <= snapshot_time:
            return "No change"
        else:
            return "Changed"


class TextFile(File):
    def __init__(self, filename):
        super().__init__(filename, "txt")
        self.line_count = 0
        self.word_count = 0
        self.character_count = 0

    def analyze_content(self):
        if self.content:
            self.line_count = len(self.content.split('\n'))
            self.word_count = len(self.content.split())
            self.character_count = len(self.content)

    def get_info(self):
        return f"{super().get_info()} - Lines: {self.line_count}, Words: {self.word_count}, Characters: {self.character_count}"


class ImageFile(File):
    def __init__(self, filename):
        super().__init__(filename, "png")
        self.image_size = "Unknown"

    def analyze_content(self):
        # Assuming image content analysis here
        self.image_size = "1024x860"  # Replace with actual analysis

    def get_info(self):
        return f"{super().get_info()} - Image Size: {self.image_size}"


class ProgramFile(File):
    def __init__(self, filename):
        super().__init__(filename, "py")
        self.line_count = 0
        self.class_count = 0
        self.method_count = 0

    def analyze_content(self):
        # Assuming program content analysis here
        self.line_count = 100  # Replace with actual analysis
        self.class_count = 5  # Replace with actual analysis
        self.method_count = 20  # Replace with actual analysis

    def get_info(self):
        return f"{super().get_info()} - Lines: {self.line_count}, Classes: {self.class_count}, Methods: {self.method_count}"


class Snapshot:
    def __init__(self):
        self.time = datetime.datetime.now()

    def update_snapshot(self):
        self.time = datetime.datetime.now()


class FileManager:
    def __init__(self):
        self.snapshot = Snapshot()
        self.files = []

    def commit(self):
        self.snapshot.update_snapshot()
        for file in self.files:
            file.update_content("")  # Reset content for all files

    def add_file(self, file):
        self.files.append(file)

    def get_file_by_name(self, filename):
        for file in self.files:
            if file.filename == filename:
                return file
        return None

    def info(self, filename="all"):
        if filename == "all":
            for file in self.files:
                print(file.get_info())
        else:
            file = self.get_file_by_name(filename)
            if file:
                print(file.get_info())
                if file.extension == "txt":
                    file.analyze_content()
                    print(f"Line Count: {file.line_count}, Word Count: {file.word_count}, Character Count: {file.character_count}")
                elif file.extension == "png":
                    file.analyze_content()
                    print(f"Image Size: {file.image_size}")
                elif file.extension == "py":
                    file.analyze_content()
                    print(f"Line Count: {file.line_count}, Class Count: {file.class_count}, Method Count: {file.method_count}")
                else:
                    print("Content analysis not available for this file type.")

    def status(self):
        print(f"Created Snapshot at: {self.snapshot.time}")
        for file in self.files:
            print(f"{file.get_info()} - {file.get_status(self.snapshot.time)}")

# Example usage:
file_manager = FileManager()
file_manager.add_file(TextFile("test.txt"))
file_manager.add_file(ImageFile("image.png"))
file_manager.add_file(ProgramFile("python_script.py"))

file_manager.commit()
file_manager.status()

# Your folder path
folder_path = "folder"

def main():
    file_manager = FileManager()






if __name__ == "__main__":
    main()



def main():
    file_manager = FileManager()


if __name__ == "__main__":
    main()
