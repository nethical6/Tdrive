import json
import os

class files:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True)
    
    def generateFileSystem():
        if (os.path.exists("./data/filesystem.json")):
            return
        f = open("./data/filesystem.json", "w")
        list = { 
            "type":"directory",
            "name":"Root",
            "subdirs":[ { 
            "type":"directory",
            "name":"home",
            "subdirs":[
        ]}
        ]}
        f.write(json.dumps(list))
        f.close

    def createNewfolder(name) -> dict:
        return {
            "type":"directory",
            "name":name,
            "subdirs":[]
            }

    def updateFileSystemChanges(folder):
        f = open("./data/filesystem.json", "w")
        f.write(json.dumps(folder))
        f.close