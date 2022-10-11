# GUI - Graphical User Interface


# Libraries
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk

app=ttk.Tk()
app.title('my app')
app.geometry('600x400')

msg=ttk.Variable(app)
# print(msg.get())
# msg.set('empty')
# print(msg.get())

ttk.Label(app,text='A simple text Label').place(x=10,y=10)
ttk.Label(app,textvariable=msg).place(x=40,y=40)

def abc():
    
    msg.set('jo tera mn')
ttk.Button(app,text='isko click krdo',command=abc).place(x=100,y=150)
ttk.Button(app,text='ye wala bhi h',font=('Arial',22),command= lambda:msg.set('pta nhi')).place(x=50,y=150)

f1=ttk.Variable(app)
f1.set('0')
f2=ttk.Variable(app)
f2.set('0')
result=ttk.Variable(app)

ttk.Entry(app, textvariable=f1, font=('Arial',22)).place(x=100,y=100)
ttk.Entry(app, textvariable=f2, font=('Arial',22)).place(x=80,y=200)
ttk.Label(app,text='Result').place(x=300,y=300)
ttk.Label(app,textvariable=result,font=('Arial,22')).place(x=300,y=350)


def calci(op):
    print('I will calculate')
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app,text='+',command=lambda:calci('+'),font=('Arial',22)).place(x=50,y=260)
ttk.Button(app,text='-',command=lambda:calci('-'),font=('Arial',22)).place(x=100,y=260)
ttk.Button(app,text='*',command=lambda:calci('*'),font=('Arial',22)).place(x=150,y=260)
ttk.Button(app,text='/',command=lambda:calci('/'),font=('Arial',22)).place(x=200,y=260)





box =ttk.Listbox(app,height=5,fg='red',activestyle='dotbox')
box.insert(1,'sample1')
box.insert(2,'sample2')
box.insert(3,'sample3')
box.place(x=400,y=40)

def show():

    print(box.get(box.curselection()))

ttk.Button(app,text='show',command=show).place(x=300,y=350)
app.mainloop()
