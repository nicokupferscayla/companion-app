import json
import os
import platform
import subprocess
import threading
import urllib.request
import time

import websockets

from config import ServerEvent
from fileWatchThread import FileWatchThread
from logger import logger


class FileDownloadThread(threading.Thread):
    def __init__(self, socket, download_url, download_path, file_name):
        threading.Thread.__init__(self)
        logger('[__init__] FileDownloadThread')
        self.connected = set()
        self.socket = socket
        self.download_url = download_url
        self.download_path = download_path
        self.file_name = file_name
        self.file_watch_thread = None

    def run(self):
        logger('[info] File Download: Started')
        urllib.request.urlretrieve(self.download_url, self.download_path)
        logger('[info] File Download: Finished')
        self.socket.sendMessage(json.dumps({
            "eventName": ServerEvent.downloaded
        }))
        self.open_file(self.download_path)

        self.file_watch_thread = FileWatchThread(self.socket, self.download_path, self.file_name)
        self.file_watch_thread.start()

        while not self.socket.closed:
            time.sleep(1)
        logger('[close] FileDownloadThread finished')
        return True


    def open_file(self, file_path):
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', file_path))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(file_path)
        else:  # linux variants
            subprocess.call(('xdg-open', file_path))