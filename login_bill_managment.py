from tkinter import *
from tkinter import messagebox

def login():
    user = username.get()
    code = password.get()
    
    if user == "Anit" and code == "2838":
        root = Toplevel(screen)
        root.title("Bill")
        root.geometry("1280x720+150+80")
        root.configure(bg="#d7dae2")
        root.resizable(False, False)
        
        def Reset():
            entry_Idli.delete(0, END)
            entry_Cookies.delete(0, END)
            entry_Tea.delete(0, END)
            entry_Cofee.delete(0, END)
            entry_Juice.delete(0, END)
            entry_Cake.delete(0, END)
            entry_Pastry.delete(0, END)
            Total_bill.set("")

        def Total():
            try:
                a1 = int(Idli.get())
            except:
                a1 = 0
            try:
                a2 = int(Cookies.get())
            except:
                a2 = 0
            try:
                a3 = int(Tea.get())
            except:
                a3 = 0
            try:
                a4 = int(Cofee.get())
            except:
                a4 = 0
            try:
                a5 = int(Juice.get())
            except:
                a5 = 0
            try:
                a6 = int(Cake.get())
            except:
                a6 = 0
            try:
                a7 = int(Pastry.get())
            except:
                a7 = 0

            c1 = 60 * a1
            c2 = 30 * a2
            c3 = 6 * a3
            c4 = 80 * a4
            c5 = 20 * a5
            c6 = 150 * a6
            c7 = 45 * a7

            totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7
            string_bill = "RS. " + str('%.2f' % totalcost)
            Total_bill.set(string_bill)

        Idli = StringVar()
        Cookies = StringVar()
        Tea = StringVar()
        Cofee = StringVar()
        Juice = StringVar()
        Cake = StringVar()
        Pastry = StringVar()
        Total_bill = StringVar()

        Label(root, text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri", 33), width=300, height=2).pack()

        f = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
        f.place(x=10, y=118)

        Label(f, text="Menu", font=("Gabriola", 40, "bold"), fg="black", bg="lightgreen").place(x=80, y=0)

        Label(f, font=("Lucida calligraphy", 15, 'bold'), text="Idli.....Rs.60/plate", fg="black", bg="lightgreen").place(x=10, y=80)
        Label(f, font=("Lucida calligraphy", 15, 'bold'), text="Cookies.....Rs.30/plate", fg="black", bg="lightgreen").place(x=10, y=110)
        Label(f, font=("Lucida calligraphy", 15, 'bold'), text="Tea.....Rs.6/plate", fg="black", bg="lightgreen").place(x=10, y=140)
        Label(f, font=("Lucida calligraphy", 15, 'bold'), text="Coffee.....Rs.80/plate", fg="black", bg="lightgreen").place(x=10, y=170)
        Label(f, font=("Lucida calligraphy", 15, 'bold'), text="Juice.....Rs.20/plate", fg="black", bg="lightgreen").place(x=10, y=200)
        Label(f, font=("Lucida calligraphy", 15, 'bold'), text="Cake.....Rs.150/plate", fg="black", bg="lightgreen").place(x=10, y=230)
        Label(f, font=("Lucida calligraphy", 15, 'bold'), text="Pastry.....Rs.45/plate", fg="black", bg="lightgreen").place(x=10, y=260)

        f2 = Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=370)
        f2.place(x=690, y=118)

        Label(f2, text="Bill", font=('calibri', 20), bg="lightyellow").place(x=120, y=10)

        lbl_total = Label(f2, font=('aria', 20, 'bold'), text="Total", width=16, fg="lightyellow", bg="black")
        lbl_total.place(x=0, y=50)

        entry_total = Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
        entry_total.place(x=20, y=100)

        f1 = Frame(root, bd=5, height=370, width=300, relief=RAISED)
        f1.place(x=350, y=118)  # Corrected the placement

        lbl_Idli = Label(f1, font=("arial", 20, 'bold'), text="Idli", width=12, fg="blue4")
        lbl_Cookies = Label(f1, font=("arial", 20, 'bold'), text="Cookies", width=12, fg="blue4")
        lbl_Tea = Label(f1, font=("arial", 20, 'bold'), text="Tea", width=12, fg="blue4")
        lbl_Cofee = Label(f1, font=("arial", 20, 'bold'), text="Coffee", width=12, fg="blue4")
        lbl_Juice = Label(f1, font=("arial", 20, 'bold'), text="Juice", width=12, fg="blue4")
        lbl_Cake = Label(f1, font=("arial", 20, 'bold'), text="Cake", width=12, fg="blue4")
        lbl_Pastry = Label(f1, font=("arial", 20, 'bold'), text="Pastry", width=12, fg="blue4")

        lbl_Idli.grid(row=1, column=0)
        lbl_Cookies.grid(row=2, column=0)
        lbl_Tea.grid(row=3, column=0)
        lbl_Cofee.grid(row=4, column=0)
        lbl_Juice.grid(row=5, column=0)
        lbl_Cake.grid(row=6, column=0)
        lbl_Pastry.grid(row=7, column=0)

        entry_Idli = Entry(f1, font=("arial", 20, 'bold'), textvariable=Idli, bd=6, width=8, fg="lightpink")
        entry_Cookies = Entry(f1, font=("arial", 20, 'bold'), textvariable=Cookies, bd=6, width=8, fg="lightpink")
        entry_Tea = Entry(f1, font=("arial", 20, 'bold'), textvariable=Tea, bd=6, width=8, fg="lightpink")
        entry_Cofee = Entry(f1, font=("arial", 20, 'bold'), textvariable=Cofee, bd=6, width=8, fg="lightpink")
        entry_Juice = Entry(f1, font=("arial", 20, 'bold'), textvariable=Juice, bd=6, width=8, fg="lightpink")
        entry_Cake = Entry(f1, font=("arial", 20, 'bold'), textvariable=Cake, bd=6, width=8, fg="lightpink")
        entry_Pastry = Entry(f1, font=("arial", 20, 'bold'), textvariable=Pastry, bd=6, width=8, fg="lightpink")

        entry_Idli.grid(row=1, column=1)
        entry_Cookies.grid(row=2, column=1)
        entry_Tea.grid(row=3, column=1)
        entry_Cofee.grid(row=4, column=1)
        entry_Juice.grid(row=5, column=1)
        entry_Cake.grid(row=6, column=1)
        entry_Pastry.grid(row=7, column=1)

        btn_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=("arial", 16, 'bold'), width=10, text="Reset", command=Reset)
        btn_reset.grid(row=8, column=0)

        btn_total = Button(f1, bd=5, fg="black", bg="lightblue", font=("arial", 16, 'bold'), width=10, text="Total", command=Total)
        btn_total.grid(row=8, column=1)

    elif user == "" and code == "":
        messagebox.showerror("Invalid", "Please enter username and Password")
    elif user == "":
        messagebox.showerror("Invalid", "Username is required")
    elif code == "":
        messagebox.showerror("Invalid", "Password is required")
    elif user != "parvat":
        messagebox.showerror("Invalid", "Please enter a valid username")
    elif code != "1234":
        messagebox.showerror("Invalid", "Please enter a valid Password")

def main_screen():
    global screen
    global username
    global password

    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")

    image_icon = PhotoImage(file="login.png")
    screen.iconphoto(False, image_icon)
    screen.title("Login System")

    lblTitle = Label(text="Login System", font=("arial", 50, 'bold'), fg="black", bg="#d7dae2")
    lblTitle.pack(pady=50)

    bordercolor = Frame(screen, bg="black", width=800, height=400)
    bordercolor.pack()

    mainframe = Frame(bordercolor, bg="#d7dae2", width=800, height=400)
    mainframe.pack(padx=20, pady=20)

    Label(mainframe, text="Username", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="Password", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)

    username = StringVar()
    password = StringVar()

    entry_username = Entry(mainframe, textvariable=username, width=12, bd=2, font=("arial", 30))
    entry_username.place(x=400, y=50)
    entry_password = Entry(mainframe, textvariable=password, width=12, bd=2, font=("arial", 30), show="*")
    entry_password.place(x=400, y=150)

    def reset():
        entry_username.delete(0, END)
        entry_password.delete(0, END)

    Button(mainframe, text="Login", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=login).place(x=100, y=250)
    Button(mainframe, text="Reset", height="2", width=23, bg="#1089ff", fg="white", bd=0, command=reset).place(x=300, y=250)
    Button(mainframe, text="Exit", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=screen.destroy).place(x=500, y=250)

    screen.mainloop()

if __name__ == "__main__":
    main_screen()
