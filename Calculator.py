from tkinter import *

root = Tk()
i = 0
root.minsize(125,180)
root.maxsize(125,180)
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM,pady=5)
s,c = "",0

def eq(a):
    global s
    s=s+a
    s1.set(s)

def eq1():
    global s,c
    b=len(s)
    if b==0:
        s="("
        c+=1
    elif (s[b-1]==")")&(c!=0):
        s+=")"
        c-=1
    elif s[b-1]=="(":
        s+="("
        c+=1
    elif (s[b-1]==")")&(c==0):
        s+="*("
        c+=1
    elif s[b-1] in "*/-+":
        s+="("
        c+=1
    elif s[b-1].isdigit():
        s+=")"
        c-=1
    s1.set(s)

def de():
    global s
    s = s[0:len(s)-1]
    s1.set(s)

def cl():
    global s
    s=""
    s1.set(s)

def ans():
    global s
    try:
        for i in range(len(s)):
            if s[i] == "%":
                s = s[0:i] + "/100"
        s1.set(eval(s))
    except:
        s1.set("Error")

l = Label(root, text="CALCULATOR",fg="green")
l.pack()

s1 = StringVar()
e1 = Entry(root,textvariable=s1)
e1.pack()

b1 = Button(bottomframe,text="C",width=3,bg='black', fg='white',command=lambda:cl()).grid(row=0, column=0)
b2 = Button(bottomframe,text="=",width=3,bg='black', fg='white',command=lambda:ans()).grid(row=0, column=1)
b3 = Button(bottomframe,text="<-",width=3,bg='black', fg='white',command=lambda:de()).grid(row=0, column=2)
b4 = Button(bottomframe,text="/",width=3,bg='black', fg='white',command=lambda:eq("/")).grid(row=0, column=3)
b5 = Button(bottomframe,text="7",width=3,bg='black', fg='white',command=lambda:eq("7")).grid(row=1, column=0)
b6 = Button(bottomframe,text="8",width=3,bg='black', fg='white',command=lambda:eq("8")).grid(row=1, column=1)
b7 = Button(bottomframe,text="9",width=3,bg='black', fg='white',command=lambda:eq("9")).grid(row=1, column=2)
b8 = Button(bottomframe,text="*",width=3,bg='black', fg='white',command=lambda:eq("*")).grid(row=1, column=3)
b9 = Button(bottomframe,text="4",width=3,bg='black', fg='white',command=lambda:eq("4")).grid(row=2, column=0)
b10 = Button(bottomframe,text="5",width=3,bg='black', fg='white',command=lambda:eq("5")).grid(row=2, column=1)
b11 = Button(bottomframe,text="6",width=3,bg='black', fg='white',command=lambda:eq("6")).grid(row=2, column=2)
b12 = Button(bottomframe,text="-",width=3,bg='black', fg='white',command=lambda:eq("-")).grid(row=2, column=3)
b13 = Button(bottomframe,text="1",width=3,bg='black', fg='white',command=lambda:eq("1")).grid(row=3, column=0)
b14 = Button(bottomframe,text="2",width=3,bg='black', fg='white',command=lambda:eq("2")).grid(row=3, column=1)
b15 = Button(bottomframe,text="3",width=3,bg='black', fg='white',command=lambda:eq("3")).grid(row=3, column=2)
b16 = Button(bottomframe,text="+",width=3,bg='black', fg='white',command=lambda:eq("+")).grid(row=3, column=3)
b17 = Button(bottomframe,text=".",width=3,bg='black', fg='white',command=lambda:eq(".")).grid(row=4, column=0)
b18 = Button(bottomframe,text="0",width=3,bg='black', fg='white',command=lambda:eq("0")).grid(row=4, column=1)
b19 = Button(bottomframe,text="%",width=3,bg='black', fg='white',command=lambda:eq("%")).grid(row=4, column=2)
b20 = Button(bottomframe,text="( )",width=3,bg='black', fg='white',command=lambda:eq1()).grid(row=4, column=3)

root.mainloop()