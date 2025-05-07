import tkinter as tk
import csv

global total_price


def read_snack_list_from_csv(filename):
    item_dict = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            item_name = row['Item Name']
            quantity = int(row['Quantity'])
            price = float(row['Price'])
            item_dict[item_name] = {'quantity': quantity, 'price': price}
    return item_dict
snack_dict = read_snack_list_from_csv('snack.csv')
lunch_dict = read_snack_list_from_csv('lunch.csv')
drink_dict = read_snack_list_from_csv('drink.csv')
item_dict={}
snack=list(snack_dict.keys())
lunch=list(lunch_dict.keys())
drink=list(drink_dict.keys())
item_dict.update(snack_dict)
item_dict.update(lunch_dict)
item_dict.update(drink_dict)
print(snack_dict)

cart_items = {}


root = tk.Tk()
root.geometry("1000x700")
root.title("Canteen order Menu")


buttons = {}


def slot1(s1Frame):
    for i, item in enumerate(snack):
        button = tk.Button(s1Frame, text=item, width=10, height=2, command=lambda item=item: add_to_cart(item, buttons[item],'snack.csv'))
        row = i // 5
        column = i % 5
        button.grid(row=row, column=column, padx=6, pady=6)
        buttons[item] = button

def slot2(s1Frame):
    for i, item in enumerate(lunch):
        button = tk.Button(s1Frame, text=item, width=10, height=2, command=lambda item=item: add_to_cart(item, buttons[item],'lunch.csv'))
        row = i // 5
        column = i % 5
        button.grid(row=row, column=column, padx=6, pady=6)
        buttons[item] = button

def slot3(s1Frame):
    for i, item in enumerate(drink):
        button = tk.Button(s1Frame, text=item, width=10, height=2, command=lambda item=item: add_to_cart(item, buttons[item],"drink.csv"))
        row = i // 5
        column = i % 5
        button.grid(row=row, column=column, padx=6, pady=6)
        buttons[item] = button

def hideIndicators():
    s1indicate.config(bg="#c3c3c3")
    s2indicate.config(bg="#c3c3c3")
    s3indicate.config(bg="#c3c3c3")


def indicate(lb, page):
    hideIndicators()
    lb.config(bg="#158aff")
    deletepages()
    page()


def deletepages():
    for frame in mainFrame.winfo_children():
        frame.destroy()


def s1page():
    s1Frame = tk.Frame(mainFrame)
    lb = tk.Label(s1Frame )
    lb.grid(row=0, column=0, pady=10)
    slot1(s1Frame)
    s1Frame.grid(row=0, column=0, padx=20, pady=20)


def s2page():
    s1Frame = tk.Frame(mainFrame)
    lb = tk.Label(s1Frame)
    slot2(s1Frame)
    lb.grid(row=0, column=0, pady=10)
    s1Frame.grid(row=0, column=0, padx=20, pady=20)
    
def s3page():
    s1Frame = tk.Frame(mainFrame)
    lb = tk.Label(s1Frame)
    slot3(s1Frame)
    lb.grid(row=0, column=0, pady=10)
    s1Frame.grid(row=0, column=0, padx=20, pady=20)


def add_to_cart(item_name, button, filename):
    if item_name not in cart_items:
        cart_items[item_name] = 1
    else:
        cart_items[item_name] += 1

    if filename == 'snack.csv':
        snack_dict[item_name]['quantity'] -= 1
        if snack_dict[item_name]['quantity'] <= 0:
            button.config(state=tk.DISABLED)
    elif filename == 'lunch.csv':
        lunch_dict[item_name]['quantity'] -= 1
        if lunch_dict[item_name]['quantity'] <= 0:
            button.config(state=tk.DISABLED)
    elif filename == 'drink.csv':
        drink_dict[item_name]['quantity'] -= 1
        if drink_dict[item_name]['quantity']<= 0:
            button.config(state=tk.DISABLED)
    update_csv(item_name, filename)
    update_cart_display()
    
def update_csv(item_name, filename):
    if filename == 'snack.csv':
        item_dict = snack_dict
    elif filename == 'lunch.csv':
        item_dict = lunch_dict
    elif filename == 'drink.csv':
        item_dict = drink_dict

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Item Name', 'Quantity', 'Price'])
        writer.writeheader()
        for name, details in item_dict.items():
            writer.writerow({'Item Name': name, 'Quantity': details['quantity'], 'Price': details['price']})

def save_cart_to_txt():
    with open("transaction.txt", 'a') as file:
        file.write("Item Name\tQuantity\tPrice\n")
        for item_name, quantity in cart_items.items():
            price = item_dict[item_name]["price"]
            total_price = price * quantity
            file.write(f"{item_name}\t{quantity}\t${total_price:.2f}\n")
    destroy_and_display_total()

def clear_cart():
    cartListbox.delete(0, tk.END)
    cart_items.clear()
    for button in buttons.values():
        button.config(state=tk.NORMAL)

def update_cart_display():
    cartListbox.delete(0, tk.END)
    total_price=0
    for item_name, quantity in cart_items.items():
        price = item_dict[item_name]["price"] * quantity
        total_price += price
        cartListbox.insert(tk.END, f"{item_name} x {quantity} - ${price:.2f}")
    cartListbox.insert(tk.END, f"Total Price :  Rs. {total_price:.2f}")
    
def destroy_and_display_total():

    for widget in root.winfo_children():
        widget.destroy()

    total_price = sum(snack_dict[item]["price"] * quantity for item, quantity in cart_items.items())

    tk.Label(root, text="You have purchased the following items:", font=("bold", 16)).pack(pady=10)
    for item, quantity in cart_items.items():
        price = snack_dict[item]["price"] * quantity
        tk.Label(root, text=f"{item} x {quantity} - Rs {price:.2f}", font=("bold", 12)).pack()
    tk.Label(root, text=f"Total Price: Rs {total_price:.2f}", font=("bold", 14)).pack(pady=10)
    
    return_home_button = tk.Button(root, text="Return to Home",command=return_home)
    return_home_button.pack(pady=10)
    
def return_home():
    root.destroy()

def allFrames_menu():
    global optionFrame,mainFrame,cartFrame,s1indicate,s2indicate,s3indicate,cartLabel,cartListbox
    optionFrame = tk.Frame(root, bg="#c3c3c3")
    optionFrame.grid(row=0, column=0, sticky="nsew")

    mainFrame = tk.Frame(root, highlightbackground="black", highlightthickness=2)
    mainFrame.grid(row=0, column=1, sticky="nsew")

    cartFrame = tk.Frame(root, highlightbackground="black", highlightthickness=2)
    cartFrame.grid(row=0, column=2, sticky="nsew")


    s1btn = tk.Button(optionFrame, text="Snacks", font=("bold", 15), fg="#158aff", bd=0, bg="#c3c3c3",
                  command=lambda: indicate(s1indicate, s1page))
    s1btn.grid(row=0, column=0, padx=10, pady=10)

    s2btn = tk.Button(optionFrame, text="Lunch", font=("bold", 15), fg="#158aff", bd=0, bg="#c3c3c3",
                  command=lambda: indicate(s2indicate, s2page))
    s2btn.grid(row=1, column=0, padx=10, pady=10)

    s3btn = tk.Button(optionFrame, text="Drink", font=("bold", 15), fg="#158aff", bd=0, bg="#c3c3c3",
                  command=lambda: indicate(s3indicate, s3page))
    s3btn.grid(row=2, column=0, padx=10, pady=10)
    

    s1indicate = tk.Label(optionFrame, text="", bg="#c3c3c3")
    s1indicate.grid(row=0, column=1, rowspan=1, sticky="nsew")

    s2indicate = tk.Label(optionFrame, text="", bg="#c3c3c3")
    s2indicate.grid(row=1, column=1, rowspan=1, sticky="nsew")

    s3indicate = tk.Label(optionFrame, text="", bg="#c3c3c3")
    s3indicate.grid(row=2, column=1, rowspan=1, sticky="nsew")

    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    cartLabel = tk.Label(cartFrame, text="Add to Plate", font=("bold", 22))
    cartLabel.grid(row=0, column=0, pady=10)

    cartListbox = tk.Listbox(cartFrame, width=30, height=35)
    cartListbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    clearButton = tk.Button(cartFrame, text="Clear", command=clear_cart)
    clearButton.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    proceedButton = tk.Button(cartFrame, text="Proceed",command=save_cart_to_txt)
    proceedButton.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    
allFrames_menu()
root.mainloop()