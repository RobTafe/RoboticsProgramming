import tkinter as tk
from tkinter.ttk import Label
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import dict_methods

# sample data
shop_cart = {"Apple": 3, "Banana": 1, "Raspberry": 10}
new_items = []

# new window to confirm payment
def open_sort_window(to_be_sorted):
    # reset button state from main window
    confirm_button.config(state="disabled")
    add_to_cart_button.config(state="active")

    # creates window and frame
    sort_window = tk.Toplevel(main_window)
    sort_window.title("Shopping Checkout")
    top_frame = Frame(sort_window)
    top_frame.pack(side="top", padx=5, pady=5)
    Label(top_frame, text="Your Cart", font=("Arial",25)).pack(padx=80)

    # sorts cart into alphabetical order
    sorted_list = dict_methods.sort_entries(to_be_sorted)
    for entry in sorted_list.items():
        Label(top_frame, text=f"{entry[0]}, {entry[1]}").pack(padx=10, pady=5)

    # opens messagebox from confirm order button
    def confirmed():
        result = tk.messagebox.askyesno("Thank you!", "Return to store?", parent=sort_window)
        if not result:
            main_window.destroy() # closes app
        else:
            sort_window.destroy() # returns to main window

    Button(top_frame, text="Confirm Payment", command=confirmed).pack(pady=5)

# main window settings
main_window = tk.Tk()
main_window.title("Shopping App")
left_frame = Frame(main_window)
left_frame.pack(side="left", padx=(10,5), pady=5)
mid_frame = Frame(main_window)
mid_frame.pack(side="left", anchor="n", padx=(10, 5), pady=5)
right_frame = Frame(main_window)
right_frame.pack(side="right", anchor="n", padx=(5, 10), pady=5)

# change
path = "/home/robert/Desktop/VSCENV/Week 3/Images/"

# add images of produce
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

produce_images = [apple,avocado,banana,broccoli,carrot,corn,grape,juice,kiwi,
               melon,milk,orange,pear,raspberry,tomato,yoghurt]
produce_names = ['Apple','Avocado','Banana','Broccoli','Carrot','Corn','Grape','Juice','Kiwi','Melon',
           'Milk','Orange','Pear','Raspberry','Tomato','Yoghurt']

# display all items in the full cart
def show_shopping_cart():
    r = 1
    for key, num in shop_cart.items():
        Label(right_frame, text="Shopping Cart", font=("arial", 25)).grid(row=0, columnspan=True, pady=10)
        (Label(right_frame, borderwidth=2, border=2, text=key, font=("arial", 15))
         .grid(row=r, column=0, padx=10,sticky="w"))
        Label(right_frame, text=num, font=("arial", 15)).grid(row=r, column=1, sticky="n")
        r += 1

# add item to new items list
def add_to_cart(name):
    new_items.append(name)

Label(mid_frame, text="New Items", font=("Arial",25)).pack(pady=10)
Label(left_frame, text="Produce", font=("arial",25)).grid(row=0, columnspan=2, pady=10)

# creation of produce button array
row = 1
column = 0
index = 0
# make listbox
selected_produce = Listbox(mid_frame)
selected_produce.pack(padx=5)

for item in produce_names:
    def action(x = item):
        selected_produce.insert(END, x) # inserts item into listbox
        add_to_cart_button.config(state="active") # activates button
        return add_to_cart(x) # sends name of produce to listbox
    (Button(left_frame, width=150, height=50, text=item, image=produce_images[index], compound="left", command=action)
     .grid(row=row, column=column,sticky="w"))
    row += 1
    if row == 9:
        row = 1
        column += 1
    index += 1

show_shopping_cart()

# opens sort window
confirm_button = Button(right_frame, anchor="s", text="Confirm Order", command=lambda: open_sort_window(shop_cart))
confirm_button.grid(row=99)
confirm_button.config(state="disabled")

# adds items from new item listbox
def add_items():
    if len(new_items) != 0:
        dict_methods.add_item(shop_cart,new_items)
        add_to_cart_button.config(state="disabled")
        confirm_button.config(state="active")
        new_items.clear()
        show_shopping_cart()
        selected_produce.delete(0,"end")
    else:
        tk.messagebox.showerror("No new items","You must select items to proceed",parent=main_window)

add_to_cart_button = Button(mid_frame, text="Add to cart",command=add_items)
add_to_cart_button.pack(anchor="s")

main_window.mainloop()
