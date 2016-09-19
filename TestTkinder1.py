from tkinter import*

def enterFunc(textVar_login, textVar_password):
    print(textVar_login.get())
    print(textVar_password.get())

def iFrame(root, side):
    storeObj=Frame(root,borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj

def callback(event):
    global textVar_login
    global textVar_password
    print(textVar_login.get())
    print(textVar_password.get())


class login(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Login in')

        textVar_login=StringVar()
        textVar_password = StringVar()

        welcome = iFrame(self, TOP)
        welcome_lable=Label(welcome,text='Welcome', bg='blue', fg='red')
        welcome_lable.pack(side = TOP,expand = YES,fill = BOTH)

        for i in ["1", "2"]:
            frame=iFrame(self, TOP)
            if i=="1":
                lable = Label(frame, text='User Name:', justify=LEFT)
                lable.pack(side = LEFT,expand = YES,fill = BOTH)
                text = Entry(frame, textvariable=textVar_login, justify=LEFT)
                text.focus_set()
                text.bind('<Key-Return>', callback)
                text.pack(side = RIGHT,expand = YES,fill = BOTH)
            else:
                lable = Label(frame, text='Password:', justify=LEFT)
                lable.pack(side = LEFT,expand = YES,fill = BOTH)
                text = Entry(frame, textvariable=textVar_password, justify=LEFT)
                text.focus_set()
                text.bind('<Key-Return>', callback)
                text.pack(side = RIGHT,expand = YES,fill = BOTH)

        entryButton=iFrame(self, TOP)
        button = Button(entryButton, text='Enter', command=lambda: enterFunc(textVar_login, textVar_password))
        button.pack(side = BOTTOM,expand = YES,fill = BOTH)


if __name__=='__main__':
    login().mainloop()