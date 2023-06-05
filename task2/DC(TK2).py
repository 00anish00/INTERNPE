import tkinter as tk
import tkinter.ttk as ttk
import datetime

base = tk.Tk()
base.title('DG-CAL')

def update_time():
    now = datetime.datetime.now()
    tim = now.strftime('%H:%M:%S %p')
    date = now.strftime('%Y-%m-%d')
    dg_label.config(text=tim + '\n' + str(date))
    dg_label.after(1000, update_time)

dg_label = tk.Label(base, font=("DS-Digital", 80), background='black', foreground='deep sky blue')
dg_label.pack(anchor='center')

update_time()

base.mainloop()
