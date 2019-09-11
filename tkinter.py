from tkinter import *

def compare():
    image = image_entry.get()
    folder = folder_entry.get()
    print("Image: {} Folder: {}".format(image, folder))

root = Tk() 
root.title("Face Recognition")
root.geometry('500x600')
root.configure(background = 'beige')

image_label = Label(root, text = "Image", bg = 'beige')
image_label.grid(row=1, column =1)
image_entry = Entry(root, bg='white', font=10)
image_entry.grid(row =1,column=2)

folder_label = Label(root, text="File", bg='beige')
folder_label.grid(row=2, column =1)
folder_entry = Entry(root, bg='white', font=10)
folder_entry.grid(row =2,column=2)

upload_button = Button(root, text ="Upload", command=lambda: compare())
upload_button.grid(row = 2, column = 3)


root.mainloop()