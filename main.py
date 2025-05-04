from tkinter import *
from tkinter import ttk


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")  

        # Title Label
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

        #======================== Left Data Frame==========================
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

        comMember=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin","student","faculty")
        comMember.grid(row=0,column=1)

        lblp_no=Label(DataFrameLeft,bg= "powder blue",text="person no:",font=("arial",12,"bold"),padx=2,pady=6)
        lblp_no.grid(row=1,column=0,sticky=W)
        txtp_no=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtp_no.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,bg= "powder blue",text="ID no:",font=("arial",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirst=Label(DataFrameLeft,bg= "powder blue",text="First Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirst.grid(row=3,column=0,sticky=W)
        txtFirst=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtFirst.grid(row=3,column=1)

        lblLast=Label(DataFrameLeft,bg= "powder blue",text="Last Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLast.grid(row=4,column=0,sticky=W)
        txtLast=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtLast.grid(row=4,column=1)

        lbladdress=Label(DataFrameLeft,bg= "powder blue",text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=5,column=0,sticky=W)
        txtaddress=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtaddress.grid(row=5,column=1)

        lbladdress1=Label(DataFrameLeft,bg= "powder blue",text="alternative Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress1.grid(row=6,column=0,sticky=W)
        txtaddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtaddress1.grid(row=6,column=1)
        
        lblPostCode = Label(DataFrameLeft, bg="powder blue", text="Post Code:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile No:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtMobile.grid(row=8, column=1)

        lblBookID = Label(DataFrameLeft, bg="powder blue", text="Book ID:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtBookID.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, bg="powder blue", text="Author:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="Days On Book:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="return fine:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=6, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtDaysOnBook.grid(row=6, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="date over due:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=7, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtDaysOnBook.grid(row=7, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="actual price:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=8, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtDaysOnBook.grid(row=8, column=3)










        # =======================Right Data Frame=====================
        DataFrameRight = LabelFrame(
            frame,
            text="Book Details",
            bg="powder blue",
            fg="black",
            bd=12,
            relief=RIDGE,
            font=("arial", 12, "bold")
        )
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        self.txtbox=Text(DataFrameRight,font=("arial", 12, "bold"),width=32,height=16,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head Firt Book','Learn Python The Hard Way','Python Programming',"Secrete Rahshy",'Python CookBook',
                   'Into to Machine Learning','Fluent Python','Machine tecno','My Python','Joss Ellif guru','Elite Jungle python',
                   'Jungli Python','Mumbai Python','Pune Python','Machine python','Advance Python','Inton Python','RedChilli Python','Ishq Python']
        listbox=Listbox(DataFrameRight,font=("arial", 12, "bold"),width=25,height=16)
        listbox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listbox.yview)

        for item in listBooks:
            listbox.insert(END,item)

      




        

        # Buttons Frame
        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        FrameButton.place(x=0, y=530, width=1530, height=70)
        
        btn_AddData=Button(FrameButton,text='Add data',font=('arial',12,'bold'),width=12,bg='blue',fg='white')
        btn_AddData.grid(row=0, column=0,padx=10)

        btn_showdata=Button(FrameButton,text='show data',font=('arial',12,'bold'),width=12,bg='orange',fg='white')
        btn_showdata.grid(row=0,column=1,padx=10)

        btn_update = Button(FrameButton, text="Update",  font=("arial", 12, "bold"),width=12,bg='green',fg='white')
        btn_update.grid(row=0, column=2, padx=10)

        btn_delete = Button(FrameButton, text="Delete", font=("arial", 12, "bold"),width=12,bg='pink',fg='white')
        btn_delete.grid(row=0, column=3, padx=10)

        btn_reset = Button(FrameButton, text="Reset", font=("arial", 12, "bold"),width=12,bg='yellow',fg='black')
        btn_reset.grid(row=0, column=4, padx=10)

        btn_exit = Button(FrameButton, text="Exit", font=("arial", 12, "bold"), width=12,bg='red',fg='white',command=self.root.quit)
        btn_exit.grid(row=0, column=5, padx=10)






        #infromaton frame
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        self.library_table=ttk.Treeview(Table_frame,column=("memeber type","pno","title",'first'))





    




if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
    