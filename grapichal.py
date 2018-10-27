from tkinter import *
import time
amount_knives = 0
root = Tk()
def scrollclick(event):
    print("You scroll-cliked me")
def leftclick(event):
    global amount_knives
    print("You left-clicked me")
    amount_knives += 1

def rightclick(event):
    print("You right-clicked me")

box = Frame(root, width=800, height=600)
photo = PhotoImage(file="Vampire_Knives.png")
label_photo = Label(root, image=photo)
label_amount = Label(root, text="Total amount of knifes: "+str(amount_knives))
label_photo.bind("<Button-1>", leftclick)
label_photo.grid(row=0, column=3)
box.grid(row=3, column=3)
#label_photo.grid(column=3)
while True:
    label_amount = Label(root, text="Total amount of knifes: " + str(amount_knives))
    label_amount.grid(row=2, column=3)
    root.mainloop()
    time.sleep(0.1)







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




