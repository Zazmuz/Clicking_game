# Importing
from tkinter import *
from threading import Thread
import time
import random
import winsound

# Making the main program "root"
root = Tk()

# Telling all the armor text labels that they are in fact text labels
label_knife_amount_text = StringVar()
label_kps_text = StringVar()
label_price_wood_armor_text = StringVar()
label_price_shadow_armor_text = StringVar()
label_price_molten_armor_text = StringVar()
label_price_yellow_hardmode_armor_text = StringVar()
label_price_pink_hardmode_armor_text = StringVar()
label_price_grey_hardmode_armor_text = StringVar()
label_price_hallowed_armor_text = StringVar()
label_price_chlorophyte_armor_text = StringVar()
label_price_turtle_armor_text = StringVar()
label_price_beetle_armor_text = StringVar()
label_price_solar_flare_armor_text = StringVar()

# Telling all the upgrade text labels that they are in fact text labels
label_price_putrid_scent_upgrade_text = StringVar()

# Main starting variables
amount_knives = 0
kps = 0
click_power = 1
critical_chance = 4

# Kps values
kps_wood_armor = 0.2
kps_shadow_armor = 1
kps_molten_armor = 3
kps_yellow_hardmode_armor = 18
kps_pink_hardmode_armor = 32
kps_grey_hardmode_armor = 2530
kps_hallowed_armor = 370
kps_chlorophyte_armor = 600
kps_turtle_armor = 2800
kps_beetle_armor = 9000
kps_solar_flare_armor = 900000

# Armor pricing
price_wood_armor = 150
price_shadow_armor = 550
price_molten_armor = 1100
price_yellow_hardmode_armor = 5000
price_pink_hardmode_armor = 8000
price_grey_hardmode_armor = 50000
price_hallowed_armor = 100000
price_chlorophyte_armor = 200000
price_turtle_armor = 500000
price_beetle_armor = 1000000
price_solar_flare_armor = 1000000000

# Upgrade pricing
price_putrid_scent_upgrade = 10000

# Telling all the armor text labels what to display
label_kps_text.set('Kps: ' + str(kps))
label_knife_amount_text.set('Knives: ' + str(amount_knives))
label_price_wood_armor_text.set(
    'Costs: ' + str(price_wood_armor) + ' knives \n Grants: ' + str(kps_wood_armor) + ' kps')
label_price_shadow_armor_text.set(
    'Costs: ' + str(price_shadow_armor) + ' knives \n Grants: ' + str(kps_shadow_armor) + ' kps')
label_price_molten_armor_text.set(
    'Costs: ' + str(price_molten_armor) + ' knives \n Grants: ' + str(kps_molten_armor) + ' kps')
label_price_yellow_hardmode_armor_text.set(
    'Costs: ' + str(price_yellow_hardmode_armor) + ' knives \n Grants: ' + str(kps_yellow_hardmode_armor) + ' kps')
label_price_pink_hardmode_armor_text.set(
    'Costs: ' + str(price_pink_hardmode_armor) + ' knives \n Grants: ' + str(kps_pink_hardmode_armor) + ' kps')
label_price_grey_hardmode_armor_text.set(
    'Costs: ' + str(price_grey_hardmode_armor) + ' knives \n Grants: ' + str(kps_grey_hardmode_armor) + ' kps')
label_price_hallowed_armor_text.set(
    'Costs: ' + str(price_hallowed_armor) + ' knives \n Grants: ' + str(kps_hallowed_armor) + ' kps')
label_price_chlorophyte_armor_text.set(
    'Costs: ' + str(price_chlorophyte_armor) + ' knives \n Grants: ' + str(kps_chlorophyte_armor) + ' kps')
label_price_turtle_armor_text.set(
    'Costs: ' + str(price_turtle_armor) + ' knives \n Grants: ' + str(kps_turtle_armor) + ' kps')
label_price_beetle_armor_text.set(
    'Costs: ' + str(price_beetle_armor) + ' knives \n Grants: ' + str(kps_beetle_armor) + ' kps')
label_price_solar_flare_armor_text.set(
    'Costs: ' + str(price_solar_flare_armor) + ' knives \n Grants: ' + str(kps_solar_flare_armor) + ' kps')

# Telling all the upgrade text labels what to display
label_price_putrid_scent_upgrade_text.set('Costs: ' + str(price_putrid_scent_upgrade) + ' knives \n Grants a 5% \nextra chance to hit a critical\nand 5 extra click power')

# Defining some functions
def kps_func():
    global kps
    global amount_knives
    while True:
        time.sleep(1)
        amount_knives += kps
        amount_knives = round(amount_knives, 1)
        label_knife_amount_text.set('Knives: ' + str(amount_knives))


def click(event):
    global amount_knives
    global click_power
    global critical_chance
    critical = random.randint(0,100)
    if critical < critical_chance:
        amount_knives += click_power*2
        label_knife_amount_text.set('Knives: ' + str(amount_knives))
        winsound.PlaySound('click_critical.wav', winsound.SND_ASYNC)

    else:
        amount_knives += click_power
        label_knife_amount_text.set('Knives: ' + str(amount_knives))
        winsound.PlaySound("click.wav", winsound.SND_ASYNC)



def save():
    # 1: Amount of knives
    # 2: Kps
    # 3: Prices top from bottom
    #
    #
    #
    #
    Var_save = [price_wood_armor, price_shadow_armor, price_molten_armor, price_yellow_hardmode_armor,
                   price_pink_hardmode_armor, price_grey_hardmode_armor, price_hallowed_armor, price_chlorophyte_armor, price_turtle_armor, price_beetle_armor, price_solar_flare_armor, critical_chance]

    savefile = open("SaveFile.txt", "w+")
    savefile.write(str(amount_knives) + "\n" + str(kps))
    savefile = open("SaveFile.txt", "a")
    for saves in Var_save:
        savefile.write("\n" + str(saves))


def load():
    global amount_knives
    global kps
    global price_wood_armor
    global price_shadow_armor
    global price_molten_armor
    global price_yellow_hardmode_armor
    global price_pink_hardmode_armor
    global price_grey_hardmode_armor
    global price_hallowed_armor
    global price_chlorophyte_armor
    global price_turtle_armor
    global price_beetle_armor
    global price_solar_flare_armor
    global price_putrid_scent_upgrade
    global critical_chance

    savefile = open("SaveFile.txt", "r")
    inside_save_file = savefile.readlines()
    amount_knives = float(inside_save_file[0][:-1])
    kps = float(inside_save_file[1][:-1])
    price_wood_armor = float(inside_save_file[2][:-1])
    price_shadow_armor = float(inside_save_file[3][:-1])
    price_molten_armor = float(inside_save_file[4][:-1])
    price_yellow_hardmode_armor = float(inside_save_file[5][:-1])
    price_pink_hardmode_armor = float(inside_save_file[6][:-1])
    price_grey_hardmode_armor = float(inside_save_file[7][:-1])
    price_hallowed_armor = float(inside_save_file[8][:-1])
    price_chlorophyte_armor = float(inside_save_file[9][:-1])
    price_turtle_armor = float(inside_save_file[10][:-1])
    price_beetle_armor = float(inside_save_file[11][:-1])
    price_solar_flare_armor = float(inside_save_file[12][:-1])
    critical_chance = float(inside_save_file[13])

    label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_wood_armor_text.set(
        'Costs: ' + str(price_wood_armor) + ' knives \n Grants: ' + str(kps_wood_armor) + ' kps')
    label_price_shadow_armor_text.set(
        'Costs: ' + str(price_shadow_armor) + ' knives \n Grants: ' + str(kps_shadow_armor) + ' kps')
    label_price_molten_armor_text.set(
        'Costs: ' + str(price_molten_armor) + ' knives \n Grants: ' + str(kps_molten_armor) + ' kps')
    label_price_yellow_hardmode_armor_text.set(
        'Costs: ' + str(price_yellow_hardmode_armor) + ' knives \n Grants: ' + str(kps_yellow_hardmode_armor) + ' kps')
    label_price_pink_hardmode_armor_text.set(
        'Costs: ' + str(price_pink_hardmode_armor) + ' knives \n Grants: ' + str(kps_pink_hardmode_armor) + ' kps')
    label_price_grey_hardmode_armor_text.set(
        'Costs: ' + str(price_grey_hardmode_armor) + ' knives \n Grants: ' + str(kps_grey_hardmode_armor) + ' kps')
    label_price_hallowed_armor_text.set(
        'Costs: ' + str(price_hallowed_armor) + ' knives \n Grants: ' + str(kps_hallowed_armor) + ' kps')
    label_price_chlorophyte_armor_text.set(
        'Costs: ' + str(price_chlorophyte_armor) + ' knives \n Grants: ' + str(kps_chlorophyte_armor) + ' kps')
    label_price_turtle_armor_text.set(
        'Costs: ' + str(price_turtle_armor) + ' knives \n Grants: ' + str(kps_turtle_armor) + ' kps')
    label_price_beetle_armor_text.set(
        'Costs: ' + str(price_beetle_armor) + ' knives \n Grants: ' + str(kps_beetle_armor) + ' kps')
    label_price_solar_flare_armor_text.set(
        'Costs: ' + str(price_solar_flare_armor) + ' knives \n Grants: ' + str(kps_solar_flare_armor) + ' kps')

# Adding save and load buttons and adding them to the grid
save_button = Button(root, text="Save", command=save)
load_button = Button(root, text="Load", command=load)
save_button.grid(row=5, column=3)
load_button.grid(row=6, column=3)

# Defining all the armor funcions
def woodarmor(event):
    global amount_knives
    global kps
    global price_wood_armor
    if amount_knives >= price_wood_armor:
        amount_knives -= round(price_wood_armor, 1)
        kps += kps_wood_armor
        price_wood_armor += round(price_wood_armor / 10)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_wood_armor_text.set(
        'Costs: ' + str(price_wood_armor) + ' knives \n Grants: ' + str(kps_wood_armor) + ' kps')


def shadowarmor(event):
    global amount_knives
    global kps
    global price_shadow_armor
    if amount_knives >= price_shadow_armor:
        amount_knives -= round(price_shadow_armor, 1)
        kps += kps_shadow_armor
        price_shadow_armor += round(price_shadow_armor / 14)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_shadow_armor_text.set(
        'Costs: ' + str(price_shadow_armor) + ' knives \n Grants: ' + str(kps_shadow_armor) + ' kps')


def moltenarmor(event):
    global amount_knives
    global kps
    global price_molten_armor
    if amount_knives >= price_molten_armor:
        amount_knives -= round(price_molten_armor, 1)
        kps += kps_molten_armor
        price_molten_armor += round(price_molten_armor / 12)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_molten_armor_text.set(
        'Costs: ' + str(price_molten_armor) + ' knives \n Grants: ' + str(kps_molten_armor) + ' kps')


def yellowhardmodearmor(event):
    global amount_knives
    global kps
    global price_yellow_hardmode_armor
    if amount_knives >= price_yellow_hardmode_armor:
        amount_knives -= round(price_yellow_hardmode_armor, 1)
        kps += kps_yellow_hardmode_armor
        price_yellow_hardmode_armor += round(price_yellow_hardmode_armor / 14)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_yellow_hardmode_armor_text.set(
        'Costs: ' + str(price_yellow_hardmode_armor) + ' knives \n Grants: ' + str(kps_yellow_hardmode_armor) + ' kps')


def pinkhardmodearmor(event):
    global amount_knives
    global kps
    global price_pink_hardmode_armor
    if amount_knives >= price_pink_hardmode_armor:
        amount_knives -= round(price_pink_hardmode_armor, 1)
        kps += kps_pink_hardmode_armor
        price_pink_hardmode_armor += round(price_pink_hardmode_armor / 12)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_pink_hardmode_armor_text.set(
        'Costs: ' + str(price_pink_hardmode_armor) + ' knives \n Grants: ' + str(kps_pink_hardmode_armor) + ' kps')


def greyhardmodearmor(event):
    global amount_knives
    global kps
    global price_grey_hardmode_armor
    if amount_knives >= price_grey_hardmode_armor:
        amount_knives -= round(price_grey_hardmode_armor, 1)
        kps += kps_grey_hardmode_armor
        price_grey_hardmode_armor += round(price_grey_hardmode_armor / 10)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_grey_hardmode_armor_text.set(
        'Costs: ' + str(price_grey_hardmode_armor) + ' knives \n Grants: ' + str(kps_grey_hardmode_armor) + ' kps')

def hallowedarmor(event):
    global amount_knives
    global kps
    global price_hallowed_armor
    if amount_knives >= price_hallowed_armor:
        amount_knives -= round(price_hallowed_armor, 1)
        kps += kps_hallowed_armor
        price_hallowed_armor += round(price_hallowed_armor / 14)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_hallowed_armor_text.set(
        'Costs: ' + str(price_hallowed_armor) + ' knives \n Grants: ' + str(kps_hallowed_armor) + ' kps')

def chlorophytearmor(event):
    global amount_knives
    global kps
    global price_chlorophyte_armor
    if amount_knives >= price_chlorophyte_armor:
        amount_knives -= round(price_chlorophyte_armor, 1)
        kps += kps_chlorophyte_armor
        price_chlorophyte_armor += round(price_chlorophyte_armor / 6)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_chlorophyte_armor_text.set(
        'Costs: ' + str(price_chlorophyte_armor) + ' knives \n Grants: ' + str(kps_chlorophyte_armor) + ' kps')

def turtlearmor(event):
    global amount_knives
    global kps
    global price_turtle_armor
    if amount_knives >= price_turtle_armor:
        amount_knives -= round(price_turtle_armor, 1)
        kps += kps_turtle_armor
        price_turtle_armor += round(price_turtle_armor / 8)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_turtle_armor_text.set(
        'Costs: ' + str(price_turtle_armor) + ' knives \n Grants: ' + str(kps_turtle_armor) + ' kps')

def beetlearmor(event):
    global amount_knives
    global kps
    global price_beetle_armor
    if amount_knives >= price_beetle_armor:
        amount_knives -= round(price_beetle_armor, 1)
        kps += kps_beetle_armor
        price_beetle_armor += round(price_beetle_armor / 15)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_beetle_armor_text.set(
        'Costs: ' + str(price_beetle_armor) + ' knives \n Grants: ' + str(kps_beetle_armor) + ' kps')

def solarflarearmor(event):
    global amount_knives
    global kps
    global price_solar_flare_armor
    if amount_knives >= price_solar_flare_armor:
        amount_knives -= round(price_solar_flare_armor, 1)
        kps += kps_solar_flare_armor
        price_solar_flare_armor += round(price_solar_flare_armor / 15)
        kps = round(kps, 1)
        label_kps_text.set('Kps: ' + str(kps))
    label_knife_amount_text.set('Knives: ' + str(amount_knives))
    label_price_solar_flare_armor_text.set(
        'Costs: ' + str(price_solar_flare_armor) + ' knives \n Grants: ' + str(kps_solar_flare_armor) + ' kps')

def putridscent(event):
    global critical_chance
    global amount_knives
    global price_putrid_scent_upgrade
    global click_power
    if amount_knives >= price_putrid_scent_upgrade:
        amount_knives -= round(price_putrid_scent_upgrade, 1)
        critical_chance += 5
        click_power += 5
        price_putrid_scent_upgrade *= 10
        label_knife_amount_text.set('Knives: ' + str(amount_knives))
        label_price_putrid_scent_upgrade_text.set(
            'Costs: ' + str(price_putrid_scent_upgrade) + ' knives \n Grants a 4% \nextra chance to hit a critical')


# Starting the kps "thread" aka extra function running 24/7
t1 = Thread(target=kps_func)
t1.daemon = True
t1.start()


# Impoting armor-images to labels, binding them to left-mouseclick and importing them in a grid pattern
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

photo_hallowed_armor = PhotoImage(file="hallowed_armor.png")
label_photo_hallowed_armor = Label(root, image=photo_hallowed_armor)
label_photo_hallowed_armor.bind("<Button-1>", hallowedarmor)
label_photo_hallowed_armor.grid(row=7, column=0)

photo_chlorophyte_armor = PhotoImage(file="chlorophyte_armor.png")
label_photo_chlorophyte_armor = Label(root, image=photo_chlorophyte_armor)
label_photo_chlorophyte_armor.bind("<Button-1>", chlorophytearmor)
label_photo_chlorophyte_armor.grid(row=8, column=0)

photo_turtle_armor = PhotoImage(file="turtle_armor.png")
label_photo_turtle_armor = Label(root, image=photo_turtle_armor)
label_photo_turtle_armor.bind("<Button-1>", turtlearmor)
label_photo_turtle_armor.grid(row=9, column=0)

photo_beetle_armor = PhotoImage(file="beetle_armor.png")
label_photo_beetle_armor = Label(root, image=photo_beetle_armor)
label_photo_beetle_armor.bind("<Button-1>", beetlearmor)
label_photo_beetle_armor.grid(row=10, column=0)

photo_solar_flare_armor = PhotoImage(file="solar_flare_armor.png")
label_photo_solar_flare_armor = Label(root, image=photo_solar_flare_armor)
label_photo_solar_flare_armor.bind("<Button-1>", solarflarearmor)
label_photo_solar_flare_armor.grid(row=11, column=0)


# Impoting upgrade-images to labels, binding them to left-mouseclick and importing them in a grid pattern
photo_putrid_scent_upgrade = PhotoImage(file="putrid_scent.png")
label_photo_putrid_scent_upgrade = Label(root, image=photo_putrid_scent_upgrade)
label_photo_putrid_scent_upgrade.bind("<Button-1>", putridscent)
label_photo_putrid_scent_upgrade.grid(row=1, column=7)

# Defining the armor text labels
label_kps = Label(textvariable=label_kps_text)
label_amount = Label(textvariable=label_knife_amount_text)
label_price_wood_armor = Label(textvariable=label_price_wood_armor_text)
label_price_shadow_armor = Label(textvariable=label_price_shadow_armor_text)
label_price_molten_armor = Label(textvariable=label_price_molten_armor_text)
label_price_yellow_hardmode_armor = Label(textvariable=label_price_yellow_hardmode_armor_text)
label_price_pink_hardmode_armor = Label(textvariable=label_price_pink_hardmode_armor_text)
label_price_grey_hardmode_armor = Label(textvariable=label_price_grey_hardmode_armor_text)
label_price_hallowed_armor = Label(textvariable=label_price_hallowed_armor_text)
label_price_chlorophyte_armor = Label(textvariable=label_price_chlorophyte_armor_text)
label_price_turtle_armor = Label(textvariable=label_price_turtle_armor_text)
label_price_beetle_armor = Label(textvariable=label_price_beetle_armor_text)
label_price_solar_flare_armor = Label(textvariable=label_price_solar_flare_armor_text)


# Defining the upgrade text labels
label_price_putrid_scent_upgrade = Label(textvariable=label_price_putrid_scent_upgrade_text)

# Adding titles for armor and upgades
label_armor_sets = Label(root, text='ARMOR SETS')
label_armor_sets.grid(row=0, column=1)
label_upgrades = Label(root, text='UPGRADES')
label_upgrades.grid(row=0, column=8)


# Adding a small box to separate the amount of knives from the upgrades
upgrade_spliting_box = Frame(root, width=25)
upgrade_spliting_box.grid(row=1, column=4)



# Placing the armor text labels in a grid pattern
label_amount.grid(row=1, column=3)
label_kps.grid(row=2, column=3)
label_price_wood_armor.grid(row=1, column=1)
label_price_shadow_armor.grid(row=2, column=1)
label_price_molten_armor.grid(row=3, column=1)
label_price_yellow_hardmode_armor.grid(row=4, column=1)
label_price_pink_hardmode_armor.grid(row=5, column=1)
label_price_grey_hardmode_armor.grid(row=6, column=1)
label_price_hallowed_armor.grid(row=7, column=1)
label_price_chlorophyte_armor.grid(row=8, column=1)
label_price_turtle_armor.grid(row=9, column=1)
label_price_beetle_armor.grid(row=10, column=1)
label_price_solar_flare_armor.grid(row=11, column=1)

# Placing the upgrade text labels in a grid pattern
label_price_putrid_scent_upgrade.grid(row=1, column=8)

# Displaying everything on the screen
root.mainloop()
