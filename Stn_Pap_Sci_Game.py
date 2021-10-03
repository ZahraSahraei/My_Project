from tkinter import *
from PIL import Image,ImageTk
from random import randint

win=Tk()
win.title("Rock Paper Scissor Game")
win.geometry("712x370")
win.resizable(False, False)
win.iconbitmap("title.ico")
win.configure(bg='Blue')
win.columnconfigure(0, weight=1)  # set all content in center

#========================Image=========================
#player
img_rock1=ImageTk.PhotoImage(Image.open("stone4_new.png"))
img_paper1=ImageTk.PhotoImage(Image.open("paper4_new.png"))
img_scissor1=ImageTk.PhotoImage(Image.open("scissor2_new.png"))

#computer
img_rock2=ImageTk.PhotoImage(Image.open("stone_new11.png"))
img_paper2=ImageTk.PhotoImage(Image.open("paper_new11.png"))
img_scissor2=ImageTk.PhotoImage(Image.open("scissor_new11.png"))

#============================Default Labels=====================
lbl_computer=Label(win,image=img_rock2)
lbl_computer.grid(row=1,column=0)

lbl_player=Label(win,image=img_rock1)
lbl_player.grid(row=1,column=4)

#============================Scores=======================
computer_score=Label(win,text=0,font=('mitra',20,"bold"),bg='Blue',fg='gold')
computer_score.grid(row=1,column=1)

player_score=Label(win,text=0,font=('mitra',20,"bold"),bg='Blue',fg='gold')
player_score.grid(row=1,column=3)

#============================Indicators=============================

player_indicator=Label(win,width=9,font=('mitra',18,'bold'),text="PLAYER",bg='gold',fg='blue').grid(row=0,column=3)

computer_indicator=Label(win,font=('mitra',18,'bold'),text="COMPUTER",bg='gold',fg='blue').grid(row=0,column=1)

#============================Functions==============================
def updateMessage(m):
    lbl_message['text']=''
    lbl_message['text']=m

def computer_update():
    counter_co=int(computer_score['text'])
    counter_co+=1
    computer_score['text']=str(counter_co)

def player_update():
    counter_pl= int(player_score['text'])
    counter_pl += 1
    player_score['text'] = str(counter_pl)

def winner_check(pl,co):
    if pl==co:
        updateMessage("tie!!")

    elif pl=='rock':
        if co=='paper':
            updateMessage("Computer Wins!!")
            computer_update()
        else:
            updateMessage("Player Wins!!")
            player_update()

    elif pl=='paper':
        if co=='scissor':
            updateMessage("Computer Wins!!")
            computer_update()
        else:
            updateMessage("Player Wins!!")
            player_update()

    elif pl == 'scissor':
        if co == 'rock':
            updateMessage("Computer Wins!!")
            computer_update()
        else:
            updateMessage("Player Wins!!")
            player_update()

    elif co == 'rock':
        if pl == 'paper':
            updateMessage("Player Wins!!")
            player_update()
        else:
            updateMessage("Computer Wins!!")
            computer_update()

    elif co == 'paper':
        if pl== 'scissor':
            updateMessage("Player Wins!!")
            player_update()
        else:
            updateMessage("Computer Wins!!")
            computer_update()

    elif co == 'scissor':
        if pl == 'rock':
            updateMessage("Player Wins!!")
            player_update()
        else:
            updateMessage("Computer Wins!!")
            computer_update()

select=["rock",'paper','scissor']

def choice_update(a):

    choice_computer=select[randint(0,2)]

    if choice_computer=='rock':
        lbl_computer.configure(image=img_rock2)
    elif choice_computer=='paper':
        lbl_computer.configure(image=img_paper2)
    else:
        lbl_computer.configure(image=img_scissor2)

    if a=='rock':
        lbl_player.configure(image=img_rock1)

    elif a=='paper':
        lbl_player.configure(image=img_paper1)
    else:
        lbl_player.configure(image=img_scissor1)

    winner_check(a,choice_computer)

# Reset The Game
def reset_game():

    computer_score['text']=0
    player_score['text']=0
    lbl_message['text']=''
    lbl_computer .configure(image=img_rock2)
    lbl_player .configure(image=img_rock1)

#================================Buttons==============================

btn_rock=Button(win,width=9,height=1,text="Rock",font=('mitra',19,'bold'),bg='Orange1',fg='blue',
                command=lambda:choice_update("rock")).grid(row=2,column=1)
btn_paper=Button(win,width=9,height=1,text="Paper",font=('mitra',19,'bold'),bg='Orange1',fg='blue',
                 command=lambda:choice_update("paper")).grid(row=2,column=2)
btn_scissor=Button(win,width=9,height=1,text="Scissor",font=('mitra',19,'bold'),bg='Orange1',fg='blue',
                   command=lambda:choice_update("scissor")).grid(row=2,column=3)

#================================MessageLabel=======================
lbl_message=Label(win,width=13,font=('mitra',15,'bold'), bg='Blue',fg='white')
lbl_message.grid(row=3,column=2)
lbl_message.config(pady=23)

#================================Restart Game============================
btn_restart=Button(win,width=12,height=1,text="Restart game",font=('mitra',19,'bold'),bg='firebrick1',fg='blue',
                command=reset_game).grid(row=4,column=2)

win.mainloop()





