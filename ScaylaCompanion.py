#!/usr/bin/env python3

import sys


from websocketThread import WebSocketThread
from buildGui import buildGui
from logger import logger

sys.path.append('.')

if __name__ == '__main__':
    socket = WebSocketThread()
    try:
        socket.start()
        buildGui()
    except KeyboardInterrupt:
        # TODO: close ws server and loop correctly
        logger("[exit] Exiting program...")
