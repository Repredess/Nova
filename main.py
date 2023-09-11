import os
from rich.console import Console
from rich.text import Text
from rich.progress import track
from time import sleep


# /Users/pc/Desktop/Новая папка

class CheckPrefix:

    def __init__(self):
        self.console = Console()
        self.clean_console()
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

        self.changed = 0
        self.hidden = 0
        self.massive = len(os.listdir(path=self.folder_track))

        for item in os.listdir(path=self.folder_track):
            # print(item)
            # if item.startswith('.'):
            #     self.hidden += 1
            #     print(item)
            #     print(self.hidden)

            if item.startswith(self.prefix) and os.path.isfile(os.path.join(self.folder_track, item)):
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
                try:
                    os.rename(os.path.join(self.folder_track, item),
                              os.path.join(self.folder_track, item.lstrip(self.prefix).strip()))
                    self.changed += 1
                except OSError:
                    print("OSError. Check valid of your folder or prefix")

        self.report()
        _ = input("Press ENTER to continue...")

    def report(self):
        print(f"{self.changed}/{self.massive} files was changed successfully.", end=' ')
        if self.hidden > 0:
            print(f"There are {self.hidden} hidden files here.")
        else:
            print()

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
        try:
            app = CheckPrefix()
        except KeyboardInterrupt:
            break

# pyinstaller -F --name="SortPrefix" main.py
