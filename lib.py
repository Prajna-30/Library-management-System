from tkinter import *

# ================== Role Selection Window ==================
class RoleSelection:
    def __init__(self, root):
        self.root = root
        self.root.title("Select Role")
        self.root.geometry("400x200")

        Label(root, text="Select Role", font=("Arial", 20, "bold")).pack(pady=20)

        Button(root, text="Admin", width=20, font=("Arial", 12), command=self.open_admin).pack(pady=10)
        Button(root, text="User", width=20, font=("Arial", 12), command=self.open_user).pack(pady=10)

    def open_admin(self):
        self.root.destroy()
        root_admin = Tk()
        AdminInterface(root_admin)
        root_admin.mainloop()

    def open_user(self):
        self.root.destroy()
        root_user = Tk()
        UserInterface(root_user)
        root_user.mainloop()

# ================== Admin Interface ==================
class AdminInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System - Admin")
        self.root.geometry("1250x800+0+0")  

        # Title Label
        lbltitle = Label(
            self.root,
            text="LIBRARY MANAGEMENT SYSTEM - ADMIN",
            bg='powder blue',
            fg='green',
            bd=20,
            relief=RIDGE,
            font=("times new roman", 50, "bold"),
            padx=2,
            pady=6
        )
        lbltitle.pack(side=TOP, fill=X)

        # Main Frame
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1230, height=400)

        # Left Data Frame
        DataFrameLeft = LabelFrame(
            frame,
            text="Library Membership Information",
            bg="powder blue",
            fg="green",
            bd=12,
            relief=RIDGE,
            font=("times new roman", 12, "bold")
        )
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        # Right Data Frame
        DataFrameRight = LabelFrame(
            frame,
            text="Book Details",
            bg="powder blue",
            fg="green",
            bd=12,
            relief=RIDGE,
            font=("times new roman", 12, "bold")
        )
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        # Buttons Frame
        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        FrameButton.place(x=0, y=530, width=1230, height=70)

        # Information frame
        meDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        meDetails.place(x=0, y=600, width=1230, height=195)

        # Example Buttons
        btn_add = Button(FrameButton, text="Add", width=12, font=("times new roman", 12, "bold"))
        btn_add.grid(row=0, column=0, padx=10)

        btn_update = Button(FrameButton, text="Update", width=12, font=("times new roman", 12, "bold"))
        btn_update.grid(row=0, column=1, padx=10)

        btn_delete = Button(FrameButton, text="Delete", width=12, font=("times new roman", 12, "bold"))
        btn_delete.grid(row=0, column=2, padx=10)

        btn_reset = Button(FrameButton, text="Reset", width=12, font=("times new roman", 12, "bold"))
        btn_reset.grid(row=0, column=3, padx=10)

        btn_exit = Button(FrameButton, text="Exit", width=12, font=("times new roman", 12, "bold"), command=self.root.quit)
        btn_exit.grid(row=0, column=4, padx=10)


# ================== User Interface ==================
class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System - User")
        self.root.geometry("800x500")

        # Title
        lbl = Label(self.root, text="Welcome to Library (User View)", font=("Arial", 24, "bold"), fg="green")
        lbl.pack(pady=20)

        # Search Section
        self.search_frame = Frame(self.root)
        self.search_frame.pack(pady=20)

        lbl_search = Label(self.search_frame, text="Search Book", font=("Arial", 14))
        lbl_search.grid(row=0, column=0, padx=10)

        self.search_entry = Entry(self.search_frame, font=("Arial", 12))
        self.search_entry.grid(row=0, column=1, padx=10)

        search_button = Button(self.search_frame, text="Search", font=("Arial", 12), command=self.search_book)
        search_button.grid(row=0, column=2, padx=10)

        self.result_label = Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Borrow Section
        self.borrow_frame = Frame(self.root)
        self.borrow_frame.pack(pady=20)

        lbl_borrow = Label(self.borrow_frame, text="Borrow Book", font=("Arial", 14))
        lbl_borrow.grid(row=0, column=0, padx=10)

        self.borrow_entry = Entry(self.borrow_frame, font=("Arial", 12))
        self.borrow_entry.grid(row=0, column=1, padx=10)

        borrow_button = Button(self.borrow_frame, text="Borrow", font=("Arial", 12), command=self.borrow_book)
        borrow_button.grid(row=0, column=2, padx=10)

        # Return Section
        self.return_frame = Frame(self.root)
        self.return_frame.pack(pady=20)

        lbl_return = Label(self.return_frame, text="Return Book", font=("Arial", 14))
        lbl_return.grid(row=0, column=0, padx=10)

        self.return_entry = Entry(self.return_frame, font=("Arial", 12))
        self.return_entry.grid(row=0, column=1, padx=10)

        return_button = Button(self.return_frame, text="Return", font=("Arial", 12), command=self.return_book)
        return_button.grid(row=0, column=2, padx=10)

        # Exit Button
        btn_exit = Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 12), width=10)
        btn_exit.pack(pady=20)

    def search_book(self):
        # Dummy search logic (can be replaced with real database query)
        book = self.search_entry.get()
        if book:
            self.result_label.config(text=f"Book '{book}' found in the library.")
        else:
            self.result_label.config(text="Please enter a book name to search.")

    def borrow_book(self):
        # Dummy borrow logic (can be replaced with real borrow system)
        book = self.borrow_entry.get()
        if book:
            self.result_label.config(text=f"Book '{book}' has been borrowed.")
        else:
            self.result_label.config(text="Please enter a book name to borrow.")

    def return_book(self):
        # Dummy return logic (can be replaced with real return system)
        book = self.return_entry.get()
        if book:
            self.result_label.config(text=f"Book '{book}' has been returned.")
        else:
            self.result_label.config(text="Please enter a book name to return.")


# ================== Start App ==================
if __name__ == "__main__":
    root = Tk()
    RoleSelection(root)
    root.mainloop()
