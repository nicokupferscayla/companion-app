import tkinter as tk
import sip
import PyQt4._qt
# from PIL import Image, ImageTk
from config import StatusColor, StatusMessage


class Application(tk.Frame):
    _info_text: tk.StringVar
    _status_text: tk.StringVar
    _status_label: tk.Label
    _info_label: tk.Label
    _scayla_logo_label: tk.Label
    _app_name: tk.Label

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        # self.socket = socket
        self.createWidgets()

    def createWidgets(self):
        self._info_text = tk.StringVar()
        self._status_text = tk.StringVar()

        self._info_text.set("... ...")
        self._status_text.set(StatusMessage().disconnected)

        scayla_logo = tk.PhotoImage(file="scayla2.gif")
        self._scayla_logo_label = tk.Label(self, image=scayla_logo)
        self._scayla_logo_label.image = scayla_logo
        self._scayla_logo_label.pack()

        self._app_name = tk.Label(self, text="Companion App", fg=StatusColor.blue, font=('helvetica', 25, 'bold'))
        self._app_name.pack(padx=20, pady=0)

        self._status_label = tk.Label(self, textvariable=self._status_text, fg=StatusColor.blue,
                                      font=('helvetica', 20, 'bold'))
        self._status_label.pack(padx=20, pady=10)
        #
        self._info_label = tk.Label(self, textvariable=self._info_text, fg=StatusColor.lightBlue,
                                    font=('helvetica', 15, 'bold'))
        self._info_label.pack(padx=20, pady=10)

    def closeApp(self):
        self.quit()

    def setInfo(self, text: StatusMessage):
        self._info_text.set(text)

    def setStatus(self, text: StatusMessage):
        self._status_text.set(text)

    def setStatusColor(self, color: StatusColor):
        self._status_label.config(fg=color)


application = Application()
