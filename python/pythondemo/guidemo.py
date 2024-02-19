from tkinter import *
win=Tk()
win.title("Arithmatic Operation")
win.geometry("500x500+600+600")
#win.state("zoomed")
win.config(bg="sky blue")

def addition():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a+b
    labeloutput.config(text=c)

def subtraction():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a-b
    labeloutput.config(text=c)
def multiply():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a*b
    labeloutput.config(text=c)

def division():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a/b
    labeloutput.config(text=c)


def modulus():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a%b
    labeloutput.config(text=c)


def Exponentiation():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a**b
    labeloutput.config(text=c)

def floordivision():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a//b
    labeloutput.config(text=c)

def equal():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a==b
    labeloutput.config(text=c)

def notequal():
    a=int(tbEntrya.get())
    b=int(tbEntrya.get())
    c=a!=b
    labeloutput.config(text=c)

def greaterthan():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a>b
    labeloutput.config(text=c)

def lesserthan():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a<b
    labeloutput.config(text=c)









Labeltitle=Label(win,text="Arithmatic Operation",fg="blue" )
Labeltitle.grid(row=0,column=1,padx=40,pady=40)

label1msg=Label(win,text="Enter value a :" ,fg="blue")
label1msg.grid(row=1,column=8,padx=40,pady=40)

tbEntrya=Entry(win,width=60)
tbEntrya.grid(row=1,column=9,padx=40,pady=40)

label2msg=Label(win,text="Enter value b :",fg="blue")
label2msg.grid(row=2,column=8,padx=40,pady=40)

tbEntryb=Entry(win,width=60)
tbEntryb.grid(row=2,column=9,padx=40,pady=40)

labeloutput=Label(win,text="value ",fg="blue")
labeloutput.grid(row=3,column=11, pady=20)

Buttonadd=Button(win,text="Addition",command=addition,fg="blue")
Buttonadd.grid(row=10,column=12)

Buttonsub=Button(win,text="subtraction",command=subtraction,fg="blue")
Buttonsub.grid(row=10,column=13)

Buttonmultiply=Button(win,text="multiply",command=multiply,fg="blue")
Buttonmultiply.grid(row=10,column=14)


Buttondivision=Button(win,text="division",command=division,fg="blue")
Buttondivision.grid(row=10,column=15)

Buttonmodulus=Button(win,text="modulus",command=modulus,fg="blue")
Buttonmodulus.grid(row=10,column=16)

ButtonExponentiation=Button(win,text="Exponentiation",command=Exponentiation,fg="blue")
ButtonExponentiation.grid(row=10,column=17)

Buttonfloordivision=Button(win,text="floordivision",command=floordivision,fg="blue")
Buttonfloordivision.grid(row=10,column=18)

Buttonequal=Button(win,text="equal",command=equal,fg="blue")
Buttonequal.grid(row=10,column=19)

Buttonnotequal=Button(win,text="notequal",command=notequal,fg="blue")
Buttonnotequal.grid(row=10,column=20)

Buttongreaterthan=Button(win,text="greaterthan",command=greaterthan,fg="blue")
Buttongreaterthan.grid(row=10,column=20)

Buttonlesserthan=Button(win,text="lesserthan",command=lesserthan,fg="blue")
Buttonlesserthan.grid(row=10,column=21)


win.mainloop()