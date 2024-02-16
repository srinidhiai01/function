from tkinter import *
app =Tk()
app.title ("my first python gui app")
app.geometry("500x200+600+200")
#app.state("zoomed")
app.config(bg="sky blue")
lblTitle =Label(app,text="Arithmatic operator") 
lblTitle.grid(row=0,column=1,padx=40,pady=30); 

inputbox1=Entry(app,width=12)
inputbox1.grid(row=0,column=2,padx=40,pady=20);

lblTitle1 =Label(app,text="Arithmatic operator") 
lblTitle1.grid(row=1,column=1,padx=40,pady=30); 

inputbox2=Entry(app,width=12)
inputbox2.grid(row=1,column=2,padx=40,pady=20);

clickme=Button(app,text="Addition")
clickme.grid(row=2,column=8,padx=40,pady=20);




app.mainloop()