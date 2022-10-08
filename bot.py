from utils.shell import shell
from utils.files import files
hello = "hi"
files.generateFileSystem()
f = open("./data/filesystem.json", "r")
shell(f.read())
