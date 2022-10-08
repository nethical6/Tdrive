from functools import reduce
import json
import pyrogram
from utils.files import files

class telegram:
    def getCreds() -> dict:
        f = open("./data/creds.json", "r")
        d = json.loads(f.read())
        return d

    def getApp() -> pyrogram.client:
        creds = telegram.getCreds()
        return pyrogram.Client("my_account", creds["id"], creds["hash"])

    def saveAllMessages():
        app = telegram.getApp()
        creds = telegram.getCreds()
        with app:
            f = open("./cache/msgs", "w")
            y = []
            for message in app.get_chat_history(creds["username"]):
                x = {"directory": message.text,
                    "msg_id": message.id,
                    "chat_id" : message.chat.id,
                    "type":"file",
                    "doocument" : files.toJSON(str(message.document))}
                y.append(x)
            f.write(json.dumps(y))
            f.close()

    def listAllFilesFrom(chatId,msgId) -> list:
        app = telegram.getApp()
        # creds = telegram.getCreds()
        # f = open("./cache/msgs","r")
        # y = json.loads(f.read())
        with app:
            for msg in app.get_messages("TdriveDatabot",reply_to_message_ids=54423):
                print(msg)
        return []

    def generateFileSystem(f) -> dict:
        f = open("./cache/msgs","r")
        y = json.loads(f.read())
        listOfFiles = {}

        for msg in y:
            x = str(msg["directory"]).split("/")
            
            print(reduce(lambda x,y: {y:x},reversed(x)))


            # listOfFiles.append()
        # print(listOfFiles)
        return listOfFiles