import tkinter
from tkinter import*
import tkinter as tk
from tkinter import ttk

root=Tk()
root.title(" AI-Project ")

#rectangle measure
text1=Label(root,text=" Rectangle measure",height=2,bg='yellow').grid(row=1,column=2,columnspan=2)

length_text=Label(root,text=' Enter length :- ',height=3).grid(row=2,column=1)
length_box=Entry(root,width=10)
length_box.grid(row=2,column=2)

breadth_text=Label(root,text=' Enter breadth :- ',height=3).grid(row=2,column=3)
breadth_box=Entry(root,width=10)
breadth_box.grid(row=2,column=4)
print(length_box.get())
def area():
    x=float(length_box.get())          # how to get the value of number entered in Entry box
    y=float(breadth_box.get())
    a=ttk.Label(root,text='Area = ').grid(row=5,column=2)
    b=ttk.Label(root,text=x*y).grid(row=5,column=3)

def perimeter():
    x=float(length_box.get())
    y=float(breadth_box.get())
    c=ttk.Label(root,text='Perimeter = ').grid(row=5,column=2)
    d=ttk.Label(root,text=2*(x+y)).grid(row=5,column=3)
                           
buton=Button(root,text='Area',command=area,bg='lightgreen').grid(row=3,column=1)
button=Button(root,text='Perimeter',command=perimeter,bg='lightgreen').grid(row=3,column=3)

msg1=Label(root,text=' Output :- ',height=3,background='lightblue').grid(row=5,column=1)
line=Label(root,text='---------------------------------------------------------------------',height=2)
line.grid(row=6,column=1,columnspan=4)

#mile to kilometer converter
text2=Label(root,text=" Mile - Kilometer converter",height=2,bg='yellow').grid(row=7,column=2,columnspan=2)
distance=Label(root,text=' Enter distance :- ',height=3).grid(row=8,column=2)
dis_box=Entry(root,width=10)
dis_box.grid(row=8,column=3)

def mile_to_km():
    i=float(dis_box.get())
    j=ttk.Label(root,text=i*0.6213712,background='yellow').grid(row=10,column=2)
    k=ttk.Label(root,text=' km ',background='yellow').grid(row=10,column=3)

def km_to_mile():
    i=float(dis_box.get())
    j=ttk.Label(root,text=i*1.609344,background='yellow').grid(row=10,column=2)
    k=ttk.Label(root,text=' mile ',background='yellow').grid(row=10,column=3)

button1=button=Button(root,text='kilometer to mile',command=mile_to_km,bg='lightgreen').grid(row=9,column=3,columnspan=2)
button2=button=Button(root,text='mile to kilometer',command=km_to_mile,bg='lightgreen').grid(row=9,column=1,columnspan=2)

msg2=Label(root,text=' Output :- ',height=3,background='lightblue').grid(row=10,column=1)

line1=Label(root,text='-------------------------------------------------------------------')
line1.grid(row=11,column=1,columnspan=4)
cred1=Label(root,text=' CREDITS -- ',height=3).grid(row=15,column=1)
cred2=Label(root,text=' LICENSE ').grid(row=15,column=2)
cred3=Label(root,text=' - opensource ').grid(row=15,column=3)
cred4=Label(root,text=' DEVELOPER ').grid(row=16,column=2)
cred5=Label(root,text=' - Kunal Kashyap ').grid(row=16,column=3)

root.resizable(False,False)
root.geometry("450x500")
root.mainloop()