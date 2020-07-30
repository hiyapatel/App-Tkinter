from tkinter import *

root = Tk()
root.minsize(500,350)
root.maxsize(500,350)
a,b,c = 0,0,0
def get():
    global a,b,c
    a = int(e1.get())
    b = int(e2.get())
    c = int(e3.get())

def cal():
    global b,c
    get()
    if b>=150000:
        b=150000
    if c>=50000:
        c=50000
    x = a-b-c
    if x<=250000:
        y = 0
    elif x<=500000:
        y = ((x-250000)*5)/100
    elif x<=100000:
        y = ((250000*5)+((x-500000)*20))/100
    else:
        y = ((250000*5)+(500000*20)+((x-1000000)*30))/100
    s4.set(str(x))
    s5.set(str(y))

def res():
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")

l = Label(root, text = 'Tax Calculator',font =("Times New Roman",26,"bold"),height=2,width=40,bg="light blue").pack(side=TOP)

l1 = Label(root, text="Total Income     :",fg="Blue",font =("Times New Roman",11)).place(x=125,y=100)
s1 = StringVar()
e1 = Entry(root,textvariable=s1,width=25)
e1.place(x=260,y=100)

l2 = Label(root, text="Investment 80C     :",fg="blue",font =("Times New Roman",11)).place(x=110,y=130)
s2 = StringVar()
e2 = Entry(root,textvariable=s2,width=25)
e2.place(x=260,y=130)

l3 = Label(root, text="Investment 80CCD     :",fg="blue",font =("Times New Roman",11)).place(x=89,y=160)
s3 = StringVar()
e3 = Entry(root,textvariable=s3,width=25)
e3.place(x=260,y=160)

l4 = Label(root, text="Net Taxable Income     :",font =("Times New Roman",11)).place(x=81,y=190)
s4 = StringVar()
e4 = Entry(root,textvariable=s4,width=25)
e4.place(x=260,y=190)

l5 = Label(root, text="Basic Tax      :",font =("Times New Roman",11)).place(x=138,y=220)
s5 = StringVar()
e5 = Entry(root,textvariable=s5,width=25)
e5.place(x=260,y=220)

b1 = Button(root,text="Calculate",width=7,command=cal).place(x=215,y=260)
b2 = Button(root,text="Reset",width=7,command=res).place(x=215,y=300)

root.mainloop()