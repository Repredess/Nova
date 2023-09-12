import os
from rich.console import Console


# /Users/pc/Desktop/Новая папка

class CheckPrefix:

    def __init__(self, recursion):
        self.defence = True
        self.changed = 0
        self.hiden = 0
        self.console = Console()
        self.clean_console()
        self.recursion = recursion
        self.start_app()

    def start_app(self):
        if self.recursion == "2":
            self.get_path()
            self.clean_console(directory=self.folder_track)
            self.get_prefix()
            self.clean_console(directory=self.folder_track, prefix=self.prefix)
            self.filter_folder()
        else:
            self.get_path()
            self.clean_console(directory=self.folder_track)
            self.get_prefix()
            self.clean_console(directory=self.folder_track, prefix=self.prefix)
            self.recursive_nest(path=self.folder_track)
            self.report()

    def recursive_nest(self, path=""):

        for item in os.listdir(path=path):

            if os.path.isfile(os.path.join(path, item)) and item.startswith(self.prefix):
                if item.lstrip(self.prefix).startswith('.'):
                    self.hiden += 1
                self.file_rename(path, item)

            elif os.path.isdir(os.path.join(path, item)):
                self.recursive_nest(path=os.path.join(path, item))
                if item.startswith(self.prefix):
                    if item.lstrip(self.prefix).startswith('.'):
                        self.hiden += 1
                    self.file_rename(path, item)
                else:
                    continue

    def file_rename(self, path, item):
        try:
            os.rename(os.path.join(path, item), os.path.join(path, item.lstrip(self.prefix)))
            self.changed += 1
        except OSError:
            self.console.print("[red]OSError. Check valid of your folder or prefix[/red]")

    def get_path(self):
        self.folder_track = self.validate_path(txt='Enter your tracking directory:')
        while not self.folder_track:
            self.console.print("[red]Path does not exist![red]", end=' ')
            self.folder_track = self.validate_path(txt='Put your tracking directory:')

    def get_prefix(self):
        self.prefix = input('Put your prefix:\n')

    def filter_folder(self):

        for item in os.listdir(path=self.folder_track):

            if item.startswith(self.prefix) and os.path.isfile(os.path.join(self.folder_track, item)):

                if self.defence:
                    if item.lstrip(self.prefix).startswith('.'):
                        self.console.print(
                            '[red]WARNING!!! Your prefix may hide your files because they would start with "."[/red]')
                        answer = input("1.Continue\n2.Choose another prefix\n")

                        while answer not in ['1', '2']:
                            answer = input('Choose between 1 or 2: ', end='')
                        if answer == "1":
                            self.defence = False
                            self.file_rename(path, item)
                            continue
                        else:
                            break

                self.file_rename(path, item)

        self.report()

    def report(self):
        if recursion == "2":
            print(f"{self.changed} files was changed successfully.")
            if self.hiden > 0:
                self.console.print(f"[red]{self.hiden} files was hidden because start with '.' after re-name[/red]")
            _ = input("Press ENTER to continue...")
        else:
            print(f"{self.changed} files/folders was changed successfully.")
            if self.hiden > 0:
                self.console.print(
                    f"[red]{self.hiden} files/folders was hidden because start with '.' after re-name[/red]")
            _ = input("Press ENTER to continue...")

    def clean_console(self, directory="", prefix=""):
        self.console.clear()
        if directory != "":
            self.console.print(f"Directory: [green]{directory}[/green]")
        if prefix != "":
            self.console.print(f"Prefix: [green]\{prefix}[/green]")

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
    clear = Console().clear()
    recursion = input("Enable inspection of subfolders?\n1.Yes 2.No\n")
    while recursion not in ["1", "2"]:
        clear
        recursion = input("Enable inspection of subfolders?\n1.Yes 2.No\n")

    while True:
        try:
            app = CheckPrefix(recursion=recursion)
        except KeyboardInterrupt:
            break

# pyinstaller -F --name="SortPrefix" main.py
