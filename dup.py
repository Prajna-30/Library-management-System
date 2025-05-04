from tkinter import *
from tkinter import ttk


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")  
        
        lbltitle = Label(
            self.root,
            text="LIBRARY MANAGEMENT SYSTEM",
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
        frame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(frame,
            text="Library Membership Information",
            bg="powder blue",
            fg="black",
            bd=12,
            relief=RIDGE,
            font=("times new roman", 12, "bold")
        )
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember=Label(DataFrameLeft,bg= "powder blue",text="Member Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)



          # Right Data Frame
        DataFrameRight = LabelFrame(
            frame,
            text="Book Details",
            bg="powder blue",
            fg="black",
            bd=12,
            relief=RIDGE,
            font=("times new roman", 12, "bold")
        )
        DataFrameRight.place(x=910, y=5, width=540, height=350)



        #======button=========
        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        FrameButton.place(x=0, y=530, width=1530, height=70)

        #infromaton frame
        meDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        meDetails.place(x=0, y=600, width=1530, height=195)


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()