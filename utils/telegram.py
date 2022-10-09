from functools import reduce
import json
import pyrogram
from utils.files import files
import os
import time

class telegram:

    creds = {}
    app = None

    def __init__(self) -> None:
        self.creds = telegram.getCreds(self)
        self.app = pyrogram.Client("my_account", self.creds["id"], self.creds["hash"])

        
    def getCreds(self) -> dict:
        if(not os.path.exists("./data/creds.json")):
            print("You need to get your own Telegram Api id and hash")
            print('''
            
    1.Go to https://my.telegram.org/auth and Login to your Telegram account with the phone number of the developer account to use.
    2.Click under API Development tools.
    3.A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
    4. Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!

            ''')
            id = input("Enter your API id: ")
            hash = input("Enter your API hash: ")
            f = open("./data/creds.json", "w")
            x = {
                "id": id,
                "hash" : hash
            }
            f.write(files.toJSON(x))
            f.close
            app = pyrogram.Client("my_account", id, hash)
            with app:
                app.send_message("me","Welcome to Tdrive!! You have been Successfully authenticated and now you can use Tdrive to store all your Files for free.")

            
        f = open("./data/creds.json", "r")
        d = json.loads(f.read())
        return d

    def sendDocument(self,path):
        app = self.app
        with app:
            app.send_document("me",path,progress=telegram.sendingProgress)

    def sendingProgress(current, total):
        print("\r" + f"Progress: {current * 100 / total:.1f}%")