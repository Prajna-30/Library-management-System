from tkinter import *
from tkinter import ttk

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="lightblue")

        # Title Label
        lbltitle = Label(
            self.root,
            text="LIBRARY MANAGEMENT SYSTEM",
            bg='lightseagreen',
            fg='white',
            bd=20,
            relief=RIDGE,
            font=("Arial Black", 30, "bold"),
            padx=2,
            pady=10
        )
        lbltitle.pack(side=TOP, fill=X)

        # Main Frame
        frame = Frame(self.root, bd=10, relief=RIDGE, padx=10, bg="lightblue")
        frame.place(x=10, y=100, width=1330, height=380)

        # Left Data Frame
        DataFrameLeft = LabelFrame(
            frame,
            text="Library Membership Information",
            bg="lightblue",
            fg="darkgreen",
            bd=8,
            relief=GROOVE,
            font=("Arial", 14, "bold")
        )
        DataFrameLeft.place(x=10, y=10, width=880, height=360)

        # --- Column 0/1: Membership & Personal Info ---
        labels = [
            ("Member Type:", 0), ("PRN No:", 1), ("ID No:", 2),
            ("First Name:", 3), ("Last Name:", 4), ("Address 1:", 5),
            ("Address 2:", 6), ("Post Code:", 7), ("Mobile No:", 8)
        ]
        for text, row in labels:
            lbl = Label(DataFrameLeft, bg="lightblue", text=text,
                        font=("Arial", 12, "bold"), padx=2, pady=4)
            lbl.grid(row=row, column=0, sticky=W, padx=5, pady=5)
            if text == "Member Type:":
                widget = ttk.Combobox(
                    DataFrameLeft, font=("Arial", 12, "bold"),
                    width=25, state="readonly"
                )
                widget['values'] = ("Admin", "Student", "Faculty")
                widget.current(0)
            else:
                widget = Entry(DataFrameLeft, font=("Arial", 12, "bold"), width=27)
            widget.grid(row=row, column=1, padx=5, pady=5)

        # --- Column 2/3: Book Info ---
        book_labels = [
            ("Book ID:", 0), ("Book Title:", 1), ("Author Name:", 2),
            ("Date Borrowed:", 3), ("Date Due:", 4),
            ("Late Return Fine:", 5), ("Date Over Due:", 6),
            ("Days On Book:", 7), ("Actual Price:", 8)
        ]
        for text, row in book_labels:
            lbl = Label(DataFrameLeft, bg="lightblue", text=text,
                        font=("Arial", 12, "bold"), padx=2, pady=4)
            lbl.grid(row=row, column=2, sticky=W, padx=5, pady=5)
            txt = Entry(DataFrameLeft, font=("Arial", 12, "bold"), width=27)
            txt.grid(row=row, column=3, padx=5, pady=5)

        # Right Data Frame
        DataFrameRight = LabelFrame(
            frame,
            text="Book Details",
            bg="lightblue",
            fg="darkgreen",
            bd=8,
            relief=GROOVE,
            font=("Arial", 14, "bold")
        )
        DataFrameRight.place(x=900, y=10, width=420, height=360)

        self.book_details_display = Text(DataFrameRight, font=("Arial", 12), width=40, height=16)
        self.book_details_display.pack(padx=10, pady=10)

        # Buttons Frame
        FrameButton = Frame(self.root, bd=10, relief=RIDGE, padx=10, bg='lightblue')
        FrameButton.place(x=10, y=490, width=1330, height=60)

        btn_specs = [
            ("Add New", "lightgreen"), ("Update", "lightgreen"),
            ("Delete", "lightcoral"), ("Reset", "gold"), ("Exit", "red")
        ]
        for idx, (text, color) in enumerate(btn_specs):
            cmd = self.root.quit if text == "Exit" else None
            btn = Button(
                FrameButton, text=text, width=12,
                font=("Arial", 12, "bold"), bg=color, fg="black",
                command=cmd
            )
            btn.grid(row=0, column=idx, padx=10, pady=5)

        # Information Frame
        FrameInfo = Frame(self.root, bd=10, relief=RIDGE, padx=10, bg='lightblue')
        FrameInfo.place(x=10, y=560, width=1330, height=120)
        self.info_display = Text(FrameInfo, font=("Arial", 10), width=130, height=5)
        self.info_display.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
