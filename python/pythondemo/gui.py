from tkinter import *
app =Tk()
app.title ("my first python gui app")
app.geometry("500x200+600+200")
#app.state("zoomed")
app.config(bg="sky blue")
lblTitle =Label(text="NAME") 
lblTitle.grid(row=0,columnspan=1,padx=40,pady=30); 

inputbox=Entry(app,width=12)
inputbox.grid(row=1,column=1);

app.mainloop()