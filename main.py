from curses import window
from tkinter import *
from turtle import width

#Saving Data
def saveData():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    with open("data.txt", "a") as data_log:
        data_log.write(f"{website} | {username} | {password}\n")
        entry_website.delete(0, END)
        entry_username.delete(0, END)
        entry_password.delete(0, END)


# UI Setup

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, )

canvas = Canvas(height=200, width=200)
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
entry_username.grid(row=2, column=1, columnspan=2)

entry_password = Entry(width=15)
entry_password.grid(row=3, column=1, columnspan=1)

#Buttons
gen_password_button = Button(text="Generate Password")
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=saveData)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()