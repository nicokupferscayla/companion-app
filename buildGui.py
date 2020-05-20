import tkinter as tk

from config import StatusColor, StatusMessage, CanvasSize


infoText = tk.StringVar()
infoText.set("")

root = tk.Tk()
statusText = tk.StringVar()
statusText.set(StatusMessage().disconnected)

canvas = tk.Canvas(root, width=CanvasSize.width, height=CanvasSize.height)  # size of the app

infoLabel = tk.Label(root, textvariable=infoText, fg=StatusColor.lightBlue, font=('helvetica', 15, 'bold'))
canvas.create_window(CanvasSize.width / 2, 250, window=infoLabel)
statusLabel = tk.Label(root, textvariable=statusText, fg=StatusColor.blue, font=('helvetica', 20, 'bold'))
canvas.create_window(CanvasSize.width / 2, 200, window=statusLabel)


def buildGui():
    label1 = tk.Label(root, text="Companion App", fg=StatusColor.blue, font=('helvetica', 25, 'bold'))
    canvas.create_window(CanvasSize.width / 2, 90, window=label1)

    background_image = tk.PhotoImage(file="images/scayla.png")
    background_label = tk.Label(root, image=background_image)
    canvas.create_window(CanvasSize.width / 2, 50, window=background_label)

    root.configure(bg=StatusColor.blue)
    # root.protocol("WM_DELETE_WINDOW", root.destroy)

    canvas.pack()
    root.mainloop()
