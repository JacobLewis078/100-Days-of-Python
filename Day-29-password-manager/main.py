from tkinter import *
import random
import string

FONT = ("Arial", 12)
PASSWORD_FILE = ".my_file_txt"

# ----------------------- Password Length -------------------------------- #
# allows user to choose number of characters desired for password
def password_length():
    popup = Tk()
    popup.title("Password Length")
    popup.config(pady=50, padx=50)


    number_text = Label(popup, text="Enter Desired Password Length:")
    number_text.grid(column=1,row=1)

    entered_number = IntVar()
    number = Entry(popup, textvariable=entered_number)
    number.grid(column=2,row=2)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# generates a random password that is 16 characters long for user to use when signing up for a website
def generate_password():
    number = int(length_input.get())
    new_password = StringVar()
    random_password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits,
                                          k=number))
    new_password.set(random_password)
    password_input.config(textvariable=new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Saves Website, email/username, and password that was entered by the user into the file .my_file.txt
#.my_file.txt is hidden to enhance security
def save_password():
    success()
    with open(PASSWORD_FILE, "a") as file:
        file.write(f"{website_input.get()} | {email_username_input.get()} {password_input.get()}\n")

    website_input.delete(0, END)
    email_username_input.delete(0, END)
    password_input.delete(0, END)
    length_input.set(0)
    website_input.focus()

# # --------------------Change Slider Variable --------------------------- #
# def slider_variable(value):
#     length_label.config(text=value)

# --------------------------- Success Dialog Box -------------------------- #
# This is the dialog box that pops up when the end user clicks the add button to let them know the password was saved successfully
def success():
    popup = Toplevel(window)
    popup.title("Success")
    popup.geometry("250x65+300+200")

    success_label = Label(popup, font=FONT, text=f"Password successfully added to {PASSWORD_FILE}")
    success_label.grid(column = 0, row = 0)
    success_button = Button(popup, text="Done", command=popup.destroy)
    success_button.grid(column=0, row=1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# ---- Labels ----- #
website_label = Label(font=FONT, text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(font=FONT, text="Email/Username:")
email_username_label.grid(column=0, row=2)

length_label = Label(font=FONT, text="Desired Length of Password:")
length_label.grid(column=0, row=3)

password_label = Label(font=FONT, text="Password:")
password_label.grid(column=0, row=4)


# ----- Input Fields -----#

# website entry
website_text = StringVar()
website_input = Entry(width=35, textvariable=website_text)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

# username or email entry
email_username_text = StringVar()
email_username_input = Entry(width=35, textvariable=email_username_text)
email_username_input.grid(column=1, row=2, columnspan=2)

# Slider where user determines the length of the password they want to generate
length_input = Scale(window, from_= 0, to=100, orient="horizontal", length=300)
length_input.grid(column=1, row=3, columnspan=2)

# Generated Password text
password_text = StringVar()
password_input = Entry(width=18, textvariable=password_text)
password_input.grid(column=1, row=4)

# ---- Buttons ----- #
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=4)

add_button = Button(text="Add", width=32, command=save_password)
add_button.grid(column=1, row=5, columnspan=2)


window.mainloop()
