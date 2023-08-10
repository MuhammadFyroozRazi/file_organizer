import tkinter as tk
from tkinter import ttk
import file_organizer as fo

def applytodirectory():
    fo.access_files(
        entry_str.get(),
        check1_var.get(),
        check2_var.get(),
        check3_var.get(),
        check4_var.get(),
        check5_var.get()
        )


window = tk.Tk()
window.title('File Organizer')
window.geometry('420x250+150+250')
window.maxsize('600','350')
window.minsize('420','250')
window.attributes('-topmost',1)
window.iconbitmap('./icon/file_organizer.ico')


target_label=ttk.Label(master=window,text='Target Path')
target_label.pack(pady=(30,5),padx=10,fill='x')
entry_str=tk.StringVar()
target_entry=ttk.Entry(master=window,textvariable=entry_str)
target_entry.pack(padx=10,fill='x')



check1_var=tk.IntVar()
check2_var=tk.IntVar()
check3_var=tk.IntVar()
check4_var=tk.IntVar()
check5_var=tk.IntVar()

checkbox_frame=ttk.Frame()
checkbox_frame.columnconfigure(0, weight=5)

check1=ttk.Checkbutton(master=checkbox_frame,text='videos',variable=check1_var)
check1.grid(row=0,column=0,ipadx=5)
check2=ttk.Checkbutton(master=checkbox_frame,text='images',variable=check2_var)
check2.grid(row=0,column=1,ipadx=5)
check3=ttk.Checkbutton(master=checkbox_frame,text='documents',variable=check3_var)
check3.grid(row=0,column=2,ipadx=5)
check4=ttk.Checkbutton(master=checkbox_frame,text='audios',variable=check4_var)
check4.grid(row=0,column=3,ipadx=5)
check5=ttk.Checkbutton(master=checkbox_frame,text='compressed',variable=check5_var)
check5.grid(row=0,column=4,ipadx=5)

checkbox_frame.pack(pady=(15,0))

submit_btn=tk.Button(master=window,text='Apply',bg='navy',fg='white',font='bold 12',command=applytodirectory)
submit_btn.pack(ipadx=5,ipady=2,pady=30)
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    window.mainloop()
