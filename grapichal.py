from tkinter import *
from threading import Thread
import time
root = Tk()

label_knife_amount_text = StringVar()
label_kps_text = StringVar()
label_price_wood_armor_text = StringVar()

amount_knives = 1000
kps = 0
price_wood_armor = 100

label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))
label_kps_text.set('Kps: ' + str(kps))
label_price_wood_armor_text.set('Costs: ' + str(price_wood_armor) + ' knives \n Grants 0.2 kps')

def scrollclick(event):
    print("You scroll-cliked me")
def leftclick(event):
    click()

def kps_func():
    global kps
    global amount_knives
    while True:
        time.sleep(1)
        amount_knives += kps
        amount_knives = round(amount_knives, 1)
        label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))


def rightclick(event):
    print("You right-clicked me")

def click():
    global amount_knives
    amount_knives += 1
    label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))
def woodarmor(event):
    global amount_knives
    global kps
    global price_wood_armor
    if amount_knives >= price_wood_armor:
        amount_knives -= price_wood_armor
        kps += 0.2
        price_wood_armor += round(price_wood_armor/12)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))
    label_price_wood_armor_text.set('Costs: ' + str(price_wood_armor) + ' knives \n Grants 0.2 kps')


t1 = Thread(target=kps_func)
t1.start()
box = Frame(root, width=400, height=200)
box.grid(row=3, column=3)


photo_knife = PhotoImage(file="Vampire_Knives.png")
label_photo_knife = Label(root, image=photo_knife)
label_photo_knife.bind("<Button-1>", leftclick)
label_photo_knife.grid(row=0, column=3)

photo_wood_armor = PhotoImage(file="wood_armor.png")
label_photo_wood_armor = Label(root, image=photo_wood_armor)
label_photo_wood_armor.bind("<Button-1>", woodarmor)
label_photo_wood_armor.grid(row=1, column=0)

label_amount = Label(textvariable = label_knife_amount_text)
label_price_wood_armor = Label(textvariable = label_price_wood_armor_text)
label_kps = Label(textvariable = label_kps_text)


label_amount.grid(row=1, column=3)
label_kps.grid(row=2, column=3)
label_price_wood_armor.grid(row=2, column=0)
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




