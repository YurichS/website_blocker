from tkinter import *
import tkinter.messagebox as mb
from datetime import datetime as dt

host_place = "C://Windows//System32//drivers//etc//hosts"
redirect = "127.0.0.1"


def clicked():
    sites = list(given_sites.get().split(","))
    time = given_time.get()
    block_ws(sites, time)
    unblock_ws(sites, time)


def block_ws(sites, time):
    mb.showinfo("Information", "Websites are blocked")
    if dt.now().strftime("%d-%m-%Y %H:%M") < time:
        with open(host_place, "r+") as host_file:
            content = host_file.read()
            for site in sites:
                if site not in content:
                    host_file.writelines(redirect + ' ' + site + "\n")
        host_file.close()
        wd.iconify()


def unblock_ws(sites, time):
    while True:
        if dt.now().strftime("%d-%m-%Y %H:%M") >= time:
            with open(host_place, "r+") as host_file:
                lines = host_file.readlines()
                host_file.seek(0)
                host_file.truncate()
                for line in range(len(lines)):
                    for site in sites:
                        if lines[line] == redirect + ' ' + site + "\n":
                            lines[line] = ""
                            break
                for line in lines:
                    host_file.writelines(line)
            host_file.close()
            mb.showinfo("Information", "Websites are unblocked")
            wd.destroy()
            break


wd = Tk()
wd.title("Website blocker")
wd.geometry("400x400")
wd.resizable(width=True, height=True)
l1 = Label(wd, text="Websites:\n"
                    "(If 2 and more - use comma)")
l1.place(rely=0.3)
given_sites = Entry(wd, width=20)
given_sites.place(relx=0.7, rely=0.33, anchor='center')
l2 = Label(wd, text="Work time:\n"
                    "(day-month-year Hour:Minutes)")
l2.place(rely=0.4)
given_time = Entry(wd, width=20)
given_time.place(relx=0.7, rely=0.43, anchor='center')
btn = Button(wd, width=20, text="Start", command=clicked)
btn.place(relx=0.45, rely=0.55, anchor='center')
while True:
    wd.update()
