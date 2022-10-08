from calendar import prmonth
import json
import os
from utils.files import files
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
		elif[cmd[0]=="clear"]:
			os.system('clear')

	def help(self):
		print(" no help for u")
		print(self.folder)

	def mkdir(self,cmd):
		if(len(cmd)<2):
			print("mkdir: missing operand")
			return 0
		x = self.getPwd()
		oldOcc = str(x)
		x["subdirs"].append(files.createNewfolder(cmd[1]))
		str(self.folder).replace(oldOcc,str(x),1)
		files.updateFileSystemChanges(self.folder)
		print("created "+ cmd[1])

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
		x = self.getPwd()
		oldOcc = str(x)
		x["subdirs"].append(files.createEmptyFile(cmd[1]))
		str(self.folder).replace(oldOcc,str(x),1)
		files.updateFileSystemChanges(self.folder)
		print("created "+ cmd[1])
		
	def getPwd(self)->dict:
		s = str(self.pwd).split("/")
		x = self.folder
		for i in s:
			x = x["subdirs"][int(i)]
			
		return x