from os import path
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import csv
import os

root = Tk()

# Pc profile
username = os.getlogin()

# Windows Configuration
root.title("Email-List creator")
root.resizable(width=FALSE, height=FALSE)
root.iconbitmap("MTE_icon.ico")

# GUI interface (label, entry, image)
frame_title = LabelFrame(root, padx=5, pady=7, relief=RIDGE)
frame_title.grid(padx=5, pady=5, row=0, column=1, columnspan=3)
title = Label(root, font=(None, 10), text="<Company Name> MTE - V3.00", justif=CENTER)
title.grid(row=0, column=1, sticky=W)

# Image left upper side
my_img = Image.open("image_MTE.png")
photo = ImageTk.PhotoImage(my_img)
label = Label(root, image=photo)
label.image = photo
label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Variable for radio button (gender)
sex = StringVar()
sex.set("None")


###################################################
# This function deletes the old entries, once saved to the csv.
#    It will not deleter if the add_to_csv() is not call.
###################################################
def clear_entry():
    first_name_E.delete(0, END)
    last_name_E.delete(0, END)
    address_E.delete(0, END)
    city_E.delete(0, END)
    phone_number_E.delete(0, END)
    email_E.delete(0, END)


###################################################
# This function checks for empty entries (first and last name).
#    If the entries are empty a warning message pop up.
# Checks if the client email and phone number are in correct format.
#    If the entries are incorrect a warning message pop up.
###################################################
def check_entry():
    # Get the entry
    global first_name_E
    global last_name_E
    global address
    global phone_number_E
    global email_E
    flag_FN = False
    flag_EM = False
    flag_PH = False

    if len(last_name_E.get()) == 0:
        messagebox.showwarning("Info empty...", "Entry first name or last name are empty. If "
                                                "no info please enter 'NONE'")
    else:
        flag_FN = True

    if not'@' in email_E.get():
        messagebox.showwarning("Email format...", "Email format incorrect. Please enter correct format.")
    else:
        flag_EM = True

    if not str.isdigit(phone_number_E.get()):
        messagebox.showwarning("Phone number format...", "Phone number is incorrect. "
                                                         "Only numbers no letter are allowed.")
    else:
        flag_PH = True

    if flag_FN and flag_EM and flag_PH:
        add_to_csv()


###################################################
# The function checks if file name is empty.
#    If the entries is empty a warning message pop up.
# Create or append on file .csv only.
# Calls the clear_entry() function to clear all entry box.
# Calls ths last_entry() function to display last entry.
###################################################
# csv <finish for now>
def add_to_csv():
    if len(file_name.get()) == 0:
        messagebox.showwarning("File name...", "NO file name has been entered. Please enter file name.")
    else:

        if path.exists(f"C:/Users/{username}/Documents/{file_name.get()}.csv"):
            with open(f"C:/Users/{username}/Documents/{file_name.get()}.csv", "a", newline='') as csvfile:
                filewriter = csv.writer(csvfile)
                filewriter.writerow([first_name_E.get(), last_name_E.get(), sex.get(), address_E.get(), city_E.get(),
                                    phone_number_E.get(), email_E.get()])
        else:
            with open(f"C:/Users/{username}/Documents/{file_name.get()}.csv", "w", newline='') as csvfile:
                filewriter = csv.writer(csvfile)
                filewriter.writerow(['First-name', 'Last-name', 'Gender', 'Address', 'City', 'Phone', 'Email'])
                filewriter.writerow([first_name_E.get(), last_name_E.get(), sex.get(), address_E.get(), city_E.get(),
                                    phone_number_E.get(), email_E.get()])

        clear_entry()
        last_entry()


###################################################
# The function displays all entries.
#    Entries already existing, last entry.
###################################################
def last_entry():
    with open(f'C:/Users/{username}/Documents/{file_name.get()}.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        info_client_entry.config(state=NORMAL)
        info_client_entry.delete(1.0, END)
        info_client_entry.config(state=DISABLED)

        for col in reader:
            info_client_entry.config(state=NORMAL)
            info_client_entry.insert(END, col['First-name'] + "\n")
            info_client_entry.config(state=DISABLED)


# Frame
frame_name = LabelFrame(root, text="   Personal information:   ", padx=40, pady=5)
frame_name.grid(row=4, column=1)

frame_con = LabelFrame(root, text="   Contact information:   ", padx=40, pady=5)
frame_con.grid(row=6, column=1, padx=10, pady=5)

frame_last_c = LabelFrame(root, text=" Last client(s) entry ", padx=2, pady=10)
frame_last_c.grid(row=3, column=0, sticky=N, rowspan=5, padx=5)

frame_file = LabelFrame(root, text="   File name:   ", padx=2, pady=10)
frame_file.grid(row=6, column=2, padx=5, sticky=N)

frame_info = LabelFrame(root, text="   Append on Existing File:   ", padx=2, pady=10)
frame_info.grid(row=1, column=2, rowspan=5, padx=5, sticky=N)


# Text Box
info_client_entry = Text(frame_last_c, borderwidth=2, width=15, height=12, state=DISABLED)
info_client_entry.grid(row=4, columns=1, padx=5)

# Labels
important_info = Label(frame_info, text='If you wish to append information to an existing file,\n'
                                        'type the correct name without the extension.', justify=LEFT)
important_info.grid()

file_name_lab = Label(frame_file, text='Enter file name for csv : ')
file_name_lab.grid(row=3, columns=1, sticky=W)

first_name = Label(frame_name, text="First name : ")  # Frame name
first_name.grid(row=4, column=1, sticky=W)

last_name = Label(frame_name, text="Last name : ")  # Frame name
last_name.grid(row=5, column=1, sticky=W)

sex_radio_button = Label(frame_name, text="Gender : ")  # Frame name
sex_radio_button.grid(row=6, column=1, sticky=W)


address = Label(frame_con, text="Address : ")
address.grid(row=6, column=2, sticky=W)

city = Label(frame_con, text="City : ")
city.grid(row=7, column=2, sticky=W)

phone_number = Label(frame_con, text="Phone number : ")
phone_number.grid(row=8, column=2, sticky=W)

email = Label(frame_con, text="Email : ")
email.grid(row=9, column=2, sticky=W)

# Entry Box
file_name = Entry(frame_file, borderwidth=2, width=25)
file_name.grid(row=3, column=3)

first_name_E = Entry(frame_name, borderwidth=2, width=40)  # Frame name
first_name_E.grid(row=4, column=3, padx=10, pady=2)

last_name_E = Entry(frame_name, borderwidth=2, width=40)  # Frame name
last_name_E.grid(row=5, column=3, padx=10, pady=2)

address_E = Entry(frame_con, borderwidth=2, width=36)
address_E.grid(row=6, column=4, padx=10, pady=2)

city_E = Entry(frame_con, borderwidth=2, width=36)
city_E.grid(row=7, column=4, padx=10, pady=2)

phone_number_E = Entry(frame_con, borderwidth=2, width=36)
phone_number_E.grid(row=8, column=4, padx=10, pady=2)

email_E = Entry(frame_con, borderwidth=2, width=36)
email_E.grid(row=9, column=4, padx=10, pady=2)

# Buttons
btn = Button(root, text="Add to .csv file", command=check_entry)
btn.grid(row=10, column=0, pady=5)
button_exit = Button(root, text='Quit Application', command=root.quit)
button_exit.grid(row=10, column=1, sticky=E, padx=5)

# Radio Button
male = Radiobutton(frame_name, text="Male", variable=sex, value="Male")  # Frame name
male.grid(row=6, column=3, sticky=W)
female = Radiobutton(frame_name, text="Female", variable=sex, value="Female")  # Frame name
female.grid(row=6, column=3)

# Buttons
bottom_text = Label(root, font='None, 8',
                    text="Copyright - Design and coded by Eklectik Design - Eklectik.design@hotmail.com",
                    justify=CENTER)
bottom_text.grid(row=11, column=0, columnspan=2)

mainloop()
