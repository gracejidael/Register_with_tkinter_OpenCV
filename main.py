
# This Program is a Registry... It accepts details of say staff(customers)
# And saves it,
# This details will include: name, email, image
# It uses basic GUI-tkinter, numpy, openCv and probably pandas libraries.


# Steps
# Get data
# Save data
# print("Let\'s get you Registered!!!")

# #click to capture photo

# Thank you {name} for signing in

from tkinter import *
from tkinter.ttk import *
from turtle import st
from ttkthemes import ThemedStyle
# import pickle
import csv


# Defining Functions to receive and save inputs


dict = {"First_Name": [], "Last_Name": [], "Email": [],
        "Gender": [], "Country": [], "Language": [], "Photo": []}


def submit_fxn():
    dict["First_Name"] = fname_entry.get()
    dict["Last_Name"] = lname_entry.get()
    dict["Email"] = email_entry.get()

    gend = vars.get()
    if gend == 1:
        dict["Gender"] = "Male"
    else:
        dict["Gender"] = "Female"

    dict["Country"] = cv.get()
    lang_get = vars1.get()
    if lang_get == 1:
        dict["Language"] = "English"
        # when other language options are added, the if statement  continues
    print(dict)

#     try:
#         record = open('record.csv', 'wb')
#         pickle.dump(dict, record)
#         record.close()
#     except:
#         print("Something went wrong while saving to external file!")

    csv_columns = ["First_Name", "Last_Name", "Email",
                   "Gender", "Country", "Language", "Photo"]

    csv_file = "record.csv"
    try:
        with open(csv_file, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            # writer.writeheader()
            writer.writerow(dict)
    except IOError:
        print("I/O error")


#
# Creating a simple GUI registration form using Tkinter in Python
# Creating the object 'base' of the Tk()
base = Tk()
style = ThemedStyle(base)  # add ubuntu style
style.set_theme('radiance')

# Using the maxsize method to the form certain dimensions
base.maxsize(900, 600)  # width * height
base.resizable(width=False, height=False)
base.configure(bg='#F6F4F2')  # background color

# Using title method to give the title to the window
base.title('Registration form')

# We now split the window to say three grids

left_frame = Frame(base, width=100, height=450)
left_frame.grid(row=0, column=0, padx=10, pady=5)
main_frame = Frame(base, width=450, height=450)
main_frame.grid(row=0, column=1, padx=10, pady=5)
right_frame = Frame(base, width=100, height=450)
right_frame.grid(row=0, column=2, padx=10, pady=5)

# # Now, we will use 'Label' method to add widget in the Registration Form and also use grid() method to set their #positions in the main_frame
heading = Label(main_frame, text="Registration form",
                width=20, font=("bold", 20))
heading.grid(columnspan=3, padx=(100, 0), pady=10)


fname = Label(main_frame, text="First Name: ", width=20, font=("bold", 10))
lname = Label(main_frame, text="Last Name: ", width=20, font=("bold", 10))
email = Label(main_frame, text="Email: ", width=20, font=("bold", 10))
gender = Label(main_frame, text="Gender", width=20, font=("bold", 10))


fname.grid(row=1, column=0, pady=5)
lname.grid(row=2, column=0, pady=5)
email.grid(row=3, column=0, pady=5)
gender.grid(row=4, column=0, pady=5)

# # Using Enrty widget to make a text entry box for accepting the input string in text from user.

fname_entry = Entry(main_frame, width=30)
lname_entry = Entry(main_frame, width=30)
email_entry = Entry(main_frame, width=30)


fname_entry.grid(row=1, column=1, padx=5, pady=5)
lname_entry.grid(row=2, column=1, padx=5, pady=5)
email_entry.grid(row=3, column=1, padx=5, pady=5)


# # Using variable 'vars' to store the integer value, which by default is 0
vars = IntVar()

# # Using Radio button widget to create an option choosing button

button1 = Radiobutton(main_frame, text="Male", variable=vars, value=1)
button2 = Radiobutton(main_frame, text="Female", variable=vars, value=2)


button1.grid(row=4, column=1)
button2.grid(row=5, column=1, padx=5)


# For Country
country = Label(main_frame, text="Country", width=20, font=("bold", 10))
country.grid(row=6, column=0, pady=5)

# # this creates list of countries available in the dropdown list.
list_of_cntry = ['Nigeria', 'Ghana', 'Cameroon',
                 'Togo', 'Chad', 'Niger', 'South Africa', 'Nigeria']

# # # the variable 'cv' is introduced to store the String Value, which by default is (empty) ""
cv = StringVar()
drplist = OptionMenu(main_frame, cv, *list_of_cntry)
drplist.config(width=20)
cv.set('Select your Country')
drplist.grid(row=6, column=1, padx=5)

# For Language Choice

language = Label(main_frame, text="Language", width=20, font=('bold', 10))
language.grid(row=7, column=0, pady=5)


# the new variable 'vars1' is created to store Integer Value, which by default is 0.
vars1 = IntVar()

lang_button1 = Checkbutton(main_frame, text="English", variable=vars1)
lang_button1.grid(row=7, column=1, pady=5)


photo = Button(main_frame, text='Take Photo', width=20)
photo.grid(row=8, column=1, pady=5)
# # Using the Button widget, we get to create a button for submitting all the data that has been entered in the entry boxes of the form by the user.

submit = Button(main_frame, text='Submit', width=20, command=submit_fxn)
submit.grid(row=9, column=1, pady=5)


# Calling the mainloop method to execute the entire program.
base.mainloop()
