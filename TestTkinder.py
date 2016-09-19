from tkinter import*

root = Tk()

def callback(event):
    print('click at', event.x, event.y)

def key(event):
    print('pressed', repr(event.char))

frame=Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()
frame.focus_set()
frame.bind("<Key>", key)
frame.pack()

if __name__=='__main__':

    root.mainloop()