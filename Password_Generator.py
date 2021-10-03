from tkinter import *
from random import randint
from tkinter import messagebox

win=Tk()
win.title('Password Generator')
win.geometry("480x300")
win.iconbitmap("pass.ico")

#Generate Random Strong Password
def new_rand_pass():
    #Clear Entry Box
    entry_pw.delete(0,END)

    pw_length=0
    #Get Password Length
    try:
        pw_length=int(entry_pass_length.get())
    except:
        messagebox.showerror('error', 'please enter password length!')
    #create variable the hold password
    my_pass=''

    # loop through password length
    for p in range(pw_length):
        my_pass += chr(randint(33, 126))

    #Output Pass to the Screen
    entry_pw.insert(0,my_pass)

#copy to clipboard
def clip_board():
    #clear the clipboard
    win.clipboard_clear()
    win.clipboard_append(entry_pw.get())
    messagebox.showinfo('info', 'password copied!')


#Lable Frame
lbl_frame=LabelFrame(win,text='How Many Characters?',fg='blue')
lbl_frame.pack(pady=20)

#Create Entry Box To Designate Number Of Character
entry_pass_length=Entry(lbl_frame,font=("Helvetica",18),fg='blue')
entry_pass_length.pack(pady=15,padx=15)

#Create Entry Box for Returned Password
entry_pw=Entry(win,text='',font=('Helvetica',18),bd=0,bg="systembuttonface",fg='blue')
entry_pw.pack(pady=15)

#Create a Frame for out Buttons
frame_btn=Frame(win)
frame_btn.pack(pady=15)

#Create Buttons
btn_generate=Button(frame_btn,width=20,height=3,text='Generate Password',command=new_rand_pass,\
                    fg='blue',bg='gray80')
btn_generate.grid(row=2,column=0,padx=8)

btn_clipboard=Button(frame_btn,width=20,height=3,text='Copy To Clipboard',command=clip_board,fg='blue',bg='gray80')
btn_clipboard.grid(row=2,column=1,padx=8)

win.mainloop()





