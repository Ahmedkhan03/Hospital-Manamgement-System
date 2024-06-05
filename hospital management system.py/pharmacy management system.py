import random
import time
import datetime
from tkinter import BOTH, END, GROOVE, LEFT, RIDGE, RIGHT, TOP, X, Y, IntVar, LabelFrame, Text, Tk, Frame, Label, Toplevel, Button, Entry, StringVar, DISABLED, NORMAL, ttk
import tkinter.messagebox

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text="   Pharmacy Management System   ", font=("arial", 40, "bold"), bd=10, relief="sunken")
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.Loginframe1 = Frame(self.frame, width=1000, height=300, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=10, relief="groove")
        self.Loginframe2.grid(row=2, column=0, pady=15)

        self.Loginframe3 = Frame(self.frame, width=1000, height=200, bd=10, relief="groove")
        self.Loginframe3.grid(row=3, column=0, pady=5)

        self.button_reg = Button(self.Loginframe3, text="Patient Registration Window", state=DISABLED, font=("arial", 15, "bold"), command=self.new_window)
        self.button_reg.grid(row=0, column=0, padx=10, pady=10)

        self.button_Hosp = Button(self.Loginframe3, text="Hospital Window", state=DISABLED, font=("arial", 15, "bold"), command=self.hospital_window)
        self.button_Hosp.grid(row=0, column=1, padx=10, pady=10)

        self.button_Dr_appt = Button(self.Loginframe3, text="Doctor Appointment Window", state=DISABLED, font=("arial", 15, "bold"), command=self.dr_appoint_window)
        self.button_Dr_appt.grid(row=0, column=2, padx=10, pady=10)
   
        self.button_med_stock = Button(self.Loginframe3, text="Medicine Stock Window", state=DISABLED, font=("arial", 15, "bold"), command=self.medicine_stock)
        self.button_med_stock.grid(row=0, column=3, padx=10, pady=10)

        self.LabelUsername = Label(self.Loginframe1, text="User Name", font=("arial", 28, "bold"), bd=3)
        self.LabelUsername.grid(row=0, column=0)
        self.textUsername = Entry(self.Loginframe1, font=("arial", 28, "bold"), bd=3, textvariable=self.Username)
        self.textUsername.grid(row=0, column=1, padx=40, pady=15)
       
        self.LabelPassword = Label(self.Loginframe1, text="Password", font=("arial", 28, "bold"), bd=3)
        self.LabelPassword.grid(row=1, column=0)
        self.textPassword = Entry(self.Loginframe1, font=("arial", 28, "bold"), bd=3, textvariable=self.Password, show='*')
        self.textPassword.grid(row=1, column=1, padx=40, pady=15)

        self.button_login = Button(self.Loginframe2, text="Login", width=20, font=("arial", 10, "bold"), command=self.login_system)
        self.button_login.grid(row=0, column=0, padx=10, pady=10)

        self.button_Reset_Credentials = Button(self.Loginframe2, text="Reset Credentials", width=20, font=("arial", 10, "bold"), command=self.reset_credentials)
        self.button_Reset_Credentials.grid(row=1, column=0, padx=10, pady=10)

        self.button_exit = Button(self.Loginframe2, text="Exit", width=20, font=("arial", 10, "bold"), command=self.exit_btn)
        self.button_exit.grid(row=2, column=0, padx=10, pady=10)

    def login_system(self):
        user = self.Username.get()
        pswd = self.Password.get()
        if user == "admin" and pswd == "admin":
            self.button_reg.config(state=NORMAL)
            self.button_Hosp.config(state=NORMAL)
            self.button_Dr_appt.config(state=NORMAL)
            self.button_med_stock.config(state=NORMAL)
            tkinter.messagebox.showinfo("Pharmacy Management System", "Login Successful")
        else:
            tkinter.messagebox.showerror("Pharmacy Management System", "Invalid username or password")
            self.button_reg.config(state=DISABLED)
            self.button_Hosp.config(state=DISABLED)
            self.button_Dr_appt.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()

    def reset_credentials(self):
        self.Username.set("")
        self.Password.set("")
        self.button_reg.config(state=DISABLED)
        self.button_Hosp.config(state=DISABLED)
        self.button_Dr_appt.config(state=DISABLED)
        self.button_med_stock.config(state=DISABLED)
        self.textUsername.focus()

    def exit_btn(self):
        exit_confirmation = tkinter.messagebox.askyesno("Pharmacy Management System", "Are you sure you want to exit?")
        if exit_confirmation:
            self.master.quit()

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app =Hospital(self.newWindow)

    def dr_appoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Doctor(self.newWindow)

    def medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window5(self.newWindow)



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




class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        Ref = StringVar()
        cmbTabletNames = StringVar()
        HospitalCode = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation = StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientID = StringVar()
        PatientNHnumber = StringVar()
        Patientname = StringVar()
        DateofBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()

        def Refrence_numfunc():
            rannumber=random.randint(10000,999999)
            randomnumber=str(rannumber)
            Ref.set(randomnumber)
            return
        
        def prescriptionfunc():
            Refrence_numfunc()
            TextPrescription.insert(END,"Pateint ID:  \t\t"+PatientID.get()+"\n")
            TextPrescription.insert(END,"Pateint Name:  \t\t"+Patientname.get()+"\n")
            TextPrescription.insert(END,"Tablet:  \t\t"+cmbTabletNames.get()+"\n")
            TextPrescription.insert(END,"Daily Dose:  \t\t"+DailyDose.get()+"\n")
            TextPrescription.insert(END,"Issued Date:  \t\t"+IssuedDate.get()+"\n")
            TextPrescription.insert(END,"Expiry Date:  \t\t"+ExpiryDate.get()+"\n")
            TextPrescription.insert(END,"Storage:  \t\t"+StorageAdvice.get()+"\n")
            TextPrescription.insert(END,"More Information:  \t\t"+MoreInformation.get()+"\n")
        def prescriptiondatafunc():
            Refrence_numfunc()
            TextPrescriptionData.insert(
        END,
        Date_of_Registration.get() + "\t" + Ref.get() + "\t\t" + PatientID.get() +
        "\t" + Patientname.get() + "\t\t" + DateofBirth.get() + "\t\t" + cmbTabletNames.get() +
        "\t\t" + IssuedDate.get() + "\t\t" + ExpiryDate.get() + "\t\t" + DailyDose.get() +
        "\t\t" + StorageAdvice.get() + "\t\t" + PatientID.get() + "\n"
    )

        def exitbtn():
            exitbtn=tkinter.messagebox.askyesno("Hospital Management System","Are u sure u want to exit?")
            if exitbtn>0:
                root.destroy()
                return
        def deletefunc():
            
       
         Ref .set("")
         cmbTabletNames .set("")
         HospitalCode .set("")
         Lot .set("")
         IssuedDate .set("")
         ExpiryDate .set("")
         DailyDose .set("")
         SideEffects .set("")
         MoreInformation .set("")
         StorageAdvice .set("")
         Medication .set("")
         PatientID .set("")
         PatientNHnumber .set("")
         Patientname .set("")
         DateofBirth .set("")
         PatientAddress .set("")
         Prescription .set("")
         NHSnumber .set("")
         TextPrescription.delete("1.0",END)
         TextPrescriptionData.delete("1.0",END)
         return
        def resetfunc():
             Ref .set("")
             cmbTabletNames .set("")
             HospitalCode .set("")
             Lot .set("")
             IssuedDate .set("")
             ExpiryDate .set("")
             DailyDose .set("")
             SideEffects .set("")
             MoreInformation .set("")
             StorageAdvice .set("")
             Medication .set("")
             PatientID .set("")
             PatientNHnumber .set("")
             Patientname .set("")
             DateofBirth .set("")
             PatientAddress .set("")
             Prescription .set("")
             NHSnumber .set("")
             
             
             return




        title = Label(self.root, text="Hospital Management System", font=("monotype corsiva", 42, "bold"),
                      bd=5, relief=GROOVE, bg="#2ab8b8", fg="black")
        title.pack(side=TOP, fill=X)

        Manage_Frame = Frame(self.root, width=1510, height=400, bd=5, relief=RIDGE, bg="#0099cc")
        Manage_Frame.place(x=10, y=80)

        Button_Frame = Frame(self.root, width=1510, height=55, bd=4, relief=RIDGE, bg="#328695")
        Button_Frame.place(x=10, y=460)

        Date_Frame = LabelFrame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg="#266e73")
        Date_Frame.place(x=10, y=510)

        Date_FrameLeft = LabelFrame(Manage_Frame, width=1050, text="General Information",
                                    font=("arial", 20, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Date_FrameLeft.pack(side=LEFT)

        Date_FrameRight = LabelFrame(Manage_Frame, width=1050, text="Prescription",
                                     font=("arial", 15, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Date_FrameRight.pack(side=RIGHT)

        Date_FrameData = LabelFrame(Date_Frame, width=1050, text="Prescription Data", font=("arial", 12, "italic"),
                                    height=390, bd=4, relief=RIDGE, bg="#3eb7bb")
        Date_FrameData.pack(side=LEFT)

        # Labels and Entries for General Information
        Datelbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date", padx=2, bg="#0099cc")
        Datelbl.grid(row=0, column=0, padx=10, pady=5, sticky="W")
        Datetxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Date_of_Registration)
        Datetxt.grid(row=0, column=1, padx=10, pady=5, sticky="E")

        Reflbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Reference Number", padx=2, bg="#0099cc")
        Reflbl.grid(row=1, column=0, padx=10, pady=5, sticky="W")
        Reftxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=27,state=DISABLED, textvariable=Ref)
        Reftxt.grid(row=1, column=1, padx=10, pady=5, sticky="E")

        PatientIDlbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient ID", padx=2, bg="#0099cc")
        PatientIDlbl.grid(row=2, column=0, padx=10, pady=5, sticky="W")
        PatientIDtxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientID)
        PatientIDtxt.grid(row=2, column=1, padx=10, pady=5, sticky="E")

        Patientnamelbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Name", padx=2, bg="#0099cc")
        Patientnamelbl.grid(row=3, column=0, padx=10, pady=5, sticky="W")
        Patientnametxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Patientname)
        Patientnametxt.grid(row=3, column=1, padx=10, pady=5, sticky="E")

        DateofBirthlbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of Birth", padx=2, bg="#0099cc")
        DateofBirthlbl.grid(row=4, column=0, padx=10, pady=5, sticky="W")
        DateofBirthtxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=DateofBirth)
        DateofBirthtxt.grid(row=4, column=1, padx=10, pady=5, sticky="E")

        PatientAddresslbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Address", padx=2, bg="#0099cc")
        PatientAddresslbl.grid(row=5, column=0, padx=10, pady=5, sticky="W")
        PatientAddresstxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientAddress)
        PatientAddresstxt.grid(row=5, column=1, padx=10, pady=5, sticky="E")

        NHSnumberlbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="NHS Number", padx=2, bg="#0099cc")
        NHSnumberlbl.grid(row=6, column=0, padx=10, pady=5, sticky="W")
        

        NHSnumbertxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=NHSnumber)
        NHSnumbertxt.grid(row=6, column=1, padx=10, pady=5, sticky="E")

        Tabletlbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Tablet", padx=2, bg="#0099cc")
        Tabletlbl.grid(row=7, column=0, padx=10, pady=5, sticky="W")
        Tabletcmb = ttk.Combobox(Date_FrameLeft, textvariable=cmbTabletNames, width=25, state="readonly",
                                 font=("arial", 12, "bold"))
        Tabletcmb['values'] = ("", "Paracetamol", "Dan-p", "Dio-l", "Calpol", "Amlodipine", "Noxion",
                               "Singulair", "Plavix", "Gochi", "Death")
        Tabletcmb.current(0)
        Tabletcmb.grid(row=7, column=1, padx=10, pady=5)

        No_of_Tabletslbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Number Of Tablets", padx=2, bg="#0099cc")
        No_of_Tabletslbl.grid(row=8, column=0, padx=10, pady=5, sticky="W")
        No_of_Tabletsrtxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Ref)
        No_of_Tabletsrtxt.grid(row=8, column=1, padx=10, pady=5, sticky="E")

        HospitalCodelbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Hospital Code", padx=2, bg="#0099cc")
        HospitalCodelbl.grid(row=0, column=2, padx=10, pady=5, sticky="W")
        HospitalCodetxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=HospitalCode)
        HospitalCodetxt.grid(row=0, column=3, padx=10, pady=5, sticky="E")

        StorageAdvicelbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Storage Advice", padx=2, bg="#0099cc")
        StorageAdvicelbl.grid(row=1, column=2, padx=10, pady=5, sticky="W")

        StorageAdvicecmb = ttk.Combobox(Date_FrameLeft, textvariable=StorageAdvice, width=25, state="readonly",
                                        font=("arial", 12, "bold"))
        StorageAdvicecmb['values'] = ("", "Under Room Temperature", "Below 5°C", "Refrigeration")
        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row=1, column=3, padx=10, pady=5, sticky="E")

        Medicationlbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Medication", padx=2, bg="#0099cc")
        Medicationlbl.grid(row=2, column=2, padx=10, pady=5, sticky="W")
        Medicationtxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=Medication)
        Medicationtxt.grid(row=2, column=3, padx=10, pady=5, sticky="E")

        DailyDoselbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Daily Dose", padx=2, bg="#0099cc")
        DailyDoselbl.grid(row=3, column=2, padx=10, pady=5, sticky="W")
        DailyDosetxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=DailyDose)
        DailyDosetxt.grid(row=3, column=3, padx=10, pady=5, sticky="E")

        SideEffectslbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Side Effects", padx=2, bg="#0099cc")
        SideEffectslbl.grid(row=4, column=2, padx=10, pady=5, sticky="W")
        SideEffectstxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=SideEffects)
        SideEffectstxt.grid(row=4, column=3, padx=10, pady=5, sticky="E")

        MoreInformationlbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="More Information", padx=2, bg="#0099cc")
        MoreInformationlbl.grid(row=5, column=2, padx=10, pady=5, sticky="W")
        MoreInformationtxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=MoreInformation)
        MoreInformationtxt.grid(row=5, column=3, padx=10, pady=5, sticky="E")

        # Labels and Entries for Prescription Data
        Prescriptionlbl = Label(Date_FrameData, font=("arial", 12, "bold"), width=20, text="Prescription", padx=2, bg="#3eb7bb")
        Prescriptionlbl.grid(row=0, column=0, padx=10, pady=5, sticky="W")
        Prescriptiontxt = Entry(Date_FrameData, font=("arial", 12, "bold"), width=30, textvariable=Prescription)
        Prescriptiontxt.grid(row=0, column=1, padx=10, pady=5, sticky="W")


        Lotlbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Lot Number", padx=2, bg="#0099cc")
        Lotlbl.grid(row=6, column=2, padx=10, pady=5, sticky="W")
        Lottxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=Lot)
        Lottxt.grid(row=6, column=3, padx=10, pady=5, sticky="E")

        IssuedDatelbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of Issue", padx=2, bg="#0099cc")
        IssuedDatelbl.grid(row=7, column=2, padx=10, pady=5, sticky="W")
        IssuedDatetxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=IssuedDate)
        IssuedDatetxt.grid(row=7, column=3, padx=10, pady=5, sticky="E")

        ExpiryDatelbl = Label(Date_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of Expiry", padx=2, bg="#0099cc")
        ExpiryDatelbl.grid(row=8, column=2, padx=10, pady=5, sticky="W")
        ExpiryDatetxt = Entry(Date_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=ExpiryDate)
        ExpiryDatetxt.grid(row=8, column=3, padx=10, pady=5, sticky="E")

        TextPrescription=Text(Date_FrameRight,font=("arail",12,"bold"),width=55,height=17,padx=3,
            pady=5)
        TextPrescription.grid(row=0,column=0)



        TextPrescriptionData=Text(Date_FrameData,font=("arail",12,"bold"),width=203,height=12)
        TextPrescriptionData.grid(row=1,column=0)


        Prescriptionbtn = Button(Button_Frame, text="Prescription", bg="#ffaab0", activebackground="#fcceb2",
                         font=("arial", 15, "bold"), width=19)
        Prescriptionbtn.grid(row=0, column=1, padx=15)

        Receiptbtn = Button(Button_Frame, text="Prescription Data", bg="#ffaab0", activebackground="#fcceb2",
                    font=("arial", 15, "bold"), width=19, command=prescriptiondatafunc)  # Corrected here
        Receiptbtn.grid(row=0, column=2, padx=15)

        Resetbtn = Button(Button_Frame, text="Reset", bg="#ffaab0", activebackground="#fcceb2",
                  font=("arial", 15, "bold"), width=19, command=resetfunc)
        Resetbtn.grid(row=0, column=3, padx=15)

        Deletebtn = Button(Button_Frame, text="Delete", bg="#ffaab0", activebackground="#fcceb2",
                   font=("arial", 15, "bold"), width=19, command=deletefunc)
        Deletebtn.grid(row=0, column=4, padx=15)

        Exitbtn = Button(Button_Frame, text="Exit", bg="#ffaab0", activebackground="#fcceb2",
                 font=("arial", 15, "bold"), width=19, command=exitbtn)
        Exitbtn.grid(row=0, column=5, padx=15)


        prescriptiondatarow=Label(Date_FrameData,bg="white",font=("arial",12,"bold"),
        text="Date\tRefrence Id\tPatient Name\tDate of Birth\tNHS number\tTablets\tIssued date\tExpiry Date\tDaily Dose\tStorage Advice\tPatient Id")
        prescriptiondatarow.grid(row=0,column=0,sticky="W")



class Doctor:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="#b7d8d6")

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%Y"))
        DrId = StringVar()
        Drname = StringVar()
        DateofBirth = StringVar()
        Spec = StringVar()
        GovtPri = StringVar()
        Surgeries = StringVar()
        Experiences = StringVar()
        Nurses = StringVar()
        DrMobile = StringVar()
        PtName = StringVar()
        Appttime = StringVar()
        PtAge = StringVar()
        PatientAddress = StringVar()
        PtMobile = StringVar()
        Disease = StringVar()
        Case = StringVar()
        BenifitCard = StringVar()

        self.variables = [DrId, Drname, DateofBirth, Spec, GovtPri, Surgeries, Experiences, Nurses, DrMobile,
                          Date_of_Registration, PtName, Appttime, PtAge, PatientAddress, PtMobile, Disease,
                          Case, BenifitCard]

        title = Label(self.root, text="Doctor Management System", font=("monotype corsiva", 42, "bold"), bd=5,
                      relief=GROOVE, bg="#b7d8d6", fg="black")
        title.pack(side=TOP, fill=X)

        Manage_Frame = Frame(self.root, width=1510, height=400, bd=5, relief=RIDGE, bg="#0789e9")
        Manage_Frame.place(x=10, y=80)

        Button_Frame = Frame(self.root, width=1510, height=55, bd=4, relief=RIDGE, bg="#0789e9")
        Button_Frame.place(x=10, y=480)

        Data_Frame = Frame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg="#0789e9")
        Data_Frame.place(x=10, y=540)

        Data_FrameLeft = LabelFrame(Manage_Frame, width=1050, text="General Information",
                                    font=("arial", 20, "italic"), height=390, bd=7, pady=1, relief=RIDGE,
                                    bg="#789e9e")
        Data_FrameLeft.pack(side=LEFT, fill=Y)

        Data_FrameRight = LabelFrame(Manage_Frame, width=450, text="Doctor's Details",
                                     font=("arial", 12, "italic"), height=390, bd=7, relief=RIDGE, bg="white")
        Data_FrameRight.pack(side=RIGHT, fill=Y)

        Data_FrameBottom = LabelFrame(Data_Frame, width=1500, text="Patient's Information",
                                      font=("arial", 15, "italic"), height=260, bd=7, relief=RIDGE, bg="#b7d8d6")
        Data_FrameBottom.pack(fill=BOTH, expand=True)

        labels_texts = [
            "Doctor Id", "Doctor Name", "Date of Birth", "Specification", "Govt/Private", "Total Surgeries",
            "Experiences in years", "Nurses under Dr", "Doctor mobile no", "Date", "Patient Name",
            "Appointment Time", "Patient Age", "Patient Address", "Patient Mobile no", "Patient Disease",
            "Case", "Benifit Card"
        ]

        for i in range(9):
            lbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text=labels_texts[i], bg="#789e9e")
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky="W")
            txt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.variables[i])
            txt.grid(row=i, column=1, padx=10, pady=5, sticky="E")

        for i in range(9, 18):
            lbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text=labels_texts[i], bg="#789e9e")
            lbl.grid(row=i - 9, column=2, padx=10, pady=5, sticky="W")
            txt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.variables[i])
            txt.grid(row=i - 9, column=3, padx=10, pady=5, sticky="E")

        # Buttons
        btn_width = 15
        Prescriptionbtn = Button(Button_Frame, text="Patient Information", bg="#fe615a", activebackground="#cc6686",
                                 font=("arial", 15, "bold"), width=btn_width, command=self.show_patient_info)
        Prescriptionbtn.grid(row=0, column=0, padx=5)

        DoctorDetailsbtn = Button(Button_Frame, text="Doctor Details", bg="#fe615a", activebackground="#cc6686",
                                  font=("arial", 15, "bold"), width=btn_width, command=self.show_doctor_details)
        DoctorDetailsbtn.grid(row=0, column=1, padx=5)

        Resetbtn = Button(Button_Frame, text="Reset", bg="#fe615a", activebackground="#cc6686",
                          font=("arial", 15, "bold"), width=btn_width, command=self.reset_fields)
        Resetbtn.grid(row=0, column=2, padx=5)

        Deletebtn = Button(Button_Frame, text="Delete", bg="#fe615a", activebackground="#cc6686",
                           font=("arial", 15, "bold"), width=btn_width, command=self.delete_record)
        Deletebtn.grid(row=0, column=3, padx=5)

        Exitbtn = Button(Button_Frame, text="Exit", bg="#fe615a", activebackground="#cc6686",
                         font=("arial", 15, "bold"), width=btn_width, command=self.confirm_exit)
        Exitbtn.grid(row=0, column=4, padx=5)

    def confirm_exit(self):
        if tkinter.messagebox.askyesno("Doctor Management System", "Do you want to exit?"):
            self.root.quit()

    def reset_fields(self):
        for variable in self.variables:
            variable.set("")

    def delete_record(self):
        if tkinter.messagebox.askyesno("Doctor Management System", "Do you want to delete this record?"):
            # Here you can add the code to delete the record from your database or perform any other action
            self.reset_fields()

    def show_patient_info(self):
        tkinter.messagebox.showinfo("Patient Information", "This button will show patient information.")

    def show_doctor_details(self):
        tkinter.messagebox.showinfo("Doctor Details", "This button will show doctor details.")


class Window5:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()       

def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == "__main__":
    main()
