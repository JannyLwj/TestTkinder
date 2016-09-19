from tkinter import*

#打印输入的字符
def enterFunc(textVar_login, textVar_password):
    print(textVar_login.get())
    print(textVar_password.get())

#创建横条型框架
def iFrame(root, side):
    storeObj=Frame(root,borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj

#Enter按钮响应事件
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

        #welcome label
        welcome = iFrame(self, TOP)
        welcome_lable=Label(welcome,text='Welcome', bg='blue', fg='red')
        welcome_lable.pack(side = TOP,expand = YES,fill = BOTH)

        #创建用户名输入框
        login_frame=iFrame(self, TOP)
        lable = Label(login_frame, text='User Name:', justify=LEFT)
        lable.pack(side = LEFT,expand = YES,fill = BOTH)
        text = Entry(login_frame, textvariable=textVar_login, justify=LEFT)
        text.focus_set()
        text.bind('<Key-Return>', callback)
        text.pack(side = RIGHT,expand = YES,fill = BOTH)

        # 创建密码输入框
        password_fram=iFrame(self, TOP)
        lable = Label(password_fram, text='Password:', justify=LEFT)
        lable.pack(side = LEFT,expand = YES,fill = BOTH)
        text = Entry(password_fram, textvariable=textVar_password, justify=LEFT)
        text.focus_set()
        text.bind('<Key-Return>', callback)
        text.pack(side = RIGHT,expand = YES,fill = BOTH)

        # 创建Enter按钮，获得用户名密码
        entryButton=iFrame(self, TOP)
        button = Button(entryButton, text='Enter', command=lambda: enterFunc(textVar_login, textVar_password))
        button.pack(side = BOTTOM,expand = YES,fill = BOTH)


if __name__=='__main__':
    login().mainloop()