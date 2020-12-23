import matplotlib.pyplot as plt
import os.path, time

from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = tk.Tk()
back = tk.Frame(master=root, width=500, height=500, bg='white')
back.pack_propagate(0)
back.pack(fill="none", expand=True)


def getData(tx, lines):
    x = []
    z = []
    y = []
    r = 0
    for i in range(len(lines)):
        if lines[i][0] == tx:
            for j in range(1, len(lines[0])):
                x.append(j - 1)
                y.append(r)
                z.append(int(lines[i][j]))
            r += 1
    return x, y, z


def getPercAvg(array):
    tot = 0
    for element in array:
        tot += element
    percAvg = tot / (len(array) * 16) * 100
    return percAvg


def main():
    Tk().withdraw()
    filename = askopenfilename()
    f = open(filename, 'r')
    try:
        firstLine = f.readline()
    except:
        warning.place(relx=.5, rely=0.8, anchor="center")
        firstLine = ""
    if "Sequence number" in firstLine:
        content_list = f.readlines()

        warning.place_forget()

        lines = []
        for line in content_list:
            if "Tx " in line:
                line = line[4:-7]
                line = line.split()
                lines.append(line)

        fig = plt.figure(figsize=(12, 6))
        titleAx = fig.add_subplot(231)
        ax4 = fig.add_subplot(232, projection="3d")
        ax3 = fig.add_subplot(233, projection="3d")
        ax2 = fig.add_subplot(234, projection="3d")
        ax1 = fig.add_subplot(235, projection="3d")
        ax0 = fig.add_subplot(236, projection="3d")

        axs = [ax4, ax3, ax2, ax1, ax0]

        titleAx.set_axis_off()
        fileNameIndex = filename.rfind('/') + 1
        title = filename[fileNameIndex:]
        titleAx.text(.1, .5, title, fontsize=10)
        fileTime = (time.ctime(os.path.getctime(filename)))
        titleAx.text(.1, .3, fileTime, fontsize=10)

        titleAx.text(.1, .1, 'Copyright 2020 Sonova', fontsize=7)

        i = 12
        plots = []
        for ax in axs:
            x, y, z = getData(str(i), lines)
            newPlot = ax.scatter(x, y, z, c=z, cmap='winter', marker='o', vmin=0, vmax=16)
            plots.append(newPlot)

            ticks = (0, 2, 4, 6, 8, 10, 12, 14, 16)
            cbar = plt.colorbar(newPlot, ax=ax, pad=0.1, shrink=0.5, ticks=(0, 16))
            cbar.set_label('Packet', fontsize=8, labelpad=-10)

            percentage = getPercAvg(z)
            percentage = round(percentage, 2)
            gTitle = "Tx Power: " + str(i - 15) + " dBm, " + str(percentage) + "%"
            ax.set_title(gTitle, y=0.9, fontsize=10)
            ax.set_zlim3d(0, 16)
            ax.set_zticks(ticks)
            ax.set_xlabel('Channel', fontsize=8)
            ax.set_ylabel('Repetition', fontsize=8)
            ax.view_init(elev=10, azim=280)
            i -= 3

        plt.subplots_adjust(left=0.025, bottom=0.05, right=0.90, top=1, wspace=0.3, hspace=0.13)
        plt.show()

    else:
        warning.place(relx=.5, rely=0.8, anchor="center")


def end_program():
    raise SystemExit


root.title('PER Analysis 1.0 - Copyright 2020 Sonova')
warning = tk.Label(master=back, text="Unrecognizable File!", fg="red", bg="black", font=("Courier", 20))

button = tk.Button(master=back, text="Choose File", bg="gray", height=5, width=30, command=main)
button.place(relx=.5, rely=.5, anchor="center")

root.protocol("WM_DELETE_WINDOW", end_program)
root.mainloop()
