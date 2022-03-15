from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('Calculator')
root.geometry('220x273')
root.resizable(False, False)
root.iconbitmap("icon.ico")

btnFont = Font(size=14)

screen = Entry(root,width=35)
screen.grid(row=0,column=0,columnspan=4)

def btnFunc(a):
    screen.insert(END,a)

def cFunc():
    screen.delete(0,END)

def equals():
    x = screen.get()
    result = eval(x)
    screen.delete(0,END)
    screen.insert(0,result)

button_c = Button(root,text="C",padx=31,pady=7,font=btnFont,command=cFunc)
button_per = Button(root,text="%",padx=7,pady=7,font=btnFont,command=lambda:btnFunc("%"))
button_div = Button(root,text="/",padx=31,pady=7,font=btnFont,command=lambda:btnFunc("/"))
button_c.grid(row=1,column=0,columnspan=2)
button_per.grid(row=1,column=2)
button_div.grid(row=1,column=3)

button_7 = Button(root,text="7",padx=10,pady=7,font=btnFont,command=lambda:btnFunc("7"))
button_8 = Button(root,text="8",padx=10,pady=7,font=btnFont,command=lambda:btnFunc("8"))
button_9 = Button(root,text="9",padx=10,pady=7,font=btnFont,command=lambda:btnFunc("9"))
button_X = Button(root,text="X",padx=27,pady=7,font=btnFont,command=lambda:btnFunc("*"))
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_X.grid(row=2,column=3)

button_4 = Button(root,text="4",padx=10,pady=7,font=btnFont,command=lambda:btnFunc("4"))
button_5 = Button(root,text="5",padx=10,pady=7,font=btnFont,command=lambda:btnFunc("5"))
button_6 = Button(root,text="6",padx=10,pady=7,font=btnFont,command=lambda:btnFunc("6"))
button_sub = Button(root,text="-",padx=31,pady=7,font=btnFont,command=lambda:btnFunc("-"))
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_sub.grid(row=3,column=3)

button_1 = Button(root,text="1",padx=10,pady=7,font=btnFont,command=lambda:btnFunc("1"))
button_2 = Button(root,text="2",padx=10,pady=7,font=btnFont,command=lambda:btnFunc("2"))
button_3 = Button(root,text="3",padx=10,pady=7,font=btnFont,command=lambda:btnFunc("3"))
button_add = Button(root,text="+",padx=28,pady=7,font=btnFont,command=lambda:btnFunc("+"))
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_add.grid(row=4,column=3)

button_0 = Button(root,text="0",padx=10,pady=7,font=btnFont,command=lambda:btnFunc("0"))
button_dec = Button(root,text=".",padx=13,pady=7,font=btnFont,command=lambda:btnFunc("."))
button_equ = Button(root,text="=",padx=53,pady=7,font=btnFont,command=equals)
button_0.grid(row=5,column=0)
button_dec.grid(row=5,column=1)
button_equ.grid(row=5,column=2,columnspan=2)


root.mainloop()