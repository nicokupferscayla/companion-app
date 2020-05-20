import tkinter as tk

from config import StatusColor


infoText = tk.StringVar()
# infoText.set("")


# root = tk.Tk()
# statusText = tk.StringVar()
# statusText.set(StatusMessage().disconnected)

# canvasWidth = 300
# canvasHeight = 300

# canvas = tk.Canvas(root, width=canvasWidth, height=canvasHeight)  # size of the app

# infoLabel = tk.Label(root, textvariable=infoText, fg=StatusColor.lightBlue, font=('helvetica', 15, 'bold'))
# canvas.create_window(canvasWidth / 2, 250, window=infoLabel)
# statusLabel = tk.Label(root, textvariable=statusText, fg=StatusColor.blue, font=('helvetica', 20, 'bold'))
# canvas.create_window(canvasWidth / 2, 200, window=statusLabel)


def buildGui():
    print('no gui')
    # label1 = tk.Label(root, text="Companion App", fg=StatusColor.blue, font=('helvetica', 25, 'bold'))
    # canvas.create_window(canvasWidth / 2, 90, window=label1)
    #
    # background_image = tk.PhotoImage(file="images/scayla.png")
    # background_label = tk.Label(root, image=background_image)
    # canvas.create_window(canvasWidth / 2, 50, window=background_label)
    #
    # root.configure(bg=StatusColor.blue)
    # # root.protocol("WM_DELETE_WINDOW", root.destroy)
    #
    # canvas.pack()
    # root.mainloop()
