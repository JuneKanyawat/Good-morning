from tkinter import *

t = Tk()
t.title("Conversion :)")
t.geometry("500x500")


def con():
    t1=int(a.get())
    sum=t1*2.20462262185
    s1 = str(t1)+"  กิโลกรัม = "+str(sum)+" ปอนด์"
    Label(t,text=s1,fg="black",font=20).pack()

def con2():
    t2=int(b.get())
    sum=t2/2.20462262185
    s1 = str(t2)+" ปอนด์ = "+str(sum)+" กิโลกรัม"
    Label(t,text=s1,fg="black",font=20).pack()


Label(t,text="kilogram - pound",fg="black",font=20).pack()
Label(t,text="kilogram",fg="black",font=20).pack()
a=Entry(t, width=20)
a.pack()
button1 = Button(t,text="convert",fg="black",command=con).pack()
Label(t,text="pound",fg="black",font=20).pack()
b=Entry(t, width=20)
b.pack()
button2 = Button(t,text="convert",fg="black",command=con2).pack()
    

t.mainloop()