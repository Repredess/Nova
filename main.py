import os
from rich.console import Console


# /Users/pc/Desktop/Новая папка

class CheckPrefix:

    def __init__(self):
        self.console = Console()
        print()
        self.clean_console()
        self.get_path()
        self.clean_console(directory=self.folder_track)
        self.get_prefix()
        self.clean_console(directory=self.folder_track, prefix=self.prefix)
        self.filter_folder()

    def get_path(self):
        self.folder_track = self.validate_path(txt='Enter your tracking directory:')
        while not self.folder_track:
            self.console.print("[red]Path does not exist![red]", end=' ')
            self.folder_track = self.validate_path(txt='Put your tracking directory:')

    def get_prefix(self):
        self.prefix = input('Put your prefix:\n')

    def filter_folder(self):

        self.changed = 0
        self.massive = len(os.listdir(path=self.folder_track))
        defence = True

        for item in os.listdir(path=self.folder_track):

            if item.startswith(self.prefix) and os.path.isfile(os.path.join(self.folder_track, item)):
                if defence:
                    if item.lstrip(self.prefix).startswith('.'):
                        self.console.print('[red]WARNING!!! Your prefix may hide your files because they would start with "."[/red]')
                        answer = input("1.Continue\n2.Choose another prefix\n")

                        while answer not in ['1', '2']:
                            answer = input('Choose between 1 or 2: ', end='')
                        if answer == "1":
                            defence = False
                            try:
                                os.rename(os.path.join(self.folder_track, item),
                                          os.path.join(self.folder_track, item.lstrip(self.prefix).strip()))
                                self.changed += 1
                            except OSError:
                                print("[red]OSError. Check valid of your folder or prefix[/red]")
                            continue
                        else:
                            break

                try:
                    os.rename(os.path.join(self.folder_track, item),
                              os.path.join(self.folder_track, item.lstrip(self.prefix).strip()))
                    self.changed += 1
                except OSError:
                    self.console.print("[red]OSError. Check valid of your folder or prefix[/red]")

        self.report()
        _ = input("Press ENTER to continue...")

    def report(self):
        print(f"{self.changed}/{self.massive} files was changed successfully.")

    def clean_console(self, directory="", prefix=""):
        self.console.clear()
        if directory != "":
            self.console.print(f"Directory: [green]{directory}[/green]")
        if prefix != "":
            self.console.print(f"Prefix: [green]{prefix}[/green]")

    @classmethod
    def validate_path(cls, txt=''):
        path = input(f"{txt}\n").lstrip('\\')

        if os.path.exists(path):
            return path
        elif path == "":
            return ""
        else:
            return False


if __name__ == "__main__":
    while True:
        try:
            app = CheckPrefix()
        except KeyboardInterrupt:
            break

# pyinstaller -F --name="SortPrefix" main.py
