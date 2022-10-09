from utils.shell import shell
from utils.files import files
from utils.telegram import telegram
print('''
    
         _____   _      _           
        |_   _|_| |_ __(_)_   _____ 
          | |/ _` | '__| \ \ / / _ |
          | | (_| | |  | |\ V /  __/
          |_|\__,_|_|  |_| \_/ \___|
        
        

        Welcome to TDrive.
        Created By Nethical \n\n
        ''')

files.generateFileSystem()

telegram()

f = open("./data/filesystem.json", "r")
shell(f.read())
