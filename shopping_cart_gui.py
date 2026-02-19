import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import dict_methods
import dict_methods_test
import dict_methods_test_data



# main window
main_window = tk.Tk()
main_window.geometry("400x400")
main_window.title("Fruit and Vegetable Database")

# content frames
produce_frame = Frame()
produce_frame.pack(side=TOP, padx=10, pady=5, anchor="w")
button_frame = Frame()
button_frame.pack(side=BOTTOM, pady=5, fill=X)

# images
apple = ImageTk.PhotoImage(Image.open("Week 3/images/apple.png"))
banana = ImageTk.PhotoImage(Image.open("Week 3/images/banana.png"))
carrot = ImageTk.PhotoImage(Image.open("Week 3/images/carrot.png"))
corn = ImageTk.PhotoImage(Image.open("Week 3/images/corn.png"))
grape = ImageTk.PhotoImage(Image.open("Week 3/images/grape.png"))
tomato = ImageTk.PhotoImage(Image.open("Week 3/images/tomato.png"))

# produce images
apple_img = Label(produce_frame, image=apple).grid(row=0,column=0,sticky=W,pady=2)
banana_img = tk.Label(produce_frame,image=banana).grid(row=1,column=0,sticky=W,pady=2)
carrot_img = tk.Label(produce_frame,image=carrot).grid(row=2,column=0,sticky=W,pady=2)
corn_img = tk.Label(produce_frame,image=corn).grid(row=3,column=0,sticky=W,pady=2)
grape_img = tk.Label(produce_frame,image=grape).grid(row=4,column=0,sticky=W,pady=2)
tomato_img = tk.Label(produce_frame,image=tomato).grid(row=5,column=0,sticky=W,pady=2)

# produce labels
Label(produce_frame, text="Apple", font=("arial", 20)).grid(row=0,column=1, padx=10)
Label(produce_frame, text="Banana", font=("arial", 20)).grid(row=1,column=1,padx=10)
Label(produce_frame, text="Carrot", font=("arial", 20)).grid(row=2,column=1,padx=10)
Label(produce_frame, text="Corn", font=("arial", 20)).grid(row=3,column=1,padx=10)
Label(produce_frame, text="Grapes", font=("arial", 20)).grid(row=4,column=1,padx=10)
Label(produce_frame, text="Tomato", font=("arial", 20)).grid(row=5,column=1,padx=10)

# produce entry boxes
apple_text = Entry(produce_frame, width=10).grid(row=0, column=2, padx=10)
banana_text = Entry(produce_frame, width=10).grid(row=1, column=2, padx=10)
carrot_text = Entry(produce_frame, width=10).grid(row=2, column=2, padx=10)
corn_text = Entry(produce_frame, width=10).grid(row=3, column=2, padx=10)
grape_text = Entry(produce_frame, width=10).grid(row=4, column=2, padx=10)
tomato_text = Entry(produce_frame, width=10).grid(row=5, column=2, padx=10)


def close_press():
    main_window.destroy()


#buttons
main_menu_button = Button(button_frame, text="Main Menu").pack(side=LEFT, padx=10)
confirm_button = Button(button_frame, text="Confirm Purchase").pack(side=RIGHT, padx=10)

quit_button = tk.Button(button_frame, text="Quit", command=close_press)
quit_button.pack(side=RIGHT, padx=10)




# start loop
main_window.mainloop()