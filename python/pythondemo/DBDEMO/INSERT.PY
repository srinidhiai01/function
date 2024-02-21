from tkinter import *
import mysql.connector

win=Tk()

win.title("MySQL DB Demo")
win.geometry("300x300")

class manipulationWindow:
    def __init__(self):
        frametop=Frame(win, bg="skyblue",width=800, height=300, padx=10,pady=10)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT" ).pack(padx=10, pady=10)
        btnupdate=Button(frametop,text="UPDATE" ).pack(padx=10, pady=10)
        btndelete=Button(frametop,text="DELETE").pack(padx=10, pady=10)
    
    
run=manipulationWindow()
win.mainloop()