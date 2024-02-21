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
    database="a"

    )
    return dbcon
#print5("connected to database at",dbcon)
#dbcon1=my DBconnecton()
#print("connected to database through outside of def at",dbcon1)

def insertvalue():
    name=tbEntrya.get()
    Tamil=tbEntryb.get()
    English=tbEntryc.get()
    Maths=tbEntryd.get()
    Science=tbEntrye.get()
    Socialscience=tbEntryf.get()
    e_con=MyDBconnection()
    result=e_con.cursor
    statement="insertvalue into sri3_user_details(name,Tamil,English,,Maths,Science,Socialscience)values(%s,%s,%s,%s,%s,%s)"
    valuepass=(name,Tamil,English,Maths,Science,Socialscience)
    result.execute(statement,valuepass)
    e_con.commit()

    print(result.rowcount, " row inserted")
 
#def updatevalue():
   # name=tbEntrya.get()
    #Tamil=tbEntryb.get()
    #e_con=MyDBconnection()
    #result=e_con.cursor
    #statement="updatevalue into sri1_user_details(value1,value2)column(%s,%s)";
    #valuepass=(name,Tamil)
    #result.execute(statement,valuepass)
    #e_con.commit()
    #print(result.rowcount,"row insert")


#def deletevalue():
   # name=tbEntrya.get()
    #Tamil=tbEntryb.get()
   # e_con=MyDBconnection()
    #result=e_con.cursor
   # statement="deletevalue into sri1_user_details(value1,value2)column(%s,%s)";
   # valuepass=(name,Tamil)
    #result.execute(statement,valuepass)
   # e_con.commit()
   # print(result.rowcount,"row insert")









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

Buttonadd=Button(win,text="insert",command=insertvalue,fg="black")
Buttonadd.grid(row=11,column=12)

#Buttonadd=Button(win,text="update",command=updatevalue,fg="black")
#Buttonadd.grid(row=11,column=13)

#Buttonadd=Button(win,text="delete",command=deletevalue,fg="black")
#Buttonadd.grid(row=11,column=14)

#Buttonadd=Button(win,text="reset",fg="black")
#Buttonadd.grid(row=11,column=15)


#Buttonadd=Button(win,text="submit",fg="black")
#Buttonadd.grid(row=11,column=16)













win.mainloop()

