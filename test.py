# from rich.console import Console
import os
#
#
# console = Console()
# a = "hello"
# console.print(f"[green]{a}[/green]")

# # pyinstaller -F --name="Test" test.py
#
# a = "/Users/pc/Desktop/Новая папка"
# b = "{ffd}"
# txt= f'Directory: {a}\nPrefix: {b}'
#
# for i in txt.split("\n"):
#     for j, k in i.split(:)

my = "/Users/pc/Desktop/Новая папка"
counter = 0
folders = 0

def recursive_nest(path=""):
    global counter, folders

    for item in os.listdir(path=path):

        if os.path.isfile(os.path.join(path, item)):
            counter += 1
            print(f"{counter}")
            print(f"{item} - файл в папке {path}")
            print("Переименовываю файл")
            os.rename(os.path.join(path, item), os.path.join(path, str(counter)))

        if os.path.isdir(os.path.join(path, item)):
            recursive_nest(path=os.path.join(path, item))
            os.rename(os.path.join(path, item), os.path.join(path, str(f"Folder {folders}")))


print(recursive_nest(path=my))
print(counter, folders)


#
# def get_nested_counts(rootdir):
#     def count_subdirs(dirs, depth):
#         if len(counts) == depth:
#             counts.append([])  # add new deeper level
#         counts[depth].append(len(dirs))
#         for path in dirs:
#             subdirs = [entry for entry in os.scandir(path)
#                        if entry.is_dir(follow_symlinks=False)]
#             if subdirs:  # if there are subdirs
#                 count_subdirs(subdirs, depth + 1)  # make recursive call
#
#     counts = []
#     count_subdirs([rootdir], 0)
#     return counts
#
# print(get_nested_counts(rootdir=path))