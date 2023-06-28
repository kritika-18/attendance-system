from cgitb import handler
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


mydata=[]  #list to fetch the data of attendance from csv file

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x950+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("app_icon.ico")
        
        # variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        
        #first image
        img=Image.open(r"images\student_1.jpg")
        img=img.resize((520,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=520,height=130)

        #second image
        img1=Image.open(r"images\student_3.jpg")
        img1=img1.resize((520,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=520,y=0,width=520,height=130)
        
        #third image
        img2=Image.open(r"images\student_2.jpg")
        img2=img2.resize((520,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1040,y=0,width=520,height=130)
        
        
        #background image
        img3=Image.open(r"images\image16.png")
        img3=img3.resize((1560,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1560,height=700)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen") 
        title_lbl.place(x=0,y=0,width=1560,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=6,y=50,width=1520,height=610)
        
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students' Attendance Details",font=("calibri",14,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        img_left=Image.open(r"images\student_4.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=715,height=130)
        
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=715,height=410)
        
        # Label and Entry
        #attendance id
        attendanceID_label=Label(left_inside_frame,text="Attendance ID:",font=("calibri",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=17,pady=8,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("calibri",10))
        attendanceID_entry.grid(row=0,column=1,padx=17,pady=8,sticky=W)
        
        #Roll
        rolllabel=Label(left_inside_frame,text="Roll No.:",font=("calibri",12,"bold"),bg="white")
        rolllabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("calibri",10))
        atten_roll.grid(row=0,column=3,pady=8)
        
        #name
        namelabel=Label(left_inside_frame,text="Name:",font=("calibri",12,"bold"),bg="white")
        namelabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("calibri",10))
        atten_name.grid(row=1,column=1,pady=8)
        
        #Department
        deplabel=Label(left_inside_frame,text="Department:",font=("calibri",12,"bold"),bg="white")
        deplabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("calibri",10))
        atten_dep.grid(row=1,column=3,pady=5)
        
        #time
        timelabel=Label(left_inside_frame,text="Time:",font=("calibri",12,"bold"),bg="white")
        timelabel.grid(row=2,column=0)

        attend_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("calibri",10))
        attend_time.grid(row=2,column=1,pady=8)
        
        #date
        datelabel=Label(left_inside_frame,text="Date:",font=("calibri",12,"bold"),bg="white")
        datelabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("calibri",10))
        atten_date.grid(row=2,column=3,pady=8)
        
        #attendance 
        attendancelabel=Label(left_inside_frame,text="Attendance Status:",font=("calibri",12,"bold"),bg="white")
        attendancelabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsans 11 bold",state="readonly")
        self.atten_status["values"]=["Status","Present","Absent"]
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        
        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=360,width=702,height=36)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=28,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=28,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        export_btn.grid(row=0,column=1)

        #upd_btn=Button(btn_frame,text="Update",width=21,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        #upd_btn.grid(row=0,column=2)

        rst_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=28,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        rst_btn.grid(row=0,column=3)
        
        
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("calibri",14,"bold"))
        Right_frame.place(x=750,y=10,width=760,height=580)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=3,width=745,height=540)
        
        # scroll bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)  
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No.")
        self.AttendanceReportTable.heading("name",text="Name")   
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=110)
        self.AttendanceReportTable.column("roll",width=110)
        self.AttendanceReportTable.column("name",width=110)   
        self.AttendanceReportTable.column("department",width=110)
        self.AttendanceReportTable.column("time",width=110)
        self.AttendanceReportTable.column("date",width=110)
        self.AttendanceReportTable.column("attendance",width=110)
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


# fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
# import csv button function
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

# export csv button function
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export !!!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported to "+os.path.basename(fln)+" Successfully !!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
# get cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])   
        self.var_atten_roll.set(rows[1])   
        self.var_atten_name.set(rows[2])   
        self.var_atten_dep.set(rows[3])       
        self.var_atten_time.set(rows[4])   
        self.var_atten_date.set(rows[5])   
        self.var_atten_attendance.set(rows[6])   

         

# reset button function

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")   
        self.var_atten_name.set("")   
        self.var_atten_dep.set("")       
        self.var_atten_time.set("")   
        self.var_atten_date.set("")   
        self.var_atten_attendance.set("")  
        
    
                
        


if __name__=='__main__':
    root=Tk()
    obj=Attendance(root)
    root.mainloop()