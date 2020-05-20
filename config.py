#!/usr/bin/env python3


import tkinter as tk
from watchdog.observers import Observer


class StatusMessage:
    disconnected = "Disconnected"
    connected =    "  Connected  "


class StatusColor:
    blue = "#004E70"
    lightBlue = "#D9EDF7"
    green = "#27AE60"
    black = "#29302F"


class ClientEvent:
    download = "download"
    upload = "upload"


class ServerEvent:
    downloaded = "file-downloaded"
    uploaded = "file-uploaded"
    saved = "file-saved"


class RequestObject:
    eventName: str
    downloadUrl: str
    uploadUrl: str


class SocketConfig:
    ip = '127.0.0.1'
    port = 31415

