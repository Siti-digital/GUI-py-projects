import tkinter
from tkinter import*

root=Tk()
root.title("Jump Game")

#lab3=Label(text='Jump',font=('algerian',15)).grid(row=1,padx=290,pady=5)
play=Button(root,text=' Play ',font=('algerian',13),bd=5,width=6,bg='lightblue').grid(row=2,pady=10,padx=25,column=1)
jump=Button(root,text=' Jump ',font=('algerian',13),bd=5,bg='yellow').grid(row=2,pady=5,column=2)
restart=Button(root,text='Restart',font=('algerian',13),bd=5,bg='lightblue').grid(row=4,pady=5,column=1)



#root.resizable(False,False)
root.geometry("730x550")
root.mainloop()