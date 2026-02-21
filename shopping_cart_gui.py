import tkinter as tk
from tkinter.ttk import Label
from tkinter import *
from PIL import Image, ImageTk
import dict_methods_test_data
import dict_methods



# Done
def open_add_window():
    new_window = tk.Toplevel(main_window)
    new_window.title("Add To Cart")
    Label(new_window, text="Add items to shopping cart", font=("Arial", 25)).pack(pady=10,padx=10)
    left_frame = Frame(new_window)
    left_frame.pack(side="left", padx=(10,5), pady=5)

    mid_frame = Frame(new_window)
    mid_frame.pack(side="left", padx=5, pady=5)

    right_frame = Frame(new_window)
    right_frame.pack(side="left", padx=(5,10), pady=5)

    Label(left_frame, text="Current Cart").pack()
    Label(mid_frame, text="Items to Add").pack()
    Label(right_frame, text="New Cart").pack()

    current_cart_list = dict_methods_test_data.add_item_inputs
    new_cart_list = dict_methods_test_data.add_item_outputs

    for row in current_cart_list:
        cart = row[0]
        items = row[1]
        new_items = tk.Variable(value=items)
        cart_listbox = Listbox(left_frame)
        cart_listbox.pack(pady=5)
        for key in cart:
            cart_listbox.insert(END, '{}: {}'.format(key,cart[key]))
        Listbox(mid_frame, listvariable=new_items).pack(pady=5)

    for item in new_cart_list:
        cart = item
        new_cart = Listbox(right_frame)
        new_cart.pack(pady=5)
        for key in cart:
            new_cart.insert(END, '{}: {}'.format(key, cart[key]))

def open_read_window():
    new_window = tk.Toplevel(main_window)
    new_window.title("Read notes")
    Label(new_window, text="Create user cart from an iterable notes entry").pack(pady=10, padx=10)

    left_frame = Frame(new_window)
    left_frame.pack(side="left", padx=(10, 5), pady=5)

    right_frame = Frame(new_window)
    right_frame.pack(side="right", padx=(5, 10), pady=5)

    Label(left_frame, text="Customer Notes").pack()
    Label(right_frame, text="Shopping Cart").pack()

    notes_list = dict_methods_test_data.read_notes_inputs
    cart_list = dict_methods_test_data.read_notes_outputs

    for row in notes_list:
        items = row
        new_items = tk.Variable(value=items)
        Listbox(left_frame, listvariable=new_items).pack(pady=5)

    for item in cart_list:
        cart = item
        new_cart = Listbox(right_frame)
        new_cart.pack(pady=5)
        for key in cart:
            new_cart.insert(END, '{}: {}'.format(key, cart[key]))

# Needs fixing
def open_update_window():
    new_window = tk.Toplevel(main_window)
    new_window.title("Update Recipies")
    Label(new_window, text="Update the recipe ideas dictionary").pack(pady=10, padx=10)

    left_frame = Frame(new_window)
    left_frame.pack(side="left", padx=(10, 5), pady=5)

    mid_frame = Frame(new_window)
    mid_frame.pack(side="left", padx=5, pady=5)

    right_frame = Frame(new_window)
    right_frame.pack(side="left", padx=(5, 10), pady=5)

    Label(left_frame, text="Current Cart").pack()
    Label(mid_frame, text="Items to Add").pack()
    Label(right_frame, text="New Cart").pack()

    current_cart_list = dict_methods_test_data.update_recipes_inputs
    new_cart_list = dict_methods_test_data.update_recipes_outputs

    for row in current_cart_list:
        cart = row[0]
        items = row[1]
        new_items = tk.Variable(value=items)
        cart_listbox = Listbox(left_frame)
        cart_listbox.pack(pady=5)
        for key in cart:
            cart_listbox.insert(END, '{}: {}'.format(key, cart[key]))
        Listbox(mid_frame, listvariable=new_items).pack(pady=5)

    for item in new_cart_list:
        cart = item
        new_cart = Listbox(right_frame)
        new_cart.pack(pady=5)
        for key in cart:
            new_cart.insert(END, '{}: {}'.format(key, cart[key]))
# Done
def open_sort_window():
    new_window = tk.Toplevel(main_window)
    new_window.title("Sort Cart")
    Label(new_window, text="Combine users order to store aisle").pack(pady=10, padx=10)

    left_frame = Frame(new_window)
    left_frame.pack(side="left", padx=(10, 5), pady=5)

    right_frame = Frame(new_window)
    right_frame.pack(side="left", padx=(5, 10), pady=5)

    Label(left_frame, text="Current Cart").pack()
    Label(right_frame, text="Sorted Cart").pack()

    current_cart_list = dict_methods_test_data.sort_entries_inputs
    new_cart_list = dict_methods_test_data.sort_entries_outputs

    for row in current_cart_list:
        cart = row
        cart_listbox = Listbox(left_frame)
        cart_listbox.pack(pady=5)
        for key in cart:
            cart_listbox.insert(END, '{}: {}'.format(key, cart[key]))


    for item in new_cart_list:
        cart = item
        new_cart = Listbox(right_frame)
        new_cart.pack(pady=5)
        for key in cart:
            new_cart.insert(END, '{}: {}'.format(key, cart[key]))

# Rest Needs fixing
def open_send_window():
    new_window = tk.Toplevel(main_window)
    new_window.title("Send to Store")
    Label(new_window, text="Update store inventory levels").pack(pady=10, padx=10)

    left_frame = Frame(new_window)
    left_frame.pack(side="left", padx=(10, 5), pady=5)

    mid_frame = Frame(new_window)
    mid_frame.pack(side="left", padx=5, pady=5)

    right_frame = Frame(new_window)
    right_frame.pack(side="left", padx=(5, 10), pady=5)

    Label(left_frame, text="Current Cart").pack()
    Label(mid_frame, text="Items to Add").pack()
    Label(right_frame, text="New Cart").pack()

    current_cart_list = dict_methods_test_data.send_to_store_inputs
    new_cart_list = dict_methods_test_data.send_to_store_outputs

    for row in current_cart_list:
        cart = row[0]
        items = row[1]
        new_items = tk.Variable(value=items)
        cart_listbox = Listbox(left_frame)
        cart_listbox.pack(pady=5)
        for key in cart:
            cart_listbox.insert(END, '{}: {}'.format(key, cart[key]))
        Listbox(mid_frame, listvariable=new_items).pack(pady=5)

    for item in new_cart_list:
        cart = item
        new_cart = Listbox(right_frame)
        new_cart.pack(pady=5)
        for key in cart:
            new_cart.insert(END, '{}: {}'.format(key, cart[key]))

def open_inventory_window():
    new_window = tk.Toplevel(main_window)
    new_window.title("Update Inventory")
    Label(new_window, text="Add items to shopping cart").pack(pady=10, padx=10)

    left_frame = Frame(new_window)
    left_frame.pack(side="left", padx=(10, 5), pady=5)

    mid_frame = Frame(new_window)
    mid_frame.pack(side="left", padx=5, pady=5)

    right_frame = Frame(new_window)
    right_frame.pack(side="left", padx=(5, 10), pady=5)

    Label(left_frame, text="Current Cart").pack()
    Label(mid_frame, text="Items to Add").pack()
    Label(right_frame, text="New Cart").pack()

    current_cart_list = dict_methods_test_data.update_store_inventory_inputs
    new_cart_list = dict_methods_test_data.update_store_inventory_outputs

    for row in current_cart_list:
        cart = row[0]
        items = row[1]
        new_items = tk.Variable(value=items)
        cart_listbox = Listbox(left_frame)
        cart_listbox.pack(pady=5)
        for key in cart:
            cart_listbox.insert(END, '{}: {}'.format(key, cart[key]))
        Listbox(mid_frame, listvariable=new_items).pack(pady=5)

    for item in new_cart_list:
        cart = item
        new_cart = Listbox(right_frame)
        new_cart.pack(pady=5)
        for key in cart:
            new_cart.insert(END, '{}: {}'.format(key, cart[key]))

main_window = tk.Tk()
main_window.title("Main")
Label(text="Select Exercise to View", font=("Arial", 25)).grid(row=0, padx=10,pady=10)
add_button = tk.Button(main_window, text="Add Items", command=open_add_window)
add_button.grid(row=1, pady=5, padx=10)
read_button = tk.Button(main_window, text="Read Cart", command=open_read_window)
read_button.grid(row=2, pady=5, padx=10)
update_button = tk.Button(main_window, text="Update Recipies", command=open_update_window)
update_button.grid(row=3, pady=5, padx=10)
sort_button = tk.Button(main_window, text="Sort Cart", command=open_sort_window)
sort_button.grid(row=4, pady=5, padx=10)
send_button = tk.Button(main_window, text="Send Order", command=open_send_window)
send_button.grid(row=5, pady=5, padx=10)
inventory_button = tk.Button(main_window, text="Update Inventory", command=open_inventory_window)
inventory_button.grid(row=6, pady=5, padx=10)
quit_button = tk.Button(main_window, text="Close", command=main_window.destroy)
quit_button.grid(row=7, pady=(15,5), padx=10)

path = "/home/robert/Desktop/VSCENV/Week 3/Images/"

apple = ImageTk.PhotoImage(Image.open(path + "apple.png"))
avocado = ImageTk.PhotoImage(Image.open(path + "avocado.png"))
banana = ImageTk.PhotoImage(Image.open(path + "banana.png"))
blueberry = ImageTk.PhotoImage(Image.open(path + "blueberry.png"))
broccoli = ImageTk.PhotoImage(Image.open(path + "broccoli.png"))
carrot = ImageTk.PhotoImage(Image.open(path + "carrot.png"))
corn = ImageTk.PhotoImage(Image.open(path + "corn.png"))
grape = ImageTk.PhotoImage(Image.open(path + "grape.png"))
juice = ImageTk.PhotoImage(Image.open(path + "juice.png"))
kiwi = ImageTk.PhotoImage(Image.open(path + "kiwi.png"))
melon = ImageTk.PhotoImage(Image.open(path + "melon.png"))
milk = ImageTk.PhotoImage(Image.open(path + "milk.png"))
orange = ImageTk.PhotoImage(Image.open(path + "orange.png"))
pear = ImageTk.PhotoImage(Image.open(path + "pear.png"))
raspberry = ImageTk.PhotoImage(Image.open(path + "raspberry.png"))
tomato = ImageTk.PhotoImage(Image.open(path + "tomato.png"))
yoghurt = ImageTk.PhotoImage(Image.open(path + "yoghurt.png"))

produce_img = [apple,avocado,banana,broccoli,carrot,corn,grape,juice,kiwi,
               melon,milk,orange,pear,raspberry,tomato,yoghurt]
produce_txt = ['apple','avocado','banana','broccoli','carrot','corn','grape','juice','kiwi','melon',
           'milk','orange','pear','raspberry','tomato','yoghurt']

main_window.mainloop()
