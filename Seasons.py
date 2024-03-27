from tkinter import *
import tkinter as tk


###################################

def Winter(event):
    win = tk.Toplevel(window)
    win.title("Зима")
    win.resizable(0,0)
    w=win.winfo_screenwidth()//2-300
    h=win.winfo_screenheight()//2-200
    win.geometry(f'600x400+{w}+{h}')

    frm = tk.Frame(
        master=win,
        bg="#cae8ff",
        width=600,
        height=400
    )
    frm.pack()

    back_btn = tk.Button(
        text="Назад",
        font="Courier 20",
        bg="#282828",
        master=win,
        width=5,
        height=0,
        fg="#e4e4e4",
        command=lambda: win.destroy()
    )
    back_btn.place(x=15, y=330)

    text = tk.Label(
        text = "Зима - это одно из четырех времен года. \nК зимним месяцам относятся декабрь, \nянварь и февраль. В Северном полушарии \nзимой обычно выпадает снег и держатся \nнизкие температуры воздуха.",
        master=frm,
        font="Courier 17",
        width=40,
        height=10,
        bg="#cae8ff"
    )
    text.place(x=10, y=50)

def Spring(event):
    win = tk.Toplevel(window)
    win.title("Весна")
    win.resizable(0,0)
    w=win.winfo_screenwidth()//2-300
    h=win.winfo_screenheight()//2-200
    win.geometry(f'600x400+{w}+{h}')

    frm = tk.Frame(
        master=win,
        bg="#ccffea",
        width=600,
        height=400
    )
    frm.pack()

    back_btn = tk.Button(
        text="Назад",
        font="Courier 20",
        bg="#282828",
        master=win,
        width=5,
        height=0,
        fg="#e4e4e4",
        command=lambda: win.destroy()
    )
    back_btn.place(x=15, y=330)

    text = tk.Label(
        text = "Весна - это одно из четырех времен \nгода. К весенним месяцам относятся \nмарт, апрель и май. Весной происходит \nтаяние зимнего снега и пробуждение \nприроды.",
        master=frm,
        font="Courier 17",
        width=40,
        height=10,
        bg="#ccffea"
    )
    text.place(x=10, y=50)

def Summer(event):
    win = tk.Toplevel(window)
    win.title("Лето")
    win.resizable(0,0)
    w=win.winfo_screenwidth()//2-300
    h=win.winfo_screenheight()//2-200
    win.geometry(f'600x400+{w}+{h}')

    frm = tk.Frame(
        master=win,
        bg="#fde3ce",
        width=600,
        height=400
    )
    frm.pack()

    back_btn = tk.Button(
        text="Назад",
        font="Courier 20",
        bg="#282828",
        master=win,
        width=5,
        height=0,
        fg="#e4e4e4",
        command=lambda: win.destroy()
    )
    back_btn.place(x=15, y=330)

    text = tk.Label(
        text = "Лето - это одно из четырех времен года. \nК летним месяцам относятся июнь, \nиюль и август. Лето характеризуется \nнаиболее высокой температурой \nокружающей среды. В день летнего \nсолнцестояния дни самые длинные, \nа ночи самые короткие.",
        master=frm,
        font="Courier 17",
        width=40,
        height=10,
        bg="#fde3ce"
    )
    text.place(x=20, y=50)

def Autumn(event):
    win = tk.Toplevel(window)
    win.title("Осень")
    win.resizable(0,0)
    w=win.winfo_screenwidth()//2-300
    h=win.winfo_screenheight()//2-200
    win.geometry(f'600x400+{w}+{h}')

    frm = tk.Frame(
        master=win,
        bg="#ffcce1",
        width=600,
        height=400
    )
    frm.pack()

    back_btn = tk.Button(
        text="Назад",
        font="Courier 20",
        bg="#282828",
        master=win,
        width=5,
        height=0,
        fg="#e4e4e4",
        command=lambda: win.destroy()
    )
    back_btn.place(x=15, y=330)

    text = tk.Label(
        text = "Осень - это одно из четырех времен \nгода. К осенним месяцам относятся \nсентябрь, октябрь и ноябрь. Осень — \nсезон угасания природы, когда солнце \nстановится всё ниже, световой день — \nкороче, и становится всё холоднее \nи холоднее.",
        master=frm,
        font="Courier 17",
        width=40,
        height=10,
        bg="#ffcce1"
    )
    text.place(x=20, y=50)


###################################

display = ""

window = tk.Tk()
window.title("Времена года")
window.resizable(0,0)
w=window.winfo_screenwidth()//2-200
h=window.winfo_screenheight()//2-250
window.geometry(f'400x500+{w}+{h}')

frame = tk.Frame(
    master=window,
    width=400,
    height=600,
    bg="#e4e4e4"
)
frame.pack()

title = tk.Label(
    text="Времена года",
    font="Courier 30",
    master=frame,
    bg="#e4e4e4"
)
title.place(x=60, y=40)

table = tk.Frame(
    master=frame,
    bg="#d7d7d7",
    width=300,
    height=280
)
table.place(x=50, y=145)

#####Кнопки#######################

winter_btn = tk.Button(
    text="Зима",
    font="Courier 20",
    bg="#2a9df8",
    master=table,
    width=9,
    height=4,
    fg="#e4e4e4"
)
winter_btn.place(x=0, y=0)
winter_btn.bind("<Button-1>", Winter)

spring_btn = tk.Button(
    text="Весна",
    font="Courier 20",
    bg="#00bd6e",
    master=table,
    width=9,
    height=4,
    fg="#e4e4e4"
)
spring_btn.place(x=150, y=0)
spring_btn.bind("<Button-1>", Spring)

autumn_btn = tk.Button(
    text="Осень",
    font="Courier 20",
    bg="#bd004f",
    master=table,
    width=9,
    height=4,
    fg="#e4e4e4"
)
autumn_btn.place(x=0, y=140)
autumn_btn.bind("<Button-1>", Autumn)

summer_btn = tk.Button(
    text="Лето",
    font="Courier 20",
    bg="#f8852a",
    master=table,
    width=9,
    height=4,
    fg="#e4e4e4"
)
summer_btn.place(x=150, y=140)
summer_btn.bind("<Button-1>", Summer)

########################################

window.mainloop()