from tkinter import *
import mysql.connector
win =Tk()
win.title ("STUDENT DETAILS")
win.geometry("500x200+600+200")
#app.state("zoomed")
win.config(bg="Sky blue")


def MyDBconnection():
    dbcon=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_srinidhi_detailsdb"

    )
    return dbcon
#print5("connected to database at",dbcon)
#dbcon1=my DBconnecton()
#print("connected to database through outside of def at",dbcon1)

def insertvalues():
    NAME=tbEntrya.get()
    TAMIL=tbEntryb.get()
    ENGLISH=tbEntryc.get()
    MATHS=tbEntryd.get()
    SCIENCE=tbEntrye.get()
    SOCIALSCIENCE=tbEntryf.get()
    e_con=MyDBconnection()
    result=e_con.cursor()
    statement="insert into sri4_user_details(NAME,TAMIL,ENGLISH,MATHS,SCIENCE,SOCIALSCIENCE)values(%s,%s,%s,%s,%s,%s);"
    valuepass=(NAME,TAMIL,ENGLISH,MATHS,SCIENCE,SOCIALSCIENCE)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount,"row inserted")


 
def updatevalue():
    NAME=tbEntrya.get()
    TAMIL=tbEntryb.get()
    
    e_con=MyDBconnection()
    result=e_con.cursor()
    statement="update  sri4_user_details set NAME =(%s) where SNO=(%s);"
    valuepass=(NAME,TAMIL)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount,"row updated")



def deletevalue():
    NAME=tbEntrya.get()
    
    
    e_con=MyDBconnection()
    result=e_con.cursor()
    statement="delete from sri4_user_details where SNO=(%s);"
    valuepass=(NAME,)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount,"row deleted")






Labeltitle1=Label(win,text="STUDENT MARK DEATILS",fg="black",font="bold" )
Labeltitle1.grid(row=0,column=9,padx=80,pady=80)

label2msg=Label(win,text="NAME" ,fg="black")
label2msg.grid(row=1,column=8,padx=20,pady=20)

tbEntrya=Entry(win,width=60)
tbEntrya.grid(row=1,column=9,padx=20,pady=20)

Labeltitle2=Label(win,text="SUBJECT",fg="black",font="bold")
Labeltitle2.grid(row=2,column=9,padx=20,pady=20)


label3msg=Label(win,text="TAMIL",fg="black")
label3msg.grid(row=3,column=8,padx=20,pady=20)

tbEntryb=Entry(win,width=60)
tbEntryb.grid(row=3,column=9,padx=20,pady=20)


label4msg=Label(win,text="ENGLISH",fg="black")
label4msg.grid(row=4,column=8,padx=20,pady=20)

tbEntryc=Entry(win,width=60)
tbEntryc.grid(row=4,column=9,padx=20,pady=20)



label5msg=Label(win,text="MATHS",fg="black")
label5msg.grid(row=5,column=8,padx=20,pady=20)

tbEntryd=Entry(win,width=60)
tbEntryd.grid(row=5,column=9,padx=20,pady=20)

label6msg=Label(win,text="SCIENCE",fg="black")
label6msg.grid(row=6,column=8,padx=20,pady=20)

tbEntrye=Entry(win,width=60)
tbEntrye.grid(row=6,column=9,padx=20,pady=20)


label6msg=Label(win,text="SOCIAL SCIENCE",fg="black")
label6msg.grid(row=7,column=8,padx=40,pady=40)

tbEntryf=Entry(win,width=60)
tbEntryf.grid(row=7 ,column=9,padx=40,pady=40)

Buttonadd=Button(win,text="insert",command=insertvalues,fg="black")
Buttonadd.grid(row=11,column=12)

Buttonadd=Button(win,text="update",command=updatevalue,fg="black")
Buttonadd.grid(row=11,column=13)

Buttonadd=Button(win,text="delete",command=deletevalue,fg="black")
Buttonadd.grid(row=11,column=14)

Buttonadd=Button(win,text="reset",fg="black")
Buttonadd.grid(row=11,column=15)


Buttonadd=Button(win,text="submit",fg="black")
Buttonadd.grid(row=11,column=16)













win.mainloop()

