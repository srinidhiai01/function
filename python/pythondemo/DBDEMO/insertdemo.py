from tkinter import *
import mysql.connector

Win=Tk()
Win.title("Insert into mysql DB demo")
Win.geometry("500x500")

frameleft=Frame(Win,bg="pink",width=500,height=500,padx=80,pady=30)
frameleft.pack(side=LEFT)

frameright=Frame(Win,bg="skyblue",width=500,height=500)
frameright.pack(side=RIGHT)

Labeltitleofoperation=Label(frameleft,text="Insert into mysql DB demo")
Labeltitleofoperation.grid(row=0,column=1)

labelname=Label(frameleft,text="name")
labelname.grid(row=2,column=1,padx=10,pady=10)
lblTamil=Label(frameleft,text="Tamil")
lblTamil.grid(row=3,column=1,padx=30,pady=10)


Win.mainloop()