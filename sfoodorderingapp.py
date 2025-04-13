from tkinter import *
# from tkinter.ttk import *
import tkinter.font as f
import tkinter.messagebox
import random

price = 0
mainquantity = 0

root = Tk()
root.geometry("900x600")
root.title("Food Ordering App")

def value_selected():
    global mainquantity, mainfood
    mainquantity = mainfoodamount.get()

def main_selected():
    global mainquantity, mainfood
    mainfood = mainfoodchoice.get()

def foodcalculation():
    global mainquantity, mainfood, price
    if mainfood == "Chicken Sandwich":
        price = 10
    elif mainfood == "Veg Sandwich":
        price = 7
    elif mainfood == "None":
        price = 0
    
    mainfoodtotalprice = int(price) * int(mainquantity)
    print(mainfoodtotalprice)

label1 = Label(root, text="Email: ", font = ("Arial", 15))
label1.place(x=10, y=10)
emailentry = Entry(root, width=40)
emailentry.place(x=60, y=10)

label2 = Label(root, text="Password: ", font = ("Arial", 15))
label2.place(x=10, y=50)
passentry = Entry(root, width=40)
passentry.place(x=90, y=50)

mainfood = Label(root, text= "What food would you like: Chiken Sandwich, Veg Sandwich, or None?", font = ("Arial", 20))
mainfood.place(x=20, y = 90)
mainfoodchoice = Spinbox(root, values = ("Chicken Sandwich", "Veg Sandwich", "None"))
mainfoodchoice.place(x=300, y=130)
mainfoodamount = Spinbox(root, from_ = 1, to = 10, state = "readonly")
mainfoodamount.place(x=10, y=130)

beverage = Label(root, text= "What beverage would you like: Cola, Fanta, Sprite, Orange Juice, Water, or None?", font = ("Arial", 20))
beverage.place(x=20, y = 220)
maindrinkchoice = Spinbox(root, values = ("Cola", "Fanta", "Sprite", "Orange juice", "Water", "None"))
maindrinkchoice.place(x=300, y=260)
maindrinkamount = Spinbox(root, from_ = 1, to = 10, state = "readonly")
maindrinkamount.place(x=10, y=260)

desert = Label(root, text= "What desert would you like: Ice Cream, Ice Lolly, Chocolate Cake, Red Velvet Cake, or None?", font = ("Arial", 20))
desert.place(x=20, y = 350)
maindrinkchoice = Spinbox(root, values = ("Ice Cream", "Ice Lolly", "Chocolate Cake", "Red Velvet Cake",  "None"))
maindrinkchoice.place(x=300, y=390)
maindrinkamount = Spinbox(root, from_ = 1, to = 10, state = "readonly")
maindrinkamount.place(x=10, y=390)

submit= Button(root, text="Sumbit", font=("Arial", 15), command = foodcalculation)
submit.place(x=400, y = 500)
root.mainloop()