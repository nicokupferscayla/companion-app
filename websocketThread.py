#!/usr/bin/env python3
import asyncio
import json
import sys
import threading

import websockets
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

from config import ClientEvent, RequestObject, SocketConfig, StatusMessage, StatusColor
from buildGui import statusText, statusLabel
from downloadConfig import *
from fileDownloadThread import FileDownloadThread
from fileUploadThread import FileUploadThread
from logger import logger

sys.path.append('.')


class SimpleEcho(WebSocket):
    file_download_thread = None
    file_watch_thread = None

    def handleMessage(self):
        request: RequestObject = json.loads(self.data)
        if request['eventName'] == ClientEvent.download:
            file_path = DOWNLOAD_DIR + "/" + request['fileName']
            # file_path = DOWNLOAD_DIR + "/" + str(random.getrandbits(128)) + "-" + request['fileName']

            self.file_download_thread = FileDownloadThread(self, request['downloadUrl'], file_path, request['fileName'])
            self.file_download_thread.start()

        if request['eventName'] == ClientEvent.upload:
            self.file_upload_thread = FileUploadThread(self, request['uploadUrl'], request['fileName'])
            self.file_upload_thread.start()

    def handleConnected(self):
        print(self.address, 'Connected')
        statusText.set(StatusMessage.connected)
        statusLabel.config(fg=StatusColor.green)

    def handleClose(self):
        print(self.address, 'Disconnected')
        statusText.set(StatusMessage.disconnected)
        statusLabel.config(fg=StatusColor.black)


class WebSocketThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.connected = set()
        logger('[__init__] WebsocketThread')

    def run(self):
        logger('[info] Scayla WebSocket started')
        server = SimpleWebSocketServer(SocketConfig.ip, SocketConfig.port, SimpleEcho)
        server.serveforever()

    async def handler(self, websocket, path):
        self.connected.add(websocket)
        try:
            request = await websocket.recv()
        except websockets.exceptions.ConnectionClosed:
            pass
        except KeyboardInterrupt:
            pass
        finally:
            self.connected.remove(websocket)

    def sendData(self, data):
        for websocket in self.connected.copy():
            logger("Sending data: %s" % data)
            coro = websocket.send(data)
            future = asyncio.run_coroutine_threadsafe(coro)
