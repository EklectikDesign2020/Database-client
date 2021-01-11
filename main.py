from os import path
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import csv
import os
import re

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
title = Label(root, font=(None, 10), text="<Company Name> MTE - V3.50", justif=CENTER)
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


# Variable Header
header1 = 'First Name'
header2 = 'Last Name'
header3 = 'Gender'
header4 = 'Address'
header5 = 'City'
header6 = 'Phone'
header7 = 'Email'
radio1 = 'Male'
radio2 = 'Female'

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

    defaut_header1 = 'First Name'
    defaut_header2 = 'Last Name'
    defaut_header3 = 'Gender'
    defaut_header4 = 'Address'
    defaut_header5 = 'City'
    defaut_header6 = 'Phone'
    defaut_header7 = 'Email'
    defaut_radio1 = 'Male'
    defaut_radio2 = 'Female'

    # Reset Default Header

    header1 = defaut_header1
    header_1.config(text=f"{header1} : ")
    header2 = defaut_header2
    header_2.config(text=f"{header2} : ")
    header3 = defaut_header3
    header_3.config(text=f"{header3} : ")
    header4 = defaut_header4
    header_4.config(text=f"{header4} : ")
    header5 = defaut_header5
    header_5.config(text=f"{header5} : ")
    header6 = defaut_header6
    header_6.config(text=f"{header6} : ")
    header7 = defaut_header7
    header_7.config(text=f"{header7} : ")
    radio1 =  defaut_radio1
    male.config(text=f"{radio1} : ")
    radio2 = defaut_radio2
    female.config(text=f"{radio2} : ")


###################################################
# This function deletes the old entries, once saved to the csv.
#    It will not deleter if the add_to_csv() is not call.
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
    flag_FN = False
    flag_EM = False
    flag_PH = False
    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if len(header_2_Entry.get()) == 0:
        messagebox.showwarning("Info empty...", "Last name are empty. If "
                                                "no info please enter 'NONE'")
    else:
        flag_FN = True

    if header7 == 'Email':
        if not re.search(regex_email, header_6_Entry.get()):
            messagebox.showwarning("Email format...", "Email format incorrect. Please enter correct format.")
        else:
            flag_EM = True
    else:
        flag_EM = True

    if header6 == 'Phone':
        if not str.isdigit(header_5_Entry.get()):
            messagebox.showwarning("Phone number format...", "Phone number is incorrect. "
                                                         "Only numbers no letter are allowed.")
        else:
            flag_PH = True
    else:
        flag_PH = True


    if flag_FN and flag_EM and flag_PH:
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




    # GUI
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

    bts = Button(frame_header, text='Change header', command=update_header)
    bts.grid(row=15, column=2, padx=5,pady=5)



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
                filewriter.writerow([header_1_Entry.get(), header_2_Entry.get(), sex.get(), header_3_Entry.get(), header_4_Entry.get(),
                                     header_5_Entry.get(), header_6_Entry.get()])

        else:
            with open(f"C:/Users/{username}/Documents/{file_name.get()}.csv", "w", newline='') as csvfile:
                filewriter = csv.writer(csvfile)
                filewriter.writerow([header1, header2, header3, header4, header5, header6, header7])
                filewriter.writerow([header_1_Entry.get(), header_2_Entry.get(), sex.get(), header_3_Entry.get(), header_4_Entry.get(),
                                     header_5_Entry.get(), header_6_Entry.get()])

        clear_entry()
        last_entry()

###################################################
# The function loads the correct header of the .csv file loaded
###################################################
def list_header():
    global header1
    global header2
    global header3
    global header4
    global header5
    global header6
    global header7

    with open(f'C:/Users/{username}/Documents/{file_name.get()}.csv') as f:
        reader = csv.reader(f)
        i = next(reader)
        rest = list(i)

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


        print(rest)


###################################################
# The function displays all entries.
#    Entries already existing, last entry.
###################################################
def last_entry():

    try:
        with open(f'C:/Users/{username}/Documents/{file_name.get()}.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            info_client_entry.config(state=NORMAL)
            info_client_entry.delete(1.0, END)
            info_client_entry.config(state=DISABLED)
            list_header()


            for col in reader:
                info_client_entry.config(state=NORMAL)
                info_client_entry.insert(END, col[header1] + "\n")
                info_client_entry.config(state=DISABLED)
    except Exception as error:
        messagebox.showerror(' Last entry name...', f'{error} - file name is empty. Please make sure filename is not empty or Header not much')



# Frame
frame_name = LabelFrame(root, text="   Personal information:   ", padx=40, pady=10)
frame_name.grid(row=4, column=1, padx=10,sticky=N)

frame_con = LabelFrame(root, text="   Contact information:   ", padx=48, pady=10)
frame_con.grid(row=5, column=1,padx=10, pady=5, sticky=W)

frame_last_c = LabelFrame(root, text=" Last client(s) entry ", padx=2, pady=14)
frame_last_c.grid(row=3, column=0, sticky=N, rowspan=5, padx=5)

frame_file = LabelFrame(root, text="   File name:   ", padx=20, pady=10)
frame_file.grid(row=3, column=1, padx=10, sticky=(W,N))

frame_info = LabelFrame(root, text="   How to use:  ", padx=40, pady=5)
frame_info.grid(row=3, column=2, rowspan=10, padx=10, sticky=(N,W))

# Text Box
info_client_entry = Text(frame_last_c, borderwidth=2, width=15, height=18, state=DISABLED)
info_client_entry.grid(row=4, columns=1, padx=3)

# Labels
important_info = Label(frame_info, fg='red',text='Reuse Existing .csv:', justify=LEFT)
important_info.grid()

important_info = Label(frame_info, text='It is recommended to use .csv files made with this application to avoid conflict.'
                                        '\nIf file was created with this application, type in file name and press "LOAD".'
                                        '\nAll Header used in the "Loaded" .csv file will be automatically change\nTo create new file type in new file name.', justify=LEFT)
important_info.grid()

important_info = Label(frame_info, fg='red',text='\n\nInfo files:', justify=LEFT)
important_info.grid()

important_info = Label(frame_info,text='Files are saved as .csv extension and are saved in "My Documents".\nEvery .csv file created can be modified using this application', justify=LEFT)
important_info.grid()


file_name_lab = Label(frame_file, text='Enter File name : ')
file_name_lab.grid(row=3, columns=3, sticky=E)

header_1 = Label(frame_name, text=f"{header1} : ")  # Frame name
header_1.grid(row=4, column=1, sticky=W)

header_2 = Label(frame_name, text=f"{header2} : ")  # Frame name
header_2.grid(row=5, column=1, sticky=W)

header_3 = Label(frame_name, text=f"{header3} : ")  # Frame name
header_3.grid(row=6, column=1, sticky=W)


header_4 = Label(frame_con, text=f"{header4} : ")
header_4.grid(row=6, column=2, sticky=W)

header_5 = Label(frame_con, text=f"{header5} : ")
header_5.grid(row=7, column=2, sticky=W)

header_6 = Label(frame_con, text=f"{header6} : ")
header_6.grid(row=8, column=2, sticky=W)

header_7 = Label(frame_con, text=f"{header7} : ")
header_7.grid(row=9, column=2, sticky=W)

# Entry Box
file_name = Entry(frame_file, borderwidth=2, width=15)
file_name.grid(row=3, column=3, padx=10, pady=2)

header_1_Entry = Entry(frame_name, borderwidth=2, width=40)  # Frame name
header_1_Entry.grid(row=4, column=3, padx=10, pady=2)

header_2_Entry = Entry(frame_name, borderwidth=2, width=40)  # Frame name
header_2_Entry.grid(row=5, column=3, padx=10, pady=2)

header_3_Entry = Entry(frame_con, borderwidth=2, width=40)
header_3_Entry.grid(row=6, column=4, padx=10, pady=2)

header_4_Entry = Entry(frame_con, borderwidth=2, width=40)
header_4_Entry.grid(row=7, column=4, padx=10, pady=2)

header_5_Entry = Entry(frame_con, borderwidth=2, width=40)
header_5_Entry.grid(row=8, column=4, padx=10, pady=2)

header_6_Entry = Entry(frame_con, borderwidth=2, width=40)
header_6_Entry.grid(row=9, column=4, padx=10, pady=2)




# Buttons
btn = Button(root, text="Add to .csv file", command=check_entry)
btn.grid(row=10, column=0, pady=5)
button_exit = Button(root, text='Quit Application', command=root.quit)
button_exit.grid(row=10, column=1, sticky=E, padx=5)
change_header = Button(root, text='Change Header', command=headers_change)
change_header.grid(row=10, column=1)
csv_load = Button(frame_file, text='Load csv', command=last_entry)
csv_load.grid(row=3, column=5, sticky=N)
reset_header = Button(root, text='Reset Headers to Default', command=header_default)
reset_header.grid(row=10, column=2)


# Radio Button
male = Radiobutton(frame_name, text=radio1, variable=sex, value="Male")  # Frame name
male.grid(row=6, column=3, sticky=W)
female = Radiobutton(frame_name, text=radio2, variable=sex, value="Female")  # Frame name
female.grid(row=6, column=3)


bottom_text = Label(root, font='None, 8',
                    text="Copyright - Design and coded by Eklectik Design - Eklectik.design@hotmail.com",
                    justify=CENTER)
bottom_text.grid(row=11, column=0, columnspan=8)



mainloop()
