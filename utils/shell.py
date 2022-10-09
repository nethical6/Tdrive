
import json
import os
from utils.files import files
from utils.telegram import telegram
class shell():
	prompt = "$"
	pwd = "0"
	def __init__(self,folder )-> None:
		self.folder = json.loads(folder)
		while True:
			cmd = input(self.prompt+" ")
			self.evalCmd(cmd)

	def evalCmd(self,cmd):
		cmd = str(cmd).split(" ")
		if(cmd[0] =='help'):
			shell.help(self)
		elif(cmd[0] == 'mkdir'):
			shell.mkdir(self,cmd)
		elif(cmd[0]== 'ls'):
			shell.ls(self,cmd)
		elif(cmd[0]== 'cd'):
			shell.cd(self,cmd)
		elif(cmd[0] == 'touch'):
			shell.touch(self,cmd)
		elif(cmd[0] == 'upload'):
			shell.upload(self,cmd)
		elif(cmd[0] == 'download'):
			shell.download(self,cmd)
		elif(cmd[0]=="clear"):
			os.system('clear')
		elif(cmd[0]=="rm"):
			shell.rm(self,cmd)
		else:
			print("command not found. Run help to get a list of available commands")

	def help(self):
		print('''
	help - display a list of available commands \n
	cd [directory name] - change the working directory \n
	mkdir [directory name] - Create a new Directory\n
	clear - clear the screen \n
	ls - list out all the files and folders in the current working directory \n
	upload [path to file on localdevice] - Upload a file \n
	download [name of the file to download] - Download a file from server \n
	rm [file/folder] - delete a file or folder
		''')

	def mkdir(self,cmd):
		if(len(cmd)<2):
			print("mkdir: missing operand")
			return 0
		if(shell.fileDoesntExists(self.getPwd(),cmd[1])):
			x = self.getPwd()
			oldOcc = str(x)
			x["subdirs"].append(files.createNewfolder(cmd[1]))
			str(self.folder).replace(oldOcc,str(x),1)
			files.updateFileSystemChanges(self.folder)
			print("created "+ cmd[1])
		else:
			print("file/folder with the same name already exists...")

	def ls(self,cmd):
		x = self.getPwd()
		for i in x["subdirs"]:
			if(i["type"]=="directory"):
				print("\033[91m {}\033[00m" .format(i["name"]))
			else:
				print(i["name"])


	def cd(self,cmd):
		if(len(cmd)<2):
			print("cd: missing operand")
			return 0

		if(cmd[1] == ".."):
			self.pwd = self.pwd.rsplit("/", 1)[0] # remove all after last occurence
			self.prompt = self.prompt.rsplit("/", 1)[0] # remove all after last occurence
			pass


		else:
			for index,item in enumerate(self.getPwd()["subdirs"]):
				
				if(item["name"] == cmd[1]):
					if(item["type"]=="document"):
						print("cd: %s: Not a directory" % item["name"])
						return
					self.pwd+='/'+str(index)
					self.prompt+="/"+item["name"]
					return
			print("Folder doesnot exists")
		
	def touch(self,cmd):
		if(len(cmd)<2):
			print("touch: missing operand")
			return 0
		if(shell.fileDoesntExists(self.getPwd(),cmd[1])):
			x = self.getPwd()
			oldOcc = str(x)
			x["subdirs"].append(files.createEmptyFile(cmd[1]))
			str(self.folder).replace(oldOcc,str(x),1)
			files.updateFileSystemChanges(self.folder)
			print("created "+ cmd[1])
			return
		else:
			print("file/folder with the same name already exists...")

		
	def upload(self,cmd):
		if(len(cmd)<2):
			print("touch: missing operand")
			return 0
		tg = telegram()
		a = tg.sendDocument(cmd[1])

		x = self.getPwd()
		oldOcc = str(x)
		filename = str(cmd[1]).rsplit('/', 1)[1]
		x["subdirs"].append(files.createEmptyFile(filename,a))
		str(self.folder).replace(oldOcc,str(x),1)
		files.updateFileSystemChanges(self.folder)
		print("\n created "+ cmd[1])
		
	def download(self,cmd):
		if(len(cmd)<2):
			print("touch: missing operand")
			return 0
		x = self.getPwd()
		for i in x["subdirs"]:
			if(i["type"] == "document" and i["name"] == cmd[1]):
				tg = telegram()
				tg.downloadDocument(i["file_id"],i["name"])
				print("\n Saved to ./downloads directory")
		
	def rm(self,cmd):
		if(len(cmd)<2):
			print("touch: missing operand")
			return 0
		if(not shell.fileDoesntExists(self.getPwd(),cmd[1])):
			oldOcc = str(self.getPwd())
			str(self.folder).replace(oldOcc,"")
			files.updateFileSystemChanges(self.folder)
			print("deleted"+ cmd[1])
			return
		else:
			print("file/folder with the same name already exists...")

	def getPwd(self)->dict:
		s = str(self.pwd).split("/")
		x = self.folder
		for i in s:
			x = x["subdirs"][int(i)]
			
		return x

	def fileDoesntExists(x,name) -> bool:
		for i in x["subdirs"]:
			if (i["name"] == name): return False
		return True
	