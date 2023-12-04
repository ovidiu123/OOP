from file_base import FileBase

class TextFile(FileBase):
    def __init__(self, filename="", line_count=0, word_count=0, char_count=0):
        super().__init__(filename)
        self.line_count = line_count
        self.word_count = word_count
        self.char_count = char_count

    def info(self):
        super().info()
        print(f"Line count: {self.line_count}, Word count: {self.word_count}, Character count: {self.char_count}")
