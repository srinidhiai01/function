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




Labeltitle=Label(win,text="Arithmatic Operation",fg="blue" )
Labeltitle.grid(row=0,column=1,padx=40,pady=40)

label1msg=Label(win,text="Enter value a :" ,fg="blue")
label1msg.grid(row=1,column=20,padx=40,pady=40)

tbEntrya=Entry(win,width=60)
tbEntrya.grid(row=1,column=35,padx=40,pady=40)

label2msg=Label(win,text="Enter value b :",fg="blue")
label2msg.grid(row=2,column=20,padx=40,pady=40)

tbEntryb=Entry(win,width=60)
tbEntryb.grid(row=2,column=35,padx=40,pady=40)

labeloutput=Label(win,text="value ",fg="blue")
labeloutput.grid(row=3,column=70, pady=20)

Buttonadd=Button(win,text="Addition",command=addition,fg="blue")
Buttonadd.grid(row=4,column=10)

Buttonsub=Button(win,text="subtraction",command=subtraction,fg="blue")
Buttonsub.grid(row=4,column=11)

Buttonmultiply=Button(win,text="multiply",command=multiply,fg="blue")
Buttonmultiply.grid(row=4,column=12)


Buttondivision=Button(win,text="division",command=division,fg="blue")
Buttondivision.grid(row=4,column=13)

Buttonmodulus=Button(win,text="modulus",command=modulus,fg="blue")
Buttonmodulus.grid(row=4,column=14)


win.mainloop()