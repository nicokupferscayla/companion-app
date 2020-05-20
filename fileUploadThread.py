import json
import threading
import time

from config import ServerEvent
from logger import logger


class FileUploadThread(threading.Thread):
    def __init__(self, socket, upload_url, file_name):
        threading.Thread.__init__(self)
        logger('[__init__] FileUploadThread')
        self.connected = set()
        self.socket = socket
        self.download_url = upload_url
        self.file_name = file_name

    def run(self):
        logger('[info] File Upload: Started')
        time.sleep(2)
        logger('[info] File Upload: Finished')
        self.socket.sendMessage(json.dumps({
            "eventName": ServerEvent.uploaded
        }))

        while not self.socket.closed:
            time.sleep(1)
        logger('[close] FileUploadThread finished')
        return True