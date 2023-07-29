import tkinter
from tkinter import*

cal=Tk()
cal.title("Calculator")

label1=Label(cal,text='KK-99 Instruments',height=2,font=('algerian',12)).grid(row=1,column=1,columnspan=2)
label2=Label(cal,text='   ---------------------------------------------').grid(row=2,column=0,columnspan=4)
label3=Label(cal,text=' Input :- ',font=('algerian',12)).grid(row=3,column=0)
entry1=Entry(cal,font=('arial',20,'bold'),bd=15,insertwidth=4,width=22,bg="white",justify='right') 

#entry1 value of numbers entered
entry1.grid(row=4,rowspan=3,pady=5,ipady=10,columnspan=4)
label4=Label(cal,text=' Output :- ',font=('algerian',12)).grid(row=7,column=0,pady=6)
#entry2=Entry(cal,font=('arial',20,'bold'),bd=15,insertwidth=4,width=22,bg="white",justify='right')
#entry2.grid(row=8,rowspan=3,pady=5,ipady=10,columnspan=4)

# defining functions
def btn7():
    #a=float(entry1.get())
    #b=Label(cal,text=a).grid(row=9,column=1)
    b=Label(cal,font=('arial',20,'bold'),text='7',width=22,bg="white",justify='right')
    b.grid(row=8,rowspan=3,pady=5,ipady=10,columnspan=4,column=0)
def btn8():
    #a=float(entry1.get())
    #b=Label(cal,text=a).grid(row=9,column=1)
    b=Label(cal,font=('arial',20,'bold'),text='8',width=22,bg="white",justify='right')
    b.grid(row=8,rowspan=3,pady=5,ipady=10,columnspan=4,column=0)   

def calc_equal():
    eq2=int((entry1.get()))
    equal1=sum("",eq2)
    b=Label(cal,font=('arial',20,'bold'),text=equal1,width=22,bg="white",justify='right')
     
#numerical buttons

btn7=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="7",bg="yellow",command=btn7).grid(row=13,pady=8,column=0)
btn8=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="8",bg="blue",command=btn8).grid(row=13,pady=5,column=1)
btn9=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="9",bg="yellow").grid(row=13,pady=5,column=2)
btn4=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="4",bg="lightgreen").grid(row=14,pady=5,column=0)
btn5=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="5",bg="red").grid(row=14,pady=5,column=1)
btn6=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="6",bg="lightgreen").grid(row=14,pady=5,column=2)
btn1=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="1",bg="yellow").grid(row=15,pady=5,column=0)
btn2=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="2",bg="blue").grid(row=15,pady=5,column=1)
btn3=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="3",bg="yellow").grid(row=15,pady=5,column=2)
btn0=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="0",bg="red").grid(row=16,pady=5,column=0)
btnpoint=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text=".",bg="yellow").grid(row=16,pady=5,column=1)

# mathematical operation buttons

Add=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="+",bg="lightgrey").grid(row=13,column=3)
Sub=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="-",bg="lightgrey").grid(row=14,column=3)
mul=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="x",bg="lightgrey").grid(row=15,column=3)
div=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="፥",bg="lightgrey").grid(row=16,column=3)
equal=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="=",bg="red",command=calc_equal).grid(row=16,column=2)
clear=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="C",bg="lightgrey").grid(row=17,column=0)
clear_all=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="AC",bg="lightgrey").grid(row=17,column=1)
cal.geometry("363x580")
cal.resizable(False,False)
cal.mainloop()
