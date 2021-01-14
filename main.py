from os import path
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import csv
import os
import re

# Main window
root = Tk()

# Pc profile
username = os.getlogin()

# Windows Configuration
root.title("Email-List creator")
root.resizable(width=FALSE, height=FALSE)
root.iconbitmap("MTE_icon.ico")

# GUI interface (label, entry, image)
title = Label(root, font=(None, 10), text="<Company Name> MTE - V4.00", justif=CENTER)
title.grid(row=0, column=0)
my_img = Image.open("image_MTE.png") # Image open
photo = ImageTk.PhotoImage(my_img)
label = Label(root, image=photo) # Add image to label
label.image = photo
label.grid(row=0, column=0, padx=10, pady=10, sticky=W) # Place label with image

# Variable for radio button (gender)
gender_value = StringVar()
gender_value.set("None")
option_del_rep = IntVar()
option_del_rep.set('1')

# Variable Header / DON'T MODIFY / Default setting
header1 = 'First Name'
header2 = 'Last Name'
header3 = 'Gender'
header4 = 'Address'
header5 = 'City'
header6 = 'Phone'
header7 = 'Email'
radio1 = 'Male'
radio2 = 'Female'


###################################################
# The function reset headers to default setting using above value.
#
###################################################
def header_default():
    # Global Variables
    global header1
    global header2
    global header3
    global header4
    global header5
    global header6
    global header7
    global radio1
    global radio2


    default_header1 = 'First Name'
    default_header2 = 'Last Name'
    default_header3 = 'Gender'
    default_header4 = 'Address'
    default_header5 = 'City'
    default_header6 = 'Phone'
    default_header7 = 'Email'
    default_radio1 = 'Male'
    default_radio2 = 'Female'

    # Reset Default Header / update label
    header1 = default_header1
    header_1.config(text=f"{header1} : ")
    header2 = default_header2
    header_2.config(text=f"{header2} : ")
    header3 = default_header3
    header_3.config(text=f"{header3} : ")
    header4 = default_header4
    header_4.config(text=f"{header4} : ")
    header5 = default_header5
    header_5.config(text=f"{header5} : ")
    header6 = default_header6
    header_6.config(text=f"{header6} : ")
    header7 = default_header7
    header_7.config(text=f"{header7} : ")
    radio1 =  default_radio1
    male.config(text=f"{radio1} : ")
    radio2 = default_radio2
    female.config(text=f"{radio2} : ")


###################################################
# This function deletes the old entries, once info is added to the csv.
#    It will not delete if the add_to_csv() is not call.
###################################################
def clear_entry():
    header_1_Entry.delete(0, END)
    header_2_Entry.delete(0, END)
    header_3_Entry.delete(0, END)
    header_4_Entry.delete(0, END)
    header_5_Entry.delete(0, END)
    header_6_Entry.delete(0, END)


###################################################
# This function checks for empty entries (first and last name).
#    If the entries are empty a warning message pop up.
# Checks if the client email and phone number are in correct format.
#    If the entries are incorrect a warning message pop up.
###################################################
def check_entry():
    # Get the entry
    global header_1_Entry
    global header_2_Entry
    global header_4
    global header_5_Entry
    global header_6_Entry

    # Flags
    flag_LN = False  # Last name
    flag_EM = False  # Email address
    flag_PH = False  # Phone number
    flag_AD = False  # Address


    # Regular expression
    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  # Example email@email.com
    regex_phone_us = '^\w{3}-\w{3}-\w{4}$'  # Example 516-111-2222

    if len(header_2_Entry.get()) <=2:
        messagebox.showwarning("Format incorrect...", "Last name is empty. If "
                                                "no info please enter 'NONE'")
    else:
        flag_LN = True

    if header7 == 'Email':
        if not re.search(regex_email, header_6_Entry.get()):
            messagebox.showwarning("Format incorrect.", "Email format incorrect. Please enter correct format. Example profilename@Domain.com or else.")
        else:
            flag_EM = True
    else:
        flag_EM = True

    if header6 == 'Phone':
        if not str.isdigit(header_5_Entry.get()) and not re.search(regex_phone_us, header_5_Entry.get()):
            messagebox.showwarning("Format incorrect.", "Phone number format  incorrect. "
                                                         "Please enter correct format. Example 516-111-2222")
        else:
            flag_PH = True
    else:
        flag_PH = True

    if '@' and '%' and '&' in header_5_Entry.get():
        messagebox.showwarning("Format incorrect.", "Address is incorrect format. "
                                                         "No special character in address.")
    else:
        flag_AD = True

    # If all format are correct add to .csv file
    if flag_LN and flag_EM and flag_PH and flag_AD:
        add_to_csv()


###################################################
# The function let's the use change headers.
#    It will not delete unused header.
# Let's the user change the Header name of .csv file if needed.
###################################################
def headers_change():
    top = Toplevel()
    # Global Variables
    global header1
    global header2
    global header3
    global header4
    global header5
    global header6
    global header7
    global radio1
    global radio2

    ### Gui section, here is only labels, entryBox and buttons ###
    # Frame
    frame_header = LabelFrame(top, text="    Change Headers:   ", padx=2, pady=10)
    frame_header.grid(row=1, column=5, rowspan=8, sticky=N, padx=5, pady=5)

    # Header change
    header1_changer = Label(frame_header, text=header1)
    header1_changer.grid(row=4, column=1)

    header2_changer = Label(frame_header, text=header2)
    header2_changer.grid(row=5, column=1)

    header3_changer = Label(frame_header, text=header3)
    header3_changer.grid(row=6, column=1)

    header4_changer = Label(frame_header, text=header4)
    header4_changer.grid(row=7, column=1)

    header5_changer = Label(frame_header, text=header5)
    header5_changer.grid(row=8, column=1)

    header6_changer = Label(frame_header, text=header6)
    header6_changer.grid(row=9, column=1)

    header7_changer = Label(frame_header, text=header7)
    header7_changer.grid(row=10, column=1)

    radio1_changer = Label(frame_header, text=radio1)
    radio1_changer.grid(row=11, column=1)

    radio2_changer = Label(frame_header, text=radio2)
    radio2_changer.grid(row=12, column=1)

    # Entry box.
    header1_changer_Entry = Entry(frame_header)
    header1_changer_Entry.grid(row=4, column=2, padx=10, pady=5)
    header1_changer_Entry.insert(END, header1)

    header2_changer_Entry = Entry(frame_header)
    header2_changer_Entry.grid(row=5, column=2, padx=10, pady=5)
    header2_changer_Entry.insert(END, header2)

    header3_changer_Entry = Entry(frame_header)
    header3_changer_Entry.grid(row=6, column=2, padx=10, pady=5)
    header3_changer_Entry.insert(END, header3)

    header4_changer_Entry = Entry(frame_header)
    header4_changer_Entry.grid(row=7, column=2, padx=10, pady=5)
    header4_changer_Entry.insert(END, header4)

    header5_changer_Entry = Entry(frame_header)
    header5_changer_Entry.grid(row=8, column=2, padx=10, pady=5)
    header5_changer_Entry.insert(END, header5)

    header6_changer_Entry = Entry(frame_header)
    header6_changer_Entry.grid(row=9, column=2, padx=10, pady=5)
    header6_changer_Entry.insert(END, header6)

    header7_changer_Entry = Entry(frame_header)
    header7_changer_Entry.grid(row=10, column=2, padx=10, pady=5)
    header7_changer_Entry.insert(END, header7)

    radio1_Change_Entry = Entry(frame_header)
    radio1_Change_Entry.grid(row=11, column=2, padx=10, pady=5)
    radio1_Change_Entry.insert(END, radio1)

    radio2_Change_Entry = Entry(frame_header)
    radio2_Change_Entry.grid(row=12, column=2, padx=10, pady=5)
    radio2_Change_Entry.insert(END, radio2)

    # Will update the labels of the application and headers to csv file
    def update_header():
        # Global Variables
        global header1
        global header2
        global header3
        global header4
        global header5
        global header6
        global header7
        global radio1
        global radio2

        header1 = header1_changer_Entry.get()
        header_1.config(text=f"{header1} : ")
        header2 = header2_changer_Entry.get()
        header_2.config(text=f"{header2} : ")
        header3 = header3_changer_Entry.get()
        header_3.config(text=f"{header3} : ")
        header4 = header4_changer_Entry.get()
        header_4.config(text=f"{header4} : ")
        header5 = header5_changer_Entry.get()
        header_5.config(text=f"{header5} : ")
        header6 = header6_changer_Entry.get()
        header_6.config(text=f"{header6} : ")
        header7 = header7_changer_Entry.get()
        header_7.config(text=f"{header7} : ")
        radio1 =  radio1_Change_Entry.get()
        male.config(text=f"{radio1} : ")
        radio2 = radio2_Change_Entry.get()
        female.config(text=f"{radio2} : ")

        top.destroy()

    change_headers = Button(frame_header, text='Change header', command=update_header)
    change_headers.grid(row=15, column=2, padx=5, pady=5)



###################################################
# The function checks if file name is empty.
#    If the entries is empty a warning message pop up.
# Create or append on file .csv only.
# Calls the clear_entry() function to clear all entry box.
# Calls ths last_entry() function to display last entry.
###################################################
def add_to_csv():
    global filewriter
    if len(file_added_entry.get()) == 0:
        messagebox.showwarning("File name.", "NO file name has been entered. Please enter file name or load file you wish to append to.")
    else:

        if path.exists(f"C:/Users/{username}/Documents/{file_added_entry.get()}.csv"):
            with open(f"C:/Users/{username}/Documents/{file_added_entry.get()}.csv", "a", newline='') as csvfile:
                filewriter = csv.writer(csvfile)
                filewriter.writerow([header_1_Entry.get(), header_2_Entry.get(), gender_value.get(), header_3_Entry.get(), header_4_Entry.get(),
                                     header_5_Entry.get(), header_6_Entry.get()])

        else:
            with open(f"C:/Users/{username}/Documents/{file_added_entry.get()}.csv", "w", newline='') as csvfile:
                filewriter = csv.writer(csvfile)
                filewriter.writerow([header1, header2, header3, header4, header5, header6, header7])
                filewriter.writerow([header_1_Entry.get(), header_2_Entry.get(), gender_value.get(), header_3_Entry.get(), header_4_Entry.get(),
                                     header_5_Entry.get(), header_6_Entry.get()])


        clear_entry()
        last_entry()

###################################################
# The function loads the correct header of the .csv file selected in browser
###################################################
def list_header():
    global header1
    global header2
    global header3
    global header4
    global header5
    global header6
    global header7

    with open(f'C:/Users/{username}/Documents/{file_added_entry.get()}.csv') as f:
        reader = csv.reader(f)
        i = next(reader)

        header1 = i[0]
        header_1.config(text=f"{header1} : ")
        header2 = i[1]
        header_2.config(text=f"{header2} : ")
        header3 = i[2]
        header_3.config(text=f"{header3} : ")
        header4 = i[3]
        header_4.config(text=f"{header4} : ")
        header5 = i[4]
        header_5.config(text=f"{header5} : ")
        header6 = i[5]
        header_6.config(text=f"{header6} : ")
        header7 = i[6]
        header_7.config(text=f"{header7} : ")


###################################################
# The function let's user modify existing information in the .csv file.
#    It reads the file change the info and overwrite old file .csv with the existing information
###################################################
def replace_info():
    # Windows Configuration
    top = Toplevel()
    top.title("Email-List creator")
    top.resizable(width=FALSE, height=FALSE)
    top.iconbitmap("MTE_icon.ico")

    ### Gui section, here is only labels, entryBox and buttons ###

    # Gui
    frame_replace = LabelFrame(top, text='Replace information Window.', padx=5, pady=5)
    frame_replace.grid(row=1, column=1, padx=5, pady=5)

    replace_word = Label(frame_replace, text=f'Find or Delete <type info> intake {header1}  : ')
    replace_word.grid(row=3, column=2)

    replace = Entry(frame_replace, borderwidth=2, width=15)
    replace.grid(row=3, column=3)

    replace_with = Label(frame_replace, text='Replace with <type info> : ')
    replace_with.grid(row=4, column=2)
    change = Entry(frame_replace, borderwidth=2, width=15)
    change.grid(row=4, column=3)

    # Function that does the replacement
    def change_info():
        try:
            with open(f'C:/Users/{username}/Documents/{file_added_entry.get()}.csv', 'r') as r:
                r = ''.join([i for i in r])
                r = r.replace(replace.get(), change.get())
                x = open(f'C:/Users/{username}/Documents/{file_added_entry.get()}.csv', 'w')
                x.writelines(r)
                x.close()
                last_entry()  # Update info client box
                clear_entry()  # Clear entry function
                top.destroy()  # Close window
        except Exception as error:
            messagebox.showerror("Replace information", f"{error} - No entry was detected. closing window.")
            top.destroy()

    # Function that delete rows
    def delete():
        with open(f'C:/Users/{username}/Documents/{file_added_entry.get()}.csv', 'r+') as r:
            lines = r.readlines()
            r.seek(0)

            for line in lines:
                if not replace.get() in line:
                    r.write(line)
            r.truncate()
            last_entry()  # Update info client box
            clear_entry()  # Clear entry function
            top.destroy()  # Close window


    replace_info_bts = Button(frame_replace, text='Replace info', command=change_info)
    replace_info_bts.grid(row=5, column=3)

    delete_info = Button(frame_replace, text='Delete info', command=delete)
    delete_info.grid(row=5, column=1, ipadx=4, pady=5)

    if not len(replace.get()) == 0:
        replace_info_bts.config(state=NORMAL)


###################################################
# The function displays all entries.
#    Entries already existing, last entry.
###################################################
def last_entry():
    try:
        with open(f'C:/Users/{username}/Documents/{file_added_entry.get()}.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            info_client_entry.config(state=NORMAL)
            info_client_entry.delete(1.0, END)
            info_client_entry.config(state=DISABLED)
            list_header()


            for col in reader:
                info_client_entry.config(state=NORMAL)
                info_client_entry.insert(END, 'Name: ' + col[header1] + ', ' + 'Email:' + col[header7] + "\n" )
                info_client_entry.config(state=DISABLED)
    except Exception as error:
        messagebox.showinfo('Last entry name...', f'{error} file is empty' )

    # Enable button
    if not info_client_entry.get(1.0, END) == '\n':
        modify_info.config(state=NORMAL)
        show_detail.config(state=NORMAL)



###################################################
# The function open the file explorer.
#    Allows user to selected a csv file and append or change info.
###################################################
def csv_browser():
    root.filename = filedialog.askopenfile(initialdir=f"C:/Users/{username}/Documents", title="Select a file",
                                           filetypes=((".csv files", "*.csv"), ("All files", "*.*")))
    def close_file():
        file_added_entry.config(state=NORMAL)
        file_added_entry.delete(0, END)
        info_client_entry.config(state=NORMAL)
        info_client_entry.delete(1.0, END)
        close_file.destroy()
        file_browser.config(state=NORMAL)
        # Enable button
        if info_client_entry.get(1.0, END) == '\n':
            modify_info.config(state=DISABLED)
            show_detail.config(state=DISABLED)

    try:
        file_name = os.path.basename(root.filename.name)
        if ".csv" in file_name:
            file_name = file_name.replace('.csv', '')
            file_added_entry.config(state=NORMAL)
            file_added_entry.delete(0, END)
            file_added_entry.insert(0, file_name)
            file_added_entry.config(state=DISABLED)
            last_entry()
            file_browser.config(state=DISABLED)

            close_file = Button(frame_file, text='Close file', command=close_file)
            close_file.grid(row=2, column=5, padx=5, sticky=E, ipadx=17, pady=5)
    except Exception as error:
        messagebox.showwarning('File select...', f'{error} - You have closed the file explorer and no file as been selected.' )


###################################################
# The function displays wanted client with First name.
#    Display all information in respective entry box.
###################################################
def show_info():
    # Global variables
    global header1
    global header2
    global header3
    global header4
    global header5
    global header6
    global header7
    try:
        with open(f'C:/Users/{username}/Documents/{file_added_entry.get()}.csv') as f:
            reader = csv.DictReader(f, delimiter=',')

            for col in reader:
                search_header = col[header1]
                if header_1_Entry.get().lower() == search_header.lower():
                    header_1_Entry.delete(0, END)
                    header_1_Entry.insert(0, col[header1])
                    header_2_Entry.insert(0, col[header2])
                    header_3_Entry.insert(0, col[header4])
                    header_4_Entry.insert(0, col[header5])
                    header_5_Entry.insert(0, col[header6])
                    header_6_Entry.insert(0, col[header7])

    except Exception as error:
        messagebox.showwarning('Display info ERROR', f'{error} - File is empty or {header1} Box is not existing in this file or empty.')


# Not finish
def help_info():
    help_win = Toplevel()
    help_win.title('Help information')

    frame_info = LabelFrame(help_win, text="   How to use:  ", padx=40, pady=5)
    frame_info.grid(row=3, column=2, rowspan=10, padx=10, sticky=(N,W))

    # Labels
    important_info = Label(frame_info, fg='red', text='File Management :', justify=LEFT)
    important_info.grid()

    important_info = Label(frame_info,
                           text='-CREATE NEW FILE : by adding a filename in the file name textbox you will be creating a new file to add client information.\n'
                                '-MODIFY EXISTING FILE : by clicking on "Choose file" you can modify an existing .csv file. (File must have been created with this application).', justify=LEFT)
    important_info.grid()

    important_info = Label(frame_info, fg='red', text='\n\nFunctionality :', justify=LEFT)
    important_info.grid()

    important_info = Label(frame_info,
                           text=f'-SHOW DETAIL : show detail button will show the information of the client name type in the respective Textbox, <{header1}> header1.\n'
                                '-MODIFY FILE : lets you modify or delete row, for the information you have entered, in "Find <info>" is info to replace, in "Replace is the replacement.\n'
                                '-CHANGE HEADER : lets you change the header "title" in first row of the .csv files for your needs.\n'
                                '-ADD TO FILE : will add the typed in info onto the file selected or new filename, once the format of each info are correct.\n'
                                '-RESET HEADER : will reset the headers to default, [First name, Last name etc..]',
                           justify=LEFT)
    important_info.grid()


### Gui section, here is only labels, entryBox and buttons ###

# File Section // Load file section
frame_file = LabelFrame(root, text="   File Management : <Enter new file name or browse for existing File>  ", padx=38, pady=10)
frame_file.grid(row=2, column=0, padx=15, rowspan=2, sticky=W, pady=5)

file_added_label = Label(frame_file, text='File name :    ')
file_added_label.grid(row=2, columns=1)

file_browser = Button(frame_file, text='Choose file', command=csv_browser)
file_browser.grid(row=2, column=5, padx=9, sticky=E, ipadx=10, pady=5)

file_added_entry = Entry(frame_file, borderwidth=2, width=40)
file_added_entry.grid(row=2, column=2, sticky=E, padx=10, pady=2)


# Frame
frame_last_c = LabelFrame(root, text=" Client(s) entry(ies) ", padx=15, pady=14)
frame_last_c.grid(row=3, column=2, sticky=NW, rowspan=3, padx=15)

frame_information_client = LabelFrame(root, text="   Client Information   ", padx=40, pady=10)
frame_information_client.grid(row=4, column=0, padx=15, sticky=W)


# Text Box
info_client_entry = Text(frame_last_c, borderwidth=2, width=45, height=19, state=DISABLED)
info_client_entry.grid(row=4, columns=1, padx=3)


# Label headers name row[0]
header_1 = Label(frame_information_client, text=f"{header1} : ")
header_1.grid(row=4, column=1, sticky=W)

header_2 = Label(frame_information_client, text=f"{header2} : ")
header_2.grid(row=5, column=1, sticky=W)

header_3 = Label(frame_information_client, text=f"{header3} : ")
header_3.grid(row=6, column=1, sticky=W)

header_empty = Label(frame_information_client, text="                               ")
header_empty.grid(row=7, column=1, columnspan=6, sticky=W)

header_4 = Label(frame_information_client, text=f"{header4} : ")
header_4.grid(row=8, column=1, sticky=W)

header_5 = Label(frame_information_client, text=f"{header5} : ")
header_5.grid(row=9, column=1, sticky=W)

header_6 = Label(frame_information_client, text=f"{header6} : ")
header_6.grid(row=10, column=1, sticky=W)

header_7 = Label(frame_information_client, text=f"{header7} : ")
header_7.grid(row=11, column=1, sticky=W)


# Entry Box
header_1_Entry = Entry(frame_information_client, borderwidth=2, width=40)
header_1_Entry.grid(row=4, column=3, padx=12, pady=5)

header_2_Entry = Entry(frame_information_client, borderwidth=2, width=40)
header_2_Entry.grid(row=5, column=3, padx=10, pady=5)

header_3_Entry = Entry(frame_information_client, borderwidth=2, width=40)
header_3_Entry.grid(row=8, column=3, padx=10, pady=5)

header_4_Entry = Entry(frame_information_client, borderwidth=2, width=40)
header_4_Entry.grid(row=9, column=3, padx=10, pady=5)

header_5_Entry = Entry(frame_information_client, borderwidth=2, width=40)
header_5_Entry.grid(row=10, column=3, padx=10, pady=5)

header_6_Entry = Entry(frame_information_client, borderwidth=2, width=40)
header_6_Entry.grid(row=11, column=3, padx=10, pady=5)


# Buttons
change_header = Button(frame_information_client, text='Change header', command=headers_change)
change_header.grid(row=10, column=4, padx=5, sticky=E)

add_file_to_csv = Button(frame_information_client, text="Add to file", command=check_entry)
add_file_to_csv.grid(row=11, column=4, padx=5, sticky=E, ipadx=13, pady=5)

button_exit = Button(root, text='Quit Application', command=root.quit)
button_exit.grid(row=11, column=2, sticky=E, pady=5, padx=15)

reset_header = Button(root, text='Reset headers', command=header_default)
reset_header.grid(row=11, column=2)

help_info = Button(root, text='Help', command=help_info)
help_info.grid(row=0, column=2, ipadx=10, sticky=E, padx=15)

show_detail = Button(frame_information_client, text='Show detail', command=show_info, state=DISABLED)
show_detail.grid(row=4, column=4,  padx=5, sticky=E, ipadx=9)

modify_info = Button(frame_information_client, text='Modify file ', command=replace_info, state=DISABLED)
modify_info.grid(row=9, columns=5, sticky=E, ipadx=10, padx=5)

# Radio Button
male = Radiobutton(frame_information_client, text=radio1, variable=gender_value, value="Male")  # Frame name
male.grid(row=6, column=3, sticky=W)
female = Radiobutton(frame_information_client, text=radio2, variable=gender_value, value="Female")  # Frame name
female.grid(row=6, column=3)

# Licence and info creator.
bottom_text = Label(root, font='None, 8',
                    text="Copyright - Design and coded by Eklectik Design - Eklectik.design@hotmail.com",
                    justify=LEFT)
bottom_text.grid(row=11, column=0)


mainloop()
