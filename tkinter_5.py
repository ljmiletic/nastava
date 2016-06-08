#Tkinter _  Button
from tkinter import *
def prikaz():
    print("Ime:%s\nPrezime:%s"%(e1.get(),e2.get()))
    
mGui=Tk()
#mGui.geometry("150x150+200+200")
mGui.title("Unos podataka")
Label(mGui,text="Ime").grid(row=0)
Label(mGui,text="Prezime").grid(row=1)
e1=Entry(mGui)
e2=Entry(mGui)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
Button(mGui,text='Kraj',command=mGui.destroy).grid(row=3,column=0,sticky=W,pady=4)
Button(mGui,text='Prikazi',command=prikaz).grid(row=3,column=1,sticky=W,pady=4)
mGui.mainloop()


              
