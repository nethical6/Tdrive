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

    