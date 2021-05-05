from tkinter import *
import qrcode
import image
from PIL import Image,ImageTk
from resizeimage import resizeimage


class Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x550+200+50")
        self.root.title("QR Generator")
        self.root.resizable(False, False)

        title = Label(self.root, text="QR Generartor", font=("times new roman", 40),
                      bg='#053246', fg='white', anchor='center').place(x=0, y=0, relwidth=1)
        # ---------------window about the student details

        self.stud_name = StringVar()
        self.stud_Roll = IntVar()
        self.stud_year = StringVar()
        self.stud_Branch = StringVar()
        self.stud_adress = StringVar()
        self.stud_college = StringVar()

        stud_Frame = Frame(self.root, bd=3, relief=RIDGE, bg='white')
        stud_Frame.place(x=50, y=100, width=500, height=400)
        stud_title = Label(stud_Frame, text="Student Details", font=("goudy old style", 20),
                           bg='#043256', fg='white', anchor='center').place(x=0, y=0, relwidth=1)
        lbl_name = Label(stud_Frame, text="Name ", font=("times new roman", 15, 'bold'),
                         bg='white',).place(x=50, y=60)
        lbl_Roll_NO = Label(stud_Frame, text="Roll No ", font=("times new roman", 15, 'bold'),
                            bg='white',).place(x=50, y=100)
        lbl_Branch = Label(stud_Frame, text="Branch ", font=("times new roman", 15, 'bold'),
                           bg='white',).place(x=50, y=140)
        lbl_year = Label(stud_Frame, text="year ", font=("times new roman", 15, 'bold'),
                         bg='white',).place(x=50, y=180)
        lbl_address = Label(stud_Frame, text="Address ", font=("times new roman", 15, 'bold'),
                            bg='white',).place(x=50, y=220)
        lbl_college = Label(stud_Frame, text="College  ", font=("times new roman", 15, 'bold'),
                            bg='white',).place(x=50, y=260)

        text_name = Entry(stud_Frame, font=("times new roman", 15,), textvariable=self.stud_name,
                          bg='lightgrey').place(x=150, y=60)
        text_Roll_NO = Entry(stud_Frame, font=("times new roman", 15,),textvariable=self.stud_Roll,
                             bg='lightgrey').place(x=150, y=100)
        text_Branch = Entry(stud_Frame,  font=("times new roman", 15,), textvariable=self.stud_Branch,
                            bg='lightgrey').place(x=150, y=140)
        text_year = Entry(stud_Frame,  font=("times new roman", 15,), textvariable=self.stud_year,
                          bg='lightgrey').place(x=150, y=180)
        text_address = Entry(stud_Frame, font=("times new roman", 15,), textvariable=self.stud_adress,
                             bg='lightgrey').place(x=150, y=220)
        text_college = Entry(stud_Frame, font=("times new roman", 15,), textvariable=self.stud_college,
                             bg='lightgrey').place(x=150, y=260)
        btn_generate = Button(stud_Frame, text="QR Generate", command=self.generate, font=(
            "timmes new roman", 18, 'bold'), bg="#2196f3", fg="white").place(x=90, y=300, width=160, height=30)
        btn_clear = Button(stud_Frame, text="Clear",command=self.clear, font=("timmes new roman", 18, 'bold'),
                           bg="#607d8b", fg="white").place(x=300, y=300, width=80, height=30)

        self.msg = ''
        self.lbl_msg = Label(stud_Frame, text=self.msg, font=("times new roman", 18),
                             bg='white', fg="green")
        self.lbl_msg.place(x=0, y=350, relwidth=1)

        # ---------------window about the QR code
        QR_Frame = Frame(self.root, bd=3, relief=RIDGE, bg='white')
        QR_Frame.place(x=600, y=100, width=300, height=400)
        QR_title = Label(QR_Frame, text="Student QR code", font=("goudy old style", 20),
                         bg='#043256', fg='white', anchor='center').place(x=0, y=0, relwidth=1)

        self.qr_code = Label(QR_Frame, text="No QR  \n Available ", font=(
            'timmes new roman', 15), bg='#3f51b5', fg="white")
        self.qr_code.place(x=45, y=100, width=180, height=200)

   

    def generate(self):
        if (self.stud_name.get() == '' or self.stud_Roll.get() == '' or self.stud_Branch.get() == '' or self.stud_year.get() == '' or self.stud_adress.get() == '' or self.stud_college.get() == ''):
            self.msg = 'ALL Fields are Required!!!'
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            #__update
            qr_data=(f"Student Name:{self.stud_name.get()}\n Student Roll No:{self.stud_Roll.get()}\nStudent Branch :{ self.stud_Branch.get()}\nStudent year :{self.stud_year.get()}\nStudent Address:{self.stud_adress.get()}\nCollege Name:{self.stud_college.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_data)  
            qr_code=resizeimage.resize_cover(qr_code,[200,200])
            qr_code.save("QR Code/Stud_"+str(self.stud_Roll.get())+'.png')  
            #      update the image
            self.im=ImageTk.PhotoImage(file="QR Code/Stud_"+str(self.stud_Roll.get())+'.png')  #file = storage of  QR code 
            self.qr_code.config(image=self.im) 
            self.msg = 'QR Generated Successfull!!!!'
            self.lbl_msg.config(text=self.msg, fg="green")
    def clear(self):
        self.stud_name.set('')
        self.stud_Roll.set('')
        self.stud_year.set('')
        self.stud_Branch.set('')
        self.stud_adress.set('')
        self.stud_college.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        

root = Tk()
obj = Generator(root)
root.mainloop()
