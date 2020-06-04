from tkinter import *

window = Tk()
window.title('Addition')
window.geometry('500x500')

try:

    lbl0 = Label(window,text = "Enter choice : ",font = ("Arial Bold",20))
    lbl0.grid(column = 0,row = 0)

    txt0 = Entry(window,width = 10)
    txt0.grid(column = 1,row = 0)
    txt0.focus()


    def entered():
        if txt0.get() == 'add' :
            lbl1 = Label(window,text = "  A : ",font = ("Arial Bold" , 20))
            lbl1.grid(column = 0,row = 2)

            txt1 = Entry(window,width = 10)
            txt1.grid(column = 1,row = 2)
            txt1.focus()

            lbl2 = Label(window,text = "  B : ",font = ("Arial Bold",20))
            lbl2.grid(column = 0,row = 4)

            txt2 = Entry(window,width = 10)
            txt2.grid(column = 1,row = 4)

            lbl3 = Label(window,text = " Answer = ",font = ("Arial Bold",20))
            lbl3.grid(column = 0,row = 6)

            lbl4 = Label(window,font = ("Arial Bold",20))
            lbl4.grid(column = 1,row = 6)

            def add():
                res = int(txt1.get()) + int(txt2.get())
                lbl4.configure(text = res)  

            btn = Button(window,text = "ADD",font = ("Arial Bold",10),activebackground = 'gray',command = add)
            btn.grid(column = 1,row = 8)

        elif txt0.get() == 'sub':
            lbl1 = Label(window,text = "  A : ",font = ("Arial Bold" , 20))
            lbl1.grid(column = 0,row = 2)

            txt1 = Entry(window,width = 10)
            txt1.grid(column = 1,row = 2)
            txt1.focus()

            lbl2 = Label(window,text = "  B : ",font = ("Arial Bold",20))
            lbl2.grid(column = 0,row = 4)

            txt2 = Entry(window,width = 10)
            txt2.grid(column = 1,row = 4)

            lbl3 = Label(window,text = " Answer = ",font = ("Arial Bold",20))
            lbl3.grid(column = 0,row = 6)

            lbl4 = Label(window,font = ("Arial Bold",20))
            lbl4.grid(column = 1,row = 6)

            def sub():
                res = int(txt1.get()) - int(txt2.get())
                lbl4.configure(text = res)  

            btn = Button(window,text = "Sub",font = ("Arial Bold",10),activebackground = 'gray',command = sub)
            btn.grid(column = 1,row = 8)

        elif txt0.get() == 'mul':
            lbl1 = Label(window,text = "  A : ",font = ("Arial Bold" , 20))
            lbl1.grid(column = 0,row = 2)

            txt1 = Entry(window,width = 10)
            txt1.grid(column = 1,row = 2)
            txt1.focus()

            lbl2 = Label(window,text = "  B : ",font = ("Arial Bold",20))
            lbl2.grid(column = 0,row = 4)

            txt2 = Entry(window,width = 10)
            txt2.grid(column = 1,row = 4)

            lbl3 = Label(window,text = " Answer = ",font = ("Arial Bold",20))
            lbl3.grid(column = 0,row = 6)

            lbl4 = Label(window,font = ("Arial Bold",20))
            lbl4.grid(column = 1,row = 6)

            def mul():
                res = int(txt1.get()) * int(txt2.get())
                lbl4.configure(text = res)  

            btn = Button(window,text = "MUL",font = ("Arial Bold",10),activebackground = 'gray',command = mul)
            btn.grid(column = 1,row = 8)
            
        elif txt0.get() == 'div':
            lbl1 = Label(window,text = "  A : ",font = ("Arial Bold" , 20))
            lbl1.grid(column = 0,row = 2)

            txt1 = Entry(window,width = 10)
            txt1.grid(column = 1,row = 2)
            txt1.focus()

            lbl2 = Label(window,text = "  B : ",font = ("Arial Bold",20))
            lbl2.grid(column = 0,row = 4)

            txt2 = Entry(window,width = 10)
            txt2.grid(column = 1,row = 4)

            lbl3 = Label(window,text = " Answer = ",font = ("Arial Bold",20))
            lbl3.grid(column = 0,row = 6)

            lbl4 = Label(window,font = ("Arial Bold",20))
            lbl4.grid(column = 1,row = 6)

            def div():
                if float(txt2.get()) == 0:
                    lbl4.configure(text = "Infinity")
                else:
                    res = float(txt1.get()) / float(txt2.get())
                    lbl4.configure(text = res)

            btn = Button(window,text = "DIV",font = ("Arial Bold",10),activebackground = 'gray',command = div)
            btn.grid(column = 1,row = 8)

        else:
            l = Label(window,text = ' Sorry!\nInvelid Choice ',font = ('Arial Bold',10))
            l.grid(column = 1,row = 2)
                    


    btn0 = Button(window,text = " Enter ",activebackground = 'gray',command = entered)
    btn0.grid(column = 3,row = 0)

    
except ValueError as Argument:
    print("You must have to enter any two integer.",Argument)

window.mainloop()
