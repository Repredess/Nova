import os
from rich.console import Console
from rich.text import Text
from rich.progress import track
from time import sleep


# /Users/pc/Desktop/Новая папка

class CheckPrefix:

    def __init__(self):
        self.console = Console()
        self.get_path()
        self.clean_console(txt=f'Directory: {self.folder_track}')
        self.get_prefix()
        self.clean_console(txt=f'Directory: {self.folder_track}\nPrefix: {self.prefix}')
        self.filter_folder()

    def get_path(self):
        self.folder_track = self.validate_path(txt='Enter your tracking directory:')
        while not self.folder_track:
            self.folder_track = self.validate_path(txt='Invalid path. Put your tracking directory:', error=True)

    def get_prefix(self):
        self.prefix = input('Put your prefix:\n')

    def filter_folder(self):
        for item in os.listdir(path=self.folder_track):
            # print(item.lstrip(self.prefix).strip())
            if item.startswith(self.prefix):
                # if item.lstrip(self.prefix).strip().startswith('.'):
                #     self.colored_messages(
                #         'WARNING!!! Your prefix may hide your files because they would starts with "."', color='red')
                #     question = input("1.Continue\n2.Choose another prefix")
                #     while question not in ['1', '2']:
                #         self.colored_messages(
                #             'Choose between 1 or 2', color='red')
                #     if question == "1":
                #         continue
                #     if question == "2":
                #         break
                os.rename(os.path.join(self.folder_track, item),
                          os.path.join(self.folder_track, item.lstrip(self.prefix).strip()))

    def clean_console(self, txt=''):
        self.console.clear()
        print(txt)

    @classmethod
    def validate_path(cls, txt='', error=False):
        path = input(f"{txt}\n").lstrip('\\')

        if os.path.exists(path):
            return path
        elif path == "":
            return ""
        else:
            return False

    # def colored_messages(txt='', color='black'):
    #     text = Text(txt).styled(color)
    #     console.print(text)


if __name__ == "__main__":
    while True:
        app = CheckPrefix()


# pyinstaller -F --name="SortPrefix" main.py
