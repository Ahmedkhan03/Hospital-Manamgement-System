import time
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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


if __name__ == "__main__":
    root = Tk()
    app = Doctor(root)
    root.mainloop()
