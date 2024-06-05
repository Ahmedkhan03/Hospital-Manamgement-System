import random
import time
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1358x750+0+8")
        self.root.configure(background="black")

        # Initialize StringVar for Date_of_Registration
        self.Date_of_Registration = StringVar()
        self.Date_of_Registration.set(time.strftime("%d/%m/%y"))

        self.Ref = StringVar()
        self.Mobile_no = StringVar()
        self.Pincode = StringVar()
        self.Address = StringVar()
        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.Gender = StringVar()
        self.ID_Proof = StringVar()
        self.Member_Type = StringVar()
        self.var5 = IntVar()
        self.Payment_Method = StringVar()
        self.Membership_Fee = StringVar()

        self.Membership = StringVar()
        self.Membership.set("0")

        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno("Member Registration Form", "Are you sure you want to exit?")
            if exitbtt > 0:
                root.destroy()
                return

        def resetbtt():
            self.Ref.set("")
            self.Mobile_no.set("")
            self.Pincode.set("")
            self.Address.set("")
            self.Firstname.set("")
            self.Lastname.set("")
            self.Gender.set("")
            self.ID_Proof.set("")
            self.Member_Type.set("")
            self.Payment_Method.set("")
            self.Membership_Fee.set("")
            self.Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            payment_method_cmb.current(0)

        def reeesetbtt():
            reesetbtt = tkinter.messagebox.askokcancel("Member Registration Form", "You want to add a new record")
            if reeesetbtt > 0:
                resetbtt()
                detail_labeltxt.delete("1.0", END)
            elif reeesetbtt <= 0:
                resetbtt()
                return

        def Refrence_number():
            rannumber = random.randint(10000, 9999999)
            randomnumber = str(rannumber)
            self.Ref.set(randomnumber)

        def membership_fee():
            if self.var5.get() == 1:
                self.member_Membership.configure(state=NORMAL)
                item = float(15000)
                self.Membership.set(str(item) + "Rs")
            elif self.var5.get() == 0:
                self.member_Membership.configure(state=DISABLED)
                self.Membership.set("0")

        def receipt():
            Refrence_number()
            detail_labeltxt.insert(END, self.Date_of_Registration.get().ljust(10) + 
                                   self.Ref.get().ljust(10) + 
                                   self.Firstname.get().ljust(12) + 
                                   self.Lastname.get().ljust(12) + 
                                   self.Mobile_no.get().ljust(12) + 
                                   self.Address.get().ljust(15) + 
                                   self.Pincode.get().ljust(8) + 
                                   self.Gender.get().ljust(8) + 
                                   self.Member_Type.get().ljust(10) + "\n", 'bold')

        title = Label(self.root, text="Member Registration Form", font=("Monotype Corsiva", 30, "bold"), bd=5,
                      relief=GROOVE, bg="#E6005C", fg="#000000")
        title.pack(side=TOP, fill=X)

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#001a66")
        Manage_Frame.place(x=20, y=100, width=450, height=630)

        detail_frame = Frame(self.root, relief=RIDGE, bg="#001a66")
        detail_frame.place(x=480, y=100, width=850, height=630)

        Cus_title = Label(Manage_Frame, text="Customer Detail", font=("Arial", 20, "bold"), bg="#001a66", fg="white")
        Cus_title.grid(row=0, columnspan=2, pady=5)

        memeber_datelb1 = Label(Manage_Frame, text="Date", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        memeber_datelb1.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        memeber_datetxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=self.Date_of_Registration)
        memeber_datetxt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        member_reflbl = Label(Manage_Frame, text="Reference ID", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_reflbl.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        memeber_reftxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), state=DISABLED, textvariable=self.Ref)
        memeber_reftxt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        memeber_fnamelb1 = Label(Manage_Frame, text="First Name", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        memeber_fnamelb1.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        memeber_fnametxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=self.Firstname)
        memeber_fnametxt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        memeber_lnamelb1 = Label(Manage_Frame, text="Last Name", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        memeber_lnamelb1.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        memeber_lnametxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=self.Lastname)
        memeber_lnametxt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        memeber_mobilelb1 = Label(Manage_Frame, text="Mobile No", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        memeber_mobilelb1.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        memeber_mobiletxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=self.Mobile_no)
        memeber_mobiletxt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        memeber_addresslb1 = Label(Manage_Frame, text="Address", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        memeber_addresslb1.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        memeber_addresstxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=self.Address)
        memeber_addresstxt.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        memeber_pincodelb1 = Label(Manage_Frame, text="Pincode", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        memeber_pincodelb1.grid(row=7, column=0, pady=5, padx=10, sticky="w")

        memeber_pincodetxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=self.Pincode)
        memeber_pincodetxt.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        memeber_genderlb1 = Label(Manage_Frame, text="Gender", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        memeber_genderlb1.grid(row=8, column=0, pady=5, padx=10, sticky="w")
        member_gendercmb = ttk.Combobox(Manage_Frame, textvariable=self.Gender, state="readonly", font=("Arial", 15, "bold"), width=19)
        member_gendercmb['values'] = ("Male", "Female", "Other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8, column=1, pady=5, padx=10, sticky="w")

        memeber_id_prooflb1 = Label(Manage_Frame, text="ID Proof", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        memeber_id_prooflb1.grid(row=9, column=0, pady=5, padx=10, sticky="w")
        member_id_proofcmb = ttk.Combobox(Manage_Frame, textvariable=self.ID_Proof, state="readonly", font=("Arial", 15, "bold"), width=19)
        member_id_proofcmb['values'] = ("Shinakhti Card", "Passport", "Driving License", "Pan Card", "Student ID")
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        member_memtypelb1 = Label(Manage_Frame, text="Member Type", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_memtypelb1.grid(row=10, column=0, pady=5, padx=10, sticky="w")
        member_memtypecmb = ttk.Combobox(Manage_Frame, textvariable=self.Member_Type, state="readonly", font=("Arial", 15, "bold"), width=19)
        member_memtypecmb['values'] = ("Standard", "Premium", "VIP")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        # Payment Details
        payment_title = Label(Manage_Frame, text="Payment Details", font=("Arial", 20, "bold"), bg="#001a66", fg="white")
        payment_title.grid(row=11, columnspan=2, pady=10)

        payment_method_lbl = Label(Manage_Frame, text="Payment Method", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        payment_method_lbl.grid(row=12, column=0, pady=5, padx=10, sticky="w")
        payment_method_cmb = ttk.Combobox(Manage_Frame, textvariable=self.Payment_Method, state="readonly", font=("Arial", 15, "bold"), width=19)
        payment_method_cmb['values'] = ("Cash", "Card")
        payment_method_cmb.current(0)
        payment_method_cmb.grid(row=12, column=1, pady=5, padx=10, sticky="w")

        membership_fee_lbl = Label(Manage_Frame, text="Membership Fee", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        membership_fee_lbl.grid(row=13, column=0, pady=5, padx=10, sticky="w")
        membership_fee_txt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=self.Membership_Fee)
        membership_fee_txt.grid(row=13, column=1, pady=5, padx=10, sticky="w")

        detail_label = Label(detail_frame, font=("Courier", 11, "bold"), pady=10, padx=2, width=105,
                             text="Date".ljust(10) + "Ref Id".ljust(10) + "First Name".ljust(12) + 
                                  "Last Name".ljust(12) + "Mobile No".ljust(12) + 
                                  "Address".ljust(15) + "Pincode".ljust(8) + 
                                  "Gender".ljust(8) + "Member Type".ljust(10))
        detail_label.grid(row=0, column=0, columnspan=4, sticky="w")

        detail_labeltxt = Text(detail_frame, width=115, height=34, font=("Courier", 8))
        detail_labeltxt.grid(row=1, column=0, columnspan=4)

        detail_labeltxt.tag_configure('bold', font=("Courier", 8, "bold"))

        receiptbtn = Button(detail_frame, padx=15, bd=5, font=("Arial", 12, "bold"),
                            bg="#ff9966", width=20, text="Receipt", command=receipt)
        receiptbtn.grid(row=2, column=0)

        exitbtn = Button(detail_frame, padx=15, bd=5, font=("Arial", 12, "bold"),
                         bg="#ff9966", width=20, text="Exit", command=exitbtt)
        exitbtn.grid(row=2, column=1)

        resetbtn = Button(detail_frame, padx=15, bd=5, font=("Arial", 12, "bold"),
                          bg="#ff9966", width=20, text="Reset", command=reeesetbtt)
        resetbtn.grid(row=2, column=2)

if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
