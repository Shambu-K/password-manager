from curses import window
from queue import Empty
from tkinter import *
from turtle import width
from tkinter import messagebox
import random
import pyperclip

#Password generator
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+',]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_seg = [random.choice(letters) for _ in range(nr_letters)]
    numbers_seg = [random.choice(numbers) for _ in range(nr_numbers)]
    symbols_seg = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letters_seg + numbers_seg + symbols_seg

    random.shuffle(password_list)

    password = "".join(password_list)

    # print(f"ans: {password}")

    entry_password.insert(0, password)
    pyperclip.copy(password)


#Saving Data
def saveData():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="Do not leave any fields empty")

    else:
        verify = messagebox.askokcancel(title=website, message=f"The following details will be saved:\nEmail: {username} " f"\nPassword: {password}\n")

        if verify:
            with open("data.txt", "a") as data_log:
                data_log.write(f"{website} | {username} | {password}\n")
                entry_website.delete(0, END)
                entry_username.delete(0, END)
                entry_password.delete(0, END)


# UI Setup

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white" )

canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(row=0, column=1)

#Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_username = Label(text="Email/Username:")
label_username.grid(row=2, column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0, columnspan=1)

#Entries
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_username = Entry(width=35)
entry_username.insert(0,"shambukavir958@gmail.com")
entry_username.grid(row=2, column=1, columnspan=2)

entry_password = Entry(width=15)
entry_password.grid(row=3, column=1, columnspan=1)

#Buttons
gen_password_button = Button(text="Generate Password", command=generatePassword)
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=saveData)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()