import tkinter
from tkinter import *

# Creating tkinter window with fixed geometry
root = Tk()
root.geometry('500x350')

# This will create a LabelFrame
label_frame = LabelFrame(root, text='this is a quiz')
label_frame.pack(expand='yes', fill='both')
label1 = Label(label_frame, text='1. What is the capital of greece?')
label1.place(x=0, y=5)
inputtxt1 = tkinter.Text(label_frame, height=1, width=10)
inputtxt1.place(x=0, y=35)
label2 = Label(label_frame, text='2. Who is the headmaster in Harry Potter and the Chamber of Secrets?')
label2.place(x=0, y=65)
inputtxt2 = tkinter.Text(label_frame, height=1, width=10)
inputtxt2.place(x=0, y=95)
label3 = Label(label_frame, text='3. What element has symbol of "Au"?')
label3.place(x=0, y=125)
inputtxt3 = tkinter.Text(label_frame, height=1, width=10)
inputtxt3.place(x=0, y=155)

def getResult():
    input = inputtxt1.get(1, 'end')


# def printInput():
#     inp = inputtxt.get(1.0, "end-1c")
#     lbl.config(text="Provided Input: " + inp)
#
#
# # TextBox Creation
# inputtxt = tk.Text(frame,
#                    height=5,
#                    width=20)
#
# inputtxt.pack()

# Button Creation
printButton = tkinter.Button(label_frame,
                        text="Print",
                        command=getResult())


# label2 = Label(label_frame, text='2. This is another Label.')
# label2.place(x=0, y=35)

# label3 = Label(label_frame,
#                text='3. We can add multiple\n    widgets in it.')
#
# label3.place(x=0, y=65)
root.mainloop()
