from tkinter import *

def submit_form():
    # Values 
    name = name_val.get()
    phone = phone_val.get()
    gender = gender_val.get()
    emergency = emergency_val.get()
    payment = payment_val.get()
    prebook_meal = "Yes" if meal_val.get() == 1 else "No" 

    # text file to store the data 
    with open("records.txt", "a") as f:
        f.write(f"{name}, {phone}, {gender}, {emergency}, {payment}, Prebook Meal: {prebook_meal}\n")

    
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    gender_entry.set("select Gender")
    emergency_entry.delete(0, END)
    payment_val.set("Select payment option")
    meal_val.set(0)


root = Tk()
root.geometry("800x400")
root.title("MACLEANS TRAVEL AGENCY") 

#Heading
Label(root, text="MACLEANS TRAVEL AGENCY", font="Arial 14 bold").grid(row=0, column=1, pady=20) 

#Labels
Label(root, text="Name").grid(row=1, column=0)
Label(root, text="Phone").grid(row=2, column=0)
Label(root, text="Gender").grid(row=3, column=0)
Label(root, text="Emergency Contact").grid(row=4, column=0)
Label(root, text="Payment option").grid(row=5, column=0)

# Variables
name_val = StringVar()
phone_val = StringVar()
gender_val = StringVar(value="Select Gender")
emergency_val = StringVar()
payment_val = StringVar(value="Select payment option")
meal_val = IntVar()

# Entry
name_entry = Entry(root, textvariable=name_val)
phone_entry = Entry(root, textvariable=phone_val)
gender_entry = Entry(root, textvariable=gender_val)
emergency_entry = Entry(root, textvariable=emergency_val)
payment_entry = Entry(root, textvariable=payment_val) 


name_entry.grid(row=1, column=1)
phone_entry.grid(row=2, column=1)
gender_entry.grid(row=3, column=1)
emergency_entry.grid(row=4, column=1)
payment_entry.grid(row=5, column=1)


gender_menu = ["Male", "Female", "Rather not say"]
payment_optons = ["Credit card", "Debit card"] 

gender_menu = OptionMenu(root, gender_val, *gender_menu) 
payment_menu = OptionMenu(root, payment_val, *payment_optons)  

gender_menu.grid(row=3, column=2)
payment_menu.grid(row=5, column=2)

#Checkbox
Checkbutton(text="Want to prebook your meals?", variable=meal_val).grid(row=6, column=1, pady=10)

#Submit form 
Button(text="Submit", command=submit_form).grid(row=7, column=1)

root.mainloop() 