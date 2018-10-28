from tkinter import *
root = Tk()
label_text = StringVar()
amount_knives = 0
label_text.set('Total amount of knifes: ' + str(amount_knives))
def scrollclick(event):
    print("You scroll-cliked me")
def leftclick(event):
    global amount_knives
    click()


def rightclick(event):
    print("You right-clicked me")

def click():
    global amount_knives
    amount_knives += 1
    label_text.set('Total amount of knifes: ' + str(amount_knives))
def pre_bosses_melee_charachter:
    amount_knives


box = Frame(root, width=800, height=600)
photo = PhotoImage(file="Vampire_Knives.png")
label_photo = Label(root, image=photo)
label_amount = Label(textvariable = label_text)
label_photo.bind("<Button-1>", leftclick)
label_photo.grid(row=0, column=3)
box.grid(row=3, column=3)
label_photo.grid(column=3)
label_amount.grid(row=1, column=3)
root.mainloop()





# from tkinter import *
#
# root = Tk()
# test = StringVar()
# test.set('hello')
#
# label = Label(root, textvariable = test)
# label.pack()
#
# entry_box = Entry(root, textvariable = test)
# entry_box.pack()
#
# root.mainloop() # the window is now displayed




# username_box = Label(root, text="Username")
# password_box = Label(root, text="Password")
# username_entry = Entry(root)
# password_entry = Entry(root)
#
# username_box.grid(row=0, column=0)
# username_entry.grid(row=0, column=1)
#
# password_box.grid(row=1, column=0)
# password_entry.grid(row=1, column=1)
#
# check = Checkbutton(root, text="Remember me")
# check.grid(columnspan=2)




