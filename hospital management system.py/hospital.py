import random
import time
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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




if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()