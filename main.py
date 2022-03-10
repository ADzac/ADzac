import os
import platform
import tkinter
import socket


def restart(args):
    os_name = platform.system()
    if args == 1 and os_name == 'Linux':
        os.system('/sbin/shutdown -r +10')
        print("Restarting")
    if args == 2 and os_name == 'Linux':
        os.system('/sbin/shutdown +10')
        print("Shutting Down")
    else:
        exit()


gui = tkinter.Tk()
gui.geometry("300x300")


btnRes = tkinter.Button(gui, text="Restart", command=lambda: restart(1))
btnShut = tkinter.Button(gui, text="Shutdown", command=lambda: restart(2))
btnRes.pack()
btnShut.pack()
gui.mainloop()
