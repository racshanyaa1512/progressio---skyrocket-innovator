from tkinter import *
from functools import partial


def movetoActionManager():
    import ActionManager


# window
LoginWindow = Tk()
LoginWindow.geometry('1120x630')
LoginWindow.title('EnvirAware Login')

# username label and text entry box
usernameLabel = Label(LoginWindow, text="User Name").grid(row=150, column=10)
username = StringVar()
usernameEntry = Entry(LoginWindow, textvariable=username).grid(row=150, column=20)

# password label and password entry box
passwordLabel = Label(LoginWindow, text="Password").grid(row=160, column=10)
password = StringVar()
passwordEntry = Entry(LoginWindow, textvariable=password, show='*').grid(row=160, column=20)

# login button
loginButton = Button(LoginWindow, text="Login", command=movetoActionManager).grid(row=200, column=50)

LoginWindow.mainloop()
