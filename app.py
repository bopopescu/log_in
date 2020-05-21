from tkinter import *
from connect_database import *

"""""
def delete_label():
    label.destroy()
"""""


def register_user():
    username_info = username_register.get()
    password_info = password_register.get()

    if (len(username_info) != 0 and len(password_info) != 0):
        connect(username_info, password_info)

        if not is_user_registered(username_info):
            # We add the user
            add_user(username_info, password_info)

            Label(rg_screen, text="Registration completed successfully", fg="green",
                  width="200", height="1").pack()

        else:
            Label(rg_screen, text="Your usuary name is already taken", fg="red", width="200",
                  height="1").pack()
    else:
        Label(rg_screen, text="You have to fill all the gaps", fg="red", width="200",
              height="1").pack()

    # Delete the info
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def register():
    global username_register
    global password_register
    global username_entry
    global password_entry
    global rg_screen

    rg_screen = Toplevel(screen)
    rg_screen.geometry("300x200")
    rg_screen.title("Register")

    username_register = StringVar()
    password_register = StringVar()

    Label(rg_screen, text="Create an account", width="150", height="1", font=("Calibri", 13)).pack()
    Label(rg_screen, text="").pack()

    # Username
    Label(rg_screen, text="Username", width="10", height="1").pack()
    username_entry = Entry(rg_screen, textvariable=username_register)
    username_entry.pack()

    # Password
    Label(rg_screen, text="Password", width="10", height="1").pack()
    password_entry = Entry(rg_screen, textvariable=password_register)
    password_entry.pack()

    # Button register
    Button(rg_screen, text="Register", width="10", height="1", command=register_user).pack()


def login():
    global username_login
    global password_login
    global lg_screen

    username_login = StringVar()
    password_login = StringVar()

    lg_screen = Toplevel(screen)
    lg_screen.geometry("300x200")
    lg_screen.title("Log in")

    Label(lg_screen, text="Log in", width="150", height="1", font=("Calibri", 13)).pack()
    Label(lg_screen, text="").pack()

    # Username
    Label(lg_screen, text="Username", width="10", height="1").pack()
    username_entry = Entry(lg_screen, textvariable=username_login)
    username_entry.pack()

    # Password
    Label(lg_screen, text="Password", width="10", height="1").pack()
    password_entry = Entry(lg_screen, textvariable=password_login)
    password_entry.pack()

    # Button register
    Button(lg_screen, text="Enter", width="10", height="1", command=login_user).pack()


def login_user():
    username_info = username_login.get()
    password_info = password_login.get()

    if (len(username_info) != 0 and len(password_info) != 0):
        connect(username_info, password_info)
        if (is_user_registered(username_info) and is_password_correct(username_info, password_info)):
            logged_screen = Toplevel(lg_screen)
            logged_screen.geometry("300x200")
            logged_screen.title("Log in")
            Label(logged_screen, text="Hi " + username_info, fg="black", width="400", height="10").pack()
        else:
            Label(lg_screen, text="Your usuary or your password is incorrect", fg="red", width="200",
                  height="1").pack()
    else:
        Label(lg_screen, text="You have to fill all the gaps", fg="red", width="200",
              height="1").pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x200")
    screen.title("MyApp 1.0")

    Label(text="MyApp 1.0", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    # Buttons
    Button(text="Login", height="1", width=10, command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="1", width=10, command=register).pack()

    # Needed to see the window
    screen.mainloop()


main_screen()
