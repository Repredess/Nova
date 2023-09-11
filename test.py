from rich.console import Console


console = Console()
a = "hello"
console.print(f"[green]{a}[/green]")

# # pyinstaller -F --name="Test" test.py
#
# a = "/Users/pc/Desktop/Новая папка"
# b = "{ffd}"
# txt= f'Directory: {a}\nPrefix: {b}'
#
# for i in txt.split("\n"):
#     for j, k in i.split(:)