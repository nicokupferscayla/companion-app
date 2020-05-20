import json
import threading
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from logger import logger

from downloadConfig import DOWNLOAD_DIR

from config import ServerEvent


class FileWatchThread(threading.Thread, FileSystemEventHandler):
    def __init__(self, socket, download_path, file_name):
        logger('[__init__] FileWatchThread')
        threading.Thread.__init__(self)
        self.connected = set()
        self.socket = socket
        self.observer = Observer()
        self.download_path = download_path
        self.file_name = file_name

    def on_modified(self, event):
        logger('[info] File save detected')
        self.socket.sendMessage(json.dumps({
            "eventName": ServerEvent.saved,
            "unixTime": int(time.time()),
        }))

    def run(self):
        logger('[info] File Watch started')

        self.observer.schedule(self, DOWNLOAD_DIR, recursive=False)
        self.observer.start()

        while not self.socket.closed:
            time.sleep(1)
        logger('[close] FileWatchThread finished')
        self.observer.stop()
        return True
