from cgitb import handler
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from student import Student
from train import Train
import os
from face_recognition import Face_Recognition
from attendances import Attendance
from developer import Developer
from helpdesk import HelpDesk
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x950+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("app_icon.ico")

        #first image
        img=Image.open(r"images\image3.jpg")
        img=img.resize((520,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=520,height=130)

        #second image
        img1=Image.open(r"images\image5.jpg")
        img1=img1.resize((520,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=520,y=0,width=520,height=130)

        #third image
        img2=Image.open(r"images\image4.jpg")
        img2=img2.resize((520,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1040,y=0,width=520,height=130)

        #background image
        img3=Image.open(r"images\image7.jpg")
        img3=img3.resize((1560,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1560,height=700)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("ariel",35,"bold"),bg="white",fg="red") 
        title_lbl.place(x=0,y=0,width=1560,height=45)   
        
        # time 
        def time():
            string = strftime('%H:%M %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='black')
        lbl.place(x=0,y=0,width=100,height=60)
        time()    

        #student button
        img4=Image.open(r"images\image2.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("ariel",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=200,height=40)

        #detect face button
        img5=Image.open(r"images\image8.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=200,height=200)

        b2_1=Button(bg_img,text="Detect Face",cursor="hand2",command=self.face_data,font=("ariel",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=200,height=40)

        #attendance
        img6=Image.open(r"images\image9.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=200,height=200)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("ariel",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=200,height=40)

        #helpdesk
        img7=Image.open(r"images\image10.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.helpdesk_data)
        b4.place(x=1100,y=100,width=200,height=200)

        b4_1=Button(bg_img,text="Helpdesk",cursor="hand2",command=self.helpdesk_data,font=("ariel",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=200,height=40)

        #train face button
        img8=Image.open(r"images\image11.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=200,height=200)

        b5_1=Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data,font=("ariel",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=580,width=200,height=40)

        #photo button
        img9=Image.open(r"images\image14.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_images)
        b6.place(x=500,y=380,width=200,height=200)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_images,font=("ariel",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=500,y=580,width=200,height=40)

        #exit
        img10=Image.open(r"images\image13.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.exit)
        b7.place(x=800,y=380,width=200,height=200)

        b7_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("ariel",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=800,y=580,width=200,height=40)

        #developers
        img11=Image.open(r"images\image12.jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b8.place(x=1100,y=380,width=200,height=200)

        b8_1=Button(bg_img,text="Developers",cursor="hand2",command=self.developer_data,font=("ariel",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1100,y=580,width=200,height=40)


    def open_images(self):
        os.startfile("datasets")
        
        
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit?",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return
    
    #function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)   
        
    def helpdesk_data(self):
        self.new_window=Toplevel(self.root)
        self.app=HelpDesk(self.new_window) 
        

if __name__=='__main__':
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
