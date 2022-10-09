import json
import os

class files:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True)
    
    def generateFileSystem():

        if not os.path.exists("./data"):
           os.makedirs("./data")
        if not os.path.exists("./downloads"):
           os.makedirs("./downloads")


        if (os.path.exists("./data/filesystem.json")):
            return
        f = open("./data/filesystem.json", "w")
        list = { 
            "type":"directory",
            "name":"root",
            "id": hash("root"),
            "subdirs":[ { 
            "type":"directory",
            "name":"home",
            "id": hash('home'),
            "subdirs":[
        ]}
        ]}
        f.write(json.dumps(list))
        f.close

    def createNewfolder(name) -> dict:
        return {
            "type":"directory",
            "name":name,
            "id": hash(name),
            "subdirs":[]
            }

    def updateFileSystemChanges(folder):
        f = open("./data/filesystem.json", "w")
        f.write(json.dumps(folder))
        f.close

    def createEmptyFile(name,fileid="0"):
        return {
            "type":"document",
            "name":name,
            "id": hash(name),
            "file_id" : fileid
            }
