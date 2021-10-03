from tkinter import *
import math
import tkinter.messagebox
from tkinter import ttk

win=Tk()
win.title('Scientific Calculator')
win.configure(background='lavenderblush3')
win.resizable(width=False,height=False)
win.geometry("297x356+0+0")
win.iconbitmap("calculator..ico")

calc=Frame(win)
calc.grid()

class Calc():
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False
        self.num=0

    def numberEnter(self,num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())

    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)

    def valid_function(self):
        if self.op=='add':
            self.total+=self.current
        if self.op=='sub':
            self.total-=self.current
        if self.op=='multi':
            self.total*=self.current
        if self.op=='divide':
            self.total/=self.current
        if self.op=='mod':
            self.total%=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def clear_entry(self):
        self.result=False
        self.current='0'
        self.display(0)
        self.input_value=True

    def all_clear_entry(self):
        self.clear_entry()
        self.total=0

    def pm(self):
        try:
            self.result=False
            self.current=-(float(txtDisplay.get()))
        except:
            self.current = 'Error'
        self.display(self.current)

    def squared(self):
        try:
            self.result = False
            self.current = math.sqrt(float(txtDisplay.get()))
        except:
            self.current='Error'
        self.display(self.current)

    def pi(self):
        try:
            self.result=False
            self.current=math.pi
        except:
            self.current = 'Error'
        self.display(self.current)

    def e(self):
        try:
            self.result = False
            self.current = math.e
        except:
            self.current = 'Error'
        self.display(self.current)

    def deg(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        try:
            self.result = False
            self.current = math.exp(float(txtDisplay.get()))
        except:
            self.current = 'Error'
        self.display(self.current)

    def cos(self):
        try:
            self.result = False
            self.current = math.cos(math.radians(float(txtDisplay.get())))
        except:
            self.current = 'Error'
        self.display(self.current)

    def sin(self):
        try:
            self.result = False
            self.current = math.sin(math.radians(float(txtDisplay.get())))
        except:
            self.current = 'Error'
        self.display(self.current)

    def tan(self):
        try:
            self.result = False
            self.current = math.tan(math.radians(float(txtDisplay.get())))
        except:
            self.current = 'Error'
        self.display(self.current)

    def cosh(self):
        try:
            self.result = False
            self.current = math.cosh(math.radians(float(txtDisplay.get())))
        except:
            self.current = 'Error'
        self.display(self.current)

    def sinh(self):
        try:
            self.result = False
            self.current = math.sinh(math.radians(float(txtDisplay.get())))
        except:
            self.current = 'Error'
        self.display(self.current)

    def tanh(self):
        try:
            self.result = False
            self.current = math.tanh(math.radians(float(txtDisplay.get())))
        except:
            self.current = 'Error'
        self.display(self.current)

    def acosh(self):
        try:
            self.result = False
            self.current = math.acosh((float(txtDisplay.get())))
        except:
            self.current = 'Error'
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def ln(self):
        try:
            self.result = False
            self.current = math.log(float(txtDisplay.get()))
        except:
            self.current ='Error'
        self.display(self.current)

    def log10(self):
        try:
            self.result = False
            self.current = math.log10(float(txtDisplay.get()))
        except:
            self.current = 'Error'
        self.display(self.current)

    def log2(self):
        try:
            self.result = False
            self.current = math.log2(float(txtDisplay.get()))
        except:
            self.current = 'Error'
        self.display(self.current)

    def rev(self):
        try:
            self.result = False
            self.num=float(txtDisplay.get())
            self.rev_num=1/self.num
            self.current = self.rev_num
        except:
            self.current = 'Error'
        self.display(self.current)

    def sqr(self):
        try:
            self.result = False
            self.num=float(txtDisplay.get())
            self.current=math.pow(self.num,2)
        except:
            self.current = 'Error'
        self.display(self.current)

    def sqrx(self):
        try:
             self.result = False
             self.num = float(txtDisplay.get())
             self.current = math.pow(10, self.num)
        except:
             self.current = 'Error'
        self.display(self.current)

    def fact(self):
        try:
            self.result = False
            self.num = int(float(txtDisplay.get()))
            if self.num <0:
               self.num= -1* self.num
               self.current = math.factorial(self.num)
            else:
               self.current = math.factorial(self.num)
        except:
            self.current = 'Error'
        self.display(self.current)

added_value=Calc()

txtDisplay=Entry(calc,font=('times new roman',18,'bold'),bg='lavender',bd=15,width=22,justify='right')
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=4,height=1,font=('times new roman',18,'bold'),bd=5,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]['command']=lambda x=numberpad[i]:added_value.numberEnter(x)
        i+=1

#===================================Standard==============================
btnClear=Button(calc,text=chr(67),width=4,height=1,font=('times new roman',18,'bold'),bg='lavenderblush3',bd=5,
                command=added_value.clear_entry).grid(row=1, column=0, pady=1)

btnAllClear=Button(calc,text=chr(67) + chr(69),width=4,height=1,bd=5,font=('times new roman',18,'bold'),
               bg='lavenderblush3',command=added_value.all_clear_entry).grid(row=1,column=1,pady=1)

btnSq=Button(calc,text='\u221A',width=4,height=1,font=('times new roman',18,'bold'),bd=5,bg='lavenderblush3',
             command=added_value.squared).grid(row=1,column=2,pady=1)

btnAdd=Button(calc,text='+',width=4,height=1,font=('times new roman',18,'bold'),bd=5,bg='lavenderblush3',
              command=lambda: added_value.operation('add')).grid(row=1,column=3,pady=1)

btnSub=Button(calc,text='-',width=4,height=1,font=('times new roman',18,'bold'),bd=5,bg='lavenderblush3',
              command=lambda: added_value.operation('sub')).grid(row=2,column=3,pady=1)

btnMult=Button(calc,text='*',width=4,height=1,font=('times new roman',18,'bold'),bd=5,bg='lavenderblush3',
               command=lambda: added_value.operation('multi')).grid(row=3,column=3,pady=1)

btnDiv=Button(calc,text=chr(247),width=4,height=1,font=('times new roman',18,'bold'),bd=5,bg='lavenderblush3',
              command=lambda: added_value.operation('divide')).grid(row=4,column=3,pady=1)

btnZero=Button(calc,text='0',width=4,height=1,font=('times new roman',18,'bold'),bd=5,bg='lavenderblush3',
               command=lambda:added_value.numberEnter(0)).grid(row=5,column=0,pady=1)

btnDot=Button(calc,text='.',width=4,height=1,font=('times new roman',18,'bold'),bd=5,bg='lavenderblush3',
              command=lambda:added_value.numberEnter('.')).grid(row=5,column=1,pady=1)

btnPM=Button(calc,text=chr(177),width=4,height=1,font=('times new roman',18,'bold'),bd=5,bg='lavenderblush3',
             command=added_value.pm).grid(row=5,column=2,pady=1)

btnEquals=Button(calc,text='=',width=4,height=1,font=('times new roman',18,'bold'),bd=5,bg='lavenderblush3',
                 command=added_value.sum_of_total).grid(row=5,column=3,pady=1)

#===============================Scientific Calculator====================
btnPi=Button(calc,text='\u03C0',width=4,height=1,font=('times new roman',18,'bold'),bd=4,bg='lavenderblush3',
             command=added_value.pi).grid(row=1,column=4,pady=1)

btnCos=Button(calc,text='cos',width=4,height=1,font=('times new roman',18,'bold'),bd=4,bg='lavenderblush3',
              command=added_value.cos).grid(row=1,column=5,pady=1)

btnTan=Button(calc,text='tan',width=4,height=1,font=('times new roman',18,'bold'),bd=4,bg='lavenderblush3',
              command=added_value.tan).grid(row=1,column=6,pady=1)

btnSin=Button(calc,text='sin',width=4,height=1,font=('times new roman',18,'bold'),bd=4,bg='lavenderblush3',
              command=added_value.sin).grid(row=1,column=7,pady=1)

#=======================================================================
btnFact=Button(calc,text='x!',width=4,height=1,font=('times new roman',18,'bold'),bd=4,bg='lavenderblush3',
               command=added_value.fact).grid(row=2,column=4,pady=1)

btnCosh=Button(calc,text='cosh',width=4,height=1,font=('times new roman',18,'bold'),bd=4,command=added_value.cosh)\
    .grid(row=2,column=5,pady=1)

btnTanh=Button(calc,text='tanh',width=4,height=1,font=('times new roman',18,'bold'),bd=4,command=added_value.tanh)\
    .grid(row=2,column=6,pady=1)

btnSinh=Button(calc,text='sinh',width=4,height=1,font=('times new roman',18,'bold'),bd=4,command=added_value.sinh)\
    .grid(row=2,column=7,pady=1)

#========================================================================
btnLn=Button(calc,text='ln',width=4,height=1,font=('times new roman',18,'bold'),bd=4,bg='lavenderblush3',
             command=added_value.ln).grid(row=3,column=4,pady=1)

btnExp=Button(calc,text='Exp',width=4,height=1,font=('times new roman',18,'bold'),bd=4,
              command=added_value.exp).grid(row=3,column=5,pady=1)

btnMod=Button(calc,text='mod',width=4,height=1,font=('times new roman',18,'bold'),bd=4,
              command=lambda: added_value.operation('mod')).grid(row=3,column=6,pady=1)

btnE=Button(calc,text='e',width=4,height=1,font=('times new roman',18,'bold'),bd=4,command=added_value.e)\
    .grid(row=3,column=7,pady=1)

#========================================================================
btnLog2=Button(calc,text='log2',width=4,height=1,font=('times new roman',18,'bold'),bd=4,bg='lavenderblush3',
               command=added_value.log2).grid(row=4,column=4,pady=1)

btnDeg=Button(calc,text='deg',width=4,height=1,font=('times new roman',18,'bold'),bd=4,
              command=added_value.deg).grid(row=4,column=5,pady=1)

btnAcosh=Button(calc,text='acosh',width=4,height=1,font=('times new roman',18,'bold'),bd=4,
                command=added_value.acosh).grid(row=4,column=6,pady=1)

btnAsinh=Button(calc,text='asinh',width=4,height=1,font=('times new roman',18,'bold'),bd=4
                ,command=added_value.asinh).grid(row=4,column=7,pady=1)

#========================================================================
btnLog10=Button(calc,text='log10',width=4,height=1,font=('times new roman',18,'bold'),bd=4,bg='lavenderblush3',
                command=added_value.log10).grid(row=5,column=4,pady=1)

btnRev=Button(calc,text='1/x',width=4,height=1,font=('times new roman',18,'bold'),bd=4,bg='lavenderblush3',
              command=added_value.rev).grid(row=5,column=5,pady=1)

btnSqr=Button(calc,text='x\u00b2',width=4,height=1,font=('times new roman',18,'bold'),bd=4,bg='lavenderblush3',
              command=added_value.sqr).grid(row=5,column=6,pady=1)

#t1 = "4x\u2074 + 3x\u207b\u00b2"  # \u excapes, if needed
#t2 = "4x⁴ + 3x⁻²"

btnSqrx=Button(calc,text='10^x', width=4, height=1, font=('times new roman', 18,'bold'), bd=4, bg='lavenderblush3',
               command=added_value.sqrx).grid(row=5,column=7,pady=1)

lblDisplay=Label(calc,text='Scientific Calculator',font=('times new roman',18,'bold'),justify=CENTER)
lblDisplay.grid(row=0,column=4,columnspan=4)

#=================================Menu and function======================

def iExit():
    iExit=tkinter.messagebox.askyesno('Scientific Calculator','do you want to exit?')
    if iExit>0:
        win.destroy()
        return

def Scientific():
    win.resizable(width=False, height=False)
    win.geometry("579x334+0+0")
    #win.geometry("944x568+0+0")

def Standard():
    win.resizable(width=False, height=False)
    win.geometry("297x334+0+0")

menubar=Menu(calc)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Calculator',menu=filemenu)
filemenu.add_command(label='Standard',command=Standard)
filemenu.add_command(label='Scientific',command=Scientific)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=iExit)


# editmenu=Menu(menubar,tearoff=0)
# menubar.add_cascade(label='Edit',menu=editmenu)
# editmenu.add_command(label='Cut')
# editmenu.add_command(label='Copy')
# editmenu.add_separator()
# editmenu.add_command(label='Paste')
#
# helpmenu=Menu(menubar,tearoff=0)
# menubar.add_cascade(label='Help',menu=helpmenu)
# helpmenu.add_command(label='View Help')

win.config(menu=menubar)
win.mainloop()





