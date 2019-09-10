from tkinter import *


root = Tk() 
root.title("Face Recognition")
root.geometry('500x600')
root.configure(background = 'beige')

label = Label(root, text = "Image", bg = 'beige')
label.grid(row=1, column =1)
entry = Entry(root, bg='white', font=10)
entry.grid(row =1,column=2)

text = Label(root, text="File")
text.grid(row=2, column =1)

theentry = Entry(root, bg='white', font=10)
theentry.grid(row =2,column=2)

button = Button(root, text ="Upload")
button.grid(row = 2, column = 3)


root.mainloop()