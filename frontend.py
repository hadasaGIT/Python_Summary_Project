from tkinter import *
import tkinter as tk
import Logic
from mongo import mongoLogic

"""This class is a class for displaying and designing a window for the user to rename files or directories from the local computer or database
prams: Main window and three label and three entry and 2 Checkbutton and Button, 2 string  messages for user
this class include func:
constructor to init the params 
func rename -the function that renames the files from the local computer or database
"""


class frontend:
    """init the object
    :param self: object FrontEnd
    :type self: object
    :return: window user
    :rtype: tkinter
    """

    def __init__(self):

        # Create a window for the user, resize and other properties
        self.app = tk.Tk()
        self.app.title("rename file or dir")
        self.app.geometry("600x370+400+300")
        self.app.configure()

        # Create a label and Input box for the file name you want to rename
        tk.Label(self.app, text="Change from name:").pack()
        self.e1 = tk.Entry(self.app, border=2.5, width=30, bd=1)
        self.e1.pack(pady=10)

        # Create a label and Input box for the name you want to change to
        tk.Label(self.app, text="To name:").pack()
        self.e2 = tk.Entry(self.app, border=2.5, width=30, bd=1)
        self.e2.pack(pady=10)

        # Create a label and Input box for the routing to a directory where you want to rename files or for Link to a particular database
        tk.Label(self.app, text="The path to change files:", bd="3").pack()
        self.e3 = tk.Entry(self.app, border=2.5, width=30, bd=1)
        self.e3.pack(pady=10)

        # Two choice variables where to rename files from local computer, database or both
        # Create a Checkbutton for local
        self.chk_state_local = BooleanVar()
        self.chk_state_local.set(False)  # set check state
        chk_l = Checkbutton(self.app, text='Rename local files', var=self.chk_state_local).pack()

        # Create a Checkbutton for mongoDB
        self.chk_state_DB = BooleanVar()
        self.chk_state_DB.set(False)  # set check state
        chk_db = Checkbutton(self.app, text='Rename files in the database', var=self.chk_state_DB).pack()

        # Send to a function init_btn() that will create the button
        self.btn = self.init_btn()

        # Create a Input box for the message -Feedback on program success for local files
        self.message_l = tk.Entry(self.app, width=100, fg="blue", bd=1)
        self.message_l.pack(pady=10)

        # Create a Input box for the message -Feedback on program success for database files
        self.message_DB = tk.Entry(self.app, width=100, fg="blue", bd=1)
        self.message_DB.pack(pady=10)

        # Activating the window with all the elements
        self.app.mainloop()

    """function that init button
    :param self: object FrontEnd
    :type self: object
    :return: Initialized button
    :rtype: object of tkinter
    """

    def init_btn(self):
        # Create a button To activate the function rename()
        btn = tk.Button(self.app, text="Rename files or dir", width=25, command=self.click, bg="green", fg="white",
                        bd="1")
        btn.pack(padx=80, pady=20, anchor='center')
        return btn

    """A function that defines what happens when the button is pressed
    :param self: object FrontEnd
    :type self: object
    :return: no
    :rtype: no
    """

    def click(self):

        # Init Input boxes for the message and init the strings of responses
        self.message_DB.delete(0, END)
        self.message_l.delete(0, END)
        response_DB = "No change was made in DB"
        response_local = "No change was made in local file"
        #
        try:
            # If Checkbutton for local is TRUE- send the variables For the rename function in logic
            if self.chk_state_local.get():
                logic1 = Logic.logic(self.e1.get(), self.e2.get(), self.e3.get())
                count = logic1.rename()
                response_local = "Succeeded! " + str(count) + " local files/directories changed "
        except Exception as e:
            print(e)
            response_local = "Oops it's failed! -" + str(e)[12:]
        try:
            # If Checkbutton for DB is TRUE- send the variables For the rename function in mongoLogic
            if self.chk_state_DB.get():
                mongo_rename = mongoLogic(self.e1.get(), self.e2.get(), self.e3.get())
                s = mongo_rename.rename()
                response_DB = "Succeeded! files/directories changed from DB"
        except Exception as e:
            print(e)
            response_DB = "Oops it's failed! -" + str(e)[12:]
        # Init the Input boxes
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        # Insert the response_local and response_DB to Input boxes that Designed for them
        self.message_l.insert(0, response_local)
        self.message_DB.insert(0, response_DB)
