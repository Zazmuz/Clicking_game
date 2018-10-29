# Importing
from tkinter import *
from threading import Thread
import time

# Making the main program "root"
root = Tk()

# Telling all the text labels that they are in fact text labels
label_knife_amount_text = StringVar()
label_kps_text = StringVar()
label_price_wood_armor_text = StringVar()
label_price_shadow_armor_text = StringVar()
label_price_molten_armor_text= StringVar()
label_price_yellow_hardmode_armor_text = StringVar()
label_price_pink_hardmode_armor_text = StringVar()
label_price_grey_hardmode_armor_text = StringVar()

# Main starting variables
amount_knives = 0
kps = 0
click_power = 1

# Kps values
kps_wood_armor = 0.2
kps_shadow_armor = 1
kps_molten_armor = 3
kps_yellow_hardmode_armor = 20
kps_pink_hardmode_armor = 35
kps_grey_hardmode_armor = 250

# Armor pricing
price_wood_armor = 100
price_shadow_armor = 500
price_molten_armor = 1000
price_yellow_hardmode_armor = 5000
price_pink_hardmode_armor = 8000
price_grey_hardmode_armor = 50000

# Telling all the text labels what to display
label_kps_text.set('Kps: ' + str(kps))
label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))
label_price_wood_armor_text.set('Costs: ' + str(price_wood_armor) + ' knives \n Grants: ' + str(kps_wood_armor) + ' kps')
label_price_shadow_armor_text.set('Costs: ' + str(price_shadow_armor) + ' knives \n Grants: ' + str(kps_shadow_armor) + ' kps')
label_price_molten_armor_text.set('Costs: ' + str(price_molten_armor) + ' knives \n Grants: ' + str(kps_molten_armor) + ' kps')
label_price_yellow_hardmode_armor_text.set('Costs: ' + str(price_yellow_hardmode_armor) + ' knives \n Grants: ' + str(kps_yellow_hardmode_armor) + ' kps')
label_price_pink_hardmode_armor_text.set('Costs: ' + str(price_pink_hardmode_armor) + ' knives \n Grants: ' + str(kps_pink_hardmode_armor) + ' kps')
label_price_grey_hardmode_armor_text.set('Costs: ' + str(price_grey_hardmode_armor) + ' knives \n Grants: ' + str(kps_grey_hardmode_armor) + ' kps')

# Defining some functions
def kps_func():
    global kps
    global amount_knives
    while True:
        time.sleep(1)
        amount_knives += kps
        amount_knives = round(amount_knives, 1)
        label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))

def click(event):
    global amount_knives
    global click_power
    amount_knives += click_power
    label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))

# Defining all the armor funcions
def woodarmor(event):
    global amount_knives
    global kps
    global price_wood_armor
    if amount_knives >= price_wood_armor:
        amount_knives -= price_wood_armor
        kps += kps_wood_armor
        price_wood_armor += round(price_wood_armor/12)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))
    label_price_wood_armor_text.set('Costs: ' + str(price_wood_armor) + ' knives \n Grants: ' + str(kps_wood_armor) + ' kps')

def shadowarmor(event):
    global amount_knives
    global kps
    global price_shadow_armor
    if amount_knives >= price_shadow_armor:
        amount_knives -= price_shadow_armor
        kps += kps_shadow_armor
        price_shadow_armor += round(price_shadow_armor/12)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))
    label_price_shadow_armor_text.set('Costs: ' + str(price_shadow_armor) + ' knives \n Grants: ' + str(kps_shadow_armor) + ' kps')

def moltenarmor(event):
    global amount_knives
    global kps
    global price_molten_armor
    if amount_knives >= price_molten_armor:
        amount_knives -= price_molten_armor
        kps += kps_molten_armor
        price_molten_armor += round(price_molten_armor/12)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))
    label_price_molten_armor_text.set('Costs: ' + str(price_molten_armor) + ' knives \n Grants: ' + str(kps_molten_armor) + ' kps')

def yellowhardmodearmor(event):
    global amount_knives
    global kps
    global price_yellow_hardmode_armor
    if amount_knives >= price_yellow_hardmode_armor:
        amount_knives -= price_yellow_hardmode_armor
        kps += kps_yellow_hardmode_armor
        price_yellow_hardmode_armor += round(price_yellow_hardmode_armor/12)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))
    label_price_yellow_hardmode_armor_text.set('Costs: ' + str(price_yellow_hardmode_armor) + ' knives \n Grants: ' + str(kps_yellow_hardmode_armor) + ' kps')

def pinkhardmodearmor(event):
    global amount_knives
    global kps
    global price_pink_hardmode_armor
    if amount_knives >= price_pink_hardmode_armor:
        amount_knives -= price_pink_hardmode_armor
        kps += kps_pink_hardmode_armor
        price_pink_hardmode_armor += round(price_pink_hardmode_armor/12)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))
    label_price_pink_hardmode_armor_text.set('Costs: ' + str(price_pink_hardmode_armor) + ' knives \n Grants: ' + str(kps_pink_hardmode_armor) + ' kps')

def greyhardmodearmor(event):
    global amount_knives
    global kps
    global price_grey_hardmode_armor
    if amount_knives >= price_grey_hardmode_armor:
        amount_knives -= price_grey_hardmode_armor
        kps += kps_grey_hardmode_armor
        price_grey_hardmode_armor += round(price_grey_hardmode_armor/12)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Total amount of knifes: ' + str(amount_knives))
    label_price_grey_hardmode_armor_text.set('Costs: ' + str(price_grey_hardmode_armor) + ' knives \n Grants: ' + str(kps_grey_hardmode_armor) + ' kps')

# Starting the kps "thread" aka extra running 24/7 func
t1 = Thread(target=kps_func)
t1.start()


# Impoting images to labels, binding them to left-mouseclick and importing them in a grid pattern
photo_knife = PhotoImage(file="Vampire_Knives.png")
label_photo_knife = Label(root, image=photo_knife)
label_photo_knife.bind("<Button-1>", click)
label_photo_knife.grid(row=0, column=3)

photo_wood_armor = PhotoImage(file="wood_armor.png")
label_photo_wood_armor = Label(root, image=photo_wood_armor)
label_photo_wood_armor.bind("<Button-1>", woodarmor)
label_photo_wood_armor.grid(row=1, column=0)

photo_shadow_armor = PhotoImage(file="shadow_armor.png")
label_photo_shadow_armor = Label(root, image=photo_shadow_armor)
label_photo_shadow_armor.bind("<Button-1>", shadowarmor)
label_photo_shadow_armor.grid(row=2, column=0)

photo_molten_armor = PhotoImage(file="molten_armor.png")
label_photo_molten_armor = Label(root, image=photo_molten_armor)
label_photo_molten_armor.bind("<Button-1>", moltenarmor)
label_photo_molten_armor.grid(row=3, column=0)

photo_yellow_hardmode_armor = PhotoImage(file="palladium_armor.png")
label_photo_yellow_hardmode_armor = Label(root, image=photo_yellow_hardmode_armor)
label_photo_yellow_hardmode_armor.bind("<Button-1>", yellowhardmodearmor)
label_photo_yellow_hardmode_armor.grid(row=4, column=0)

photo_pink_hardmode_armor = PhotoImage(file="orichalcum_armor.png")
label_photo_pink_hardmode_armor = Label(root, image=photo_pink_hardmode_armor)
label_photo_pink_hardmode_armor.bind("<Button-1>", pinkhardmodearmor)
label_photo_pink_hardmode_armor.grid(row=5, column=0)

photo_grey_hardmode_armor = PhotoImage(file="titanium_armor.png")
label_photo_grey_hardmode_armor = Label(root, image=photo_grey_hardmode_armor)
label_photo_grey_hardmode_armor.bind("<Button-1>", greyhardmodearmor)
label_photo_grey_hardmode_armor.grid(row=6, column=0)

# Defining the text labels
label_kps = Label(textvariable = label_kps_text)
label_amount = Label(textvariable = label_knife_amount_text)
label_price_wood_armor = Label(textvariable = label_price_wood_armor_text)
label_price_shadow_armor = Label(textvariable = label_price_shadow_armor_text)
label_price_molten_armor = Label(textvariable = label_price_molten_armor_text)
label_price_yellow_hardmode_armor = Label(textvariable = label_price_yellow_hardmode_armor_text)
label_price_pink_hardmode_armor = Label(textvariable = label_price_pink_hardmode_armor_text)
label_price_grey_hardmode_armor = Label(textvariable = label_price_grey_hardmode_armor_text)



# Placing the the text labels in a grid pattern
label_amount.grid(row=1, column=3)
label_kps.grid(row=2, column=3)
label_price_wood_armor.grid(row=1, column=1)
label_price_shadow_armor.grid(row=2, column=1)
label_price_molten_armor.grid(row=3, column=1)
label_price_yellow_hardmode_armor.grid(row=4, column=1)
label_price_pink_hardmode_armor.grid(row=5, column=1)
label_price_grey_hardmode_armor.grid(row=6, column=1)

# Displaying everything on the screen
root.mainloop()




