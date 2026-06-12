import os
import sys

# -------------------- FIX FOR NO GUI ENVIRONMENT --------------------
if os.name != "nt":  # Windows doesn't use DISPLAY variable
    if "DISPLAY" not in os.environ or not os.environ["DISPLAY"]:
        print("\nERROR: No graphical display detected!")
        print("Run this program on your Laptop/PC (not in online compiler).")
        sys.exit(1)
# --------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, simpledialog

# -------------------- ROOM DATA --------------------
rooms = {
    101: {"type": "AC", "capacity": 2, "available": True, "rate": 1500},
    102: {"type": "AC", "capacity": 4, "available": True, "rate": 2200},
    201: {"type": "Non-AC", "capacity": 2, "available": True, "rate": 1000},
    202: {"type": "Non-AC", "capacity": 3, "available": True, "rate": 1300},
    301: {"type": "AC", "capacity": 3, "available": True, "rate": 2000},
    302: {"type": "Non-AC", "capacity": 4, "available": True, "rate": 1500},
}

# -------------------- RESTAURANT MENU --------------------
menu_items = {
    "Idly": 30, "Dosa": 50, "Biryani": 180,
    "Fried Rice": 120, "Meals": 100, "Paneer Curry": 140,
    "Chicken Curry": 170, "Ice Cream": 40, "Cold Drink": 20
}

# Store booking details
current_booking = {}

# NEW: Booking count
total_bookings = 0

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("500x600")

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# -------------------- START PAGE --------------------
def start_page():
    clear_window()

    tk.Label(root, text="HOTEL MANAGEMENT SYSTEM", font=("Arial", 18, "bold")).pack(pady=20)

    # Display number of bookings
    tk.Label(root, text=f"Total Bookings: {total_bookings}",
             font=("Arial", 14), fg="blue").pack(pady=5)

    tk.Button(root, text="New Booking", font=("Arial", 14), width=20, command=customer_details).pack(pady=10)
    tk.Button(root, text="Checkout", font=("Arial", 14), width=20, command=checkout_page).pack(pady=10)
    tk.Button(root, text="Exit", font=("Arial", 14), width=20, command=root.destroy).pack(pady=10)

# -------------------- CUSTOMER DETAILS --------------------
def customer_details():
    clear_window()

    tk.Label(root, text="Enter Customer Details", font=("Arial", 16, "bold")).pack(pady=10)

    labels = ["Name", "Phone", "Address", "Aadhar No"]
    entries = {}

    for label in labels:
        tk.Label(root, text=label, font=("Arial", 12)).pack()
        entry = tk.Entry(root, width=30)
        entry.pack()
        entries[label] = entry

    def submit_details():
        for label, entry in entries.items():
            if entry.get().strip() == "":
                messagebox.showerror("Error", f"Please enter {label}")
                return

        current_booking["name"] = entries["Name"].get()
        current_booking["phone"] = entries["Phone"].get()
        current_booking["address"] = entries["Address"].get()
        current_booking["aadhar"] = entries["Aadhar No"].get()

        room_selection()

    tk.Button(root, text="Next", font=("Arial", 14), command=submit_details).pack(pady=15)

# -------------------- ROOM SELECTION --------------------
def room_selection():
    clear_window()

    tk.Label(root, text="Select Available Room", font=("Arial", 16, "bold")).pack(pady=10)

    available_rooms = [room for room, data in rooms.items() if data["available"]]

    if not available_rooms:
        messagebox.showinfo("No Rooms", "Rooms are not available")
        start_page()
        return

    room_var = tk.StringVar()
    room_var.set(str(available_rooms[0]))

    for room in available_rooms:
        data = rooms[room]
        tk.Radiobutton(
            root,
            text=f"Room {room} - {data['type']} - {data['capacity']} People - Rs {data['rate']}/day",
            variable=room_var,
            value=str(room),
            font=("Arial", 12)
        ).pack(anchor="w")

    tk.Label(root, text="Enter No. of Days:", font=("Arial", 12)).pack()
    days_entry = tk.Entry(root, width=10)
    days_entry.pack()

    def confirm_room():
        if not days_entry.get().isdigit():
            messagebox.showerror("Error", "Enter valid number of days")
            return

        room_no = int(room_var.get())
        days = int(days_entry.get())

        current_booking["room_no"] = room_no
        current_booking["days"] = days
        current_booking["rate"] = rooms[room_no]["rate"]

        payment_page()

    tk.Button(root, text="Proceed to Payment", font=("Arial", 14), command=confirm_room).pack(pady=15)

# -------------------- PAYMENT --------------------
def payment_page():
    clear_window()

    tk.Label(root, text="Room Payment", font=("Arial", 16, "bold")).pack(pady=10)

    total_amount = current_booking["days"] * current_booking["rate"]
    current_booking["amount"] = total_amount

    tk.Label(root, text=f"Total Amount: Rs {total_amount}", font=("Arial", 14)).pack(pady=10)

    pay_var = tk.StringVar()
    pay_var.set("PhonePe")

    for mode in ["PhonePe", "Card", "Cash"]:
        tk.Radiobutton(root, text=mode, variable=pay_var, value=mode, font=("Arial", 12)).pack(anchor="w")

    def finalize_payment():
        global total_bookings

        rooms[current_booking["room_no"]]["available"] = False
        total_bookings += 1   # INCREASE TOTAL BOOKINGS

        messagebox.showinfo("Success",
                            f"Payment Successful!\nRoom {current_booking['room_no']} allotted.\n\n"
                            f"Total Bookings Now: {total_bookings}")

        food_choice()

    tk.Button(root, text="Pay & Confirm", font=("Arial", 14), command=finalize_payment).pack(pady=15)

# -------------------- FOOD SERVICE --------------------
def food_choice():
    clear_window()

    tk.Label(root, text="Food Service", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Button(root, text="Order to Room", font=("Arial", 14), width=20, command=restaurant_menu).pack(pady=10)
    tk.Button(root, text="Book a Table", font=("Arial", 14), width=20, command=restaurant_menu).pack(pady=10)
    tk.Button(root, text="Skip", font=("Arial", 14), width=20, command=start_page).pack(pady=10)

# -------------------- RESTAURANT MENU --------------------
def restaurant_menu():
    clear_window()

    tk.Label(root, text="Restaurant Menu", font=("Arial", 16, "bold")).pack(pady=10)

    selected_items = []

    def add_item(item):
        selected_items.append(item)
        messagebox.showinfo("Added", f"{item} added to your order")

    for item, price in menu_items.items():
        tk.Button(root, text=f"{item} - Rs {price}", width=25,
                  command=lambda i=item: add_item(i)).pack(pady=2)

    def pay_food_bill():
        if not selected_items:
            messagebox.showerror("Error", "No items selected")
            return

        total = sum(menu_items[item] for item in selected_items)

        clear_window()
        tk.Label(root, text=f"Your Food Bill: Rs {total}", font=("Arial", 16)).pack(pady=10)

        pay_var = tk.StringVar()
        pay_var.set("PhonePe")

        for mode in ["PhonePe", "Card", "Cash"]:
            tk.Radiobutton(root, text=mode, variable=pay_var, value=mode, font=("Arial", 12)).pack(anchor="w")

        def final_pay():
            messagebox.showinfo("Thank you", "Payment Successful!\nThanks for visiting.")
            start_page()

        tk.Button(root, text="Pay Now", font=("Arial", 14), command=final_pay).pack(pady=15)

    tk.Button(root, text="Proceed to Payment", font=("Arial", 14), command=pay_food_bill).pack(pady=15)

# -------------------- CHECKOUT --------------------
def checkout_page():
    clear_window()

    tk.Label(root, text="Checkout", font=("Arial", 16, "bold")).pack(pady=10)

    room_no = simpledialog.askinteger("Checkout", "Enter Room Number:")

    if room_no not in rooms or rooms[room_no]["available"] == True:
        messagebox.showerror("Error", "Invalid room number or not occupied")
        start_page()
        return

    booked_days = current_booking.get("days", 1)
    actual_days = simpledialog.askinteger("Checkout", "How many days did customer stay?")

    if actual_days > booked_days:
        extra_days = actual_days - booked_days
        extra_charge = extra_days * rooms[room_no]["rate"]
        messagebox.showinfo("Extra Charges", f"Extra Days: {extra_days}\nExtra Amount: Rs {extra_charge}")

    rooms[room_no]["available"] = True
    messagebox.showinfo("Success", "Checkout Completed Successfully!")
    start_page()

# -------------------- START APP --------------------
start_page()
root.mainloop()