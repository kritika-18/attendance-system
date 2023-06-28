from cgitb import handler
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x950+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("app_icon.ico")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_section=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        #first image
        img=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\student_1.jpg")
        img=img.resize((520,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=520,height=130)

        #second image
        img1=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\student_3.jpg")
        img1=img1.resize((520,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=520,y=0,width=520,height=130)

        #third image
        img2=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\student_2.jpg")
        img2=img2.resize((520,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1040,y=0,width=520,height=130)

        #background image
        img3=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\image7.jpg")
        img3=img3.resize((1560,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1560,height=700)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("ariel",35,"bold"),bg="white",fg="darkblue") 
        title_lbl.place(x=0,y=0,width=1560,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=6,y=55,width=1520,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("calibri",14,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\student_4.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=715,height=130)

        
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("calibri",14,"bold"))
        current_course_frame.place(x=5,y=135,width=715,height=115)

        #course
        course_label=Label(current_course_frame,text="Course",font=("calibri",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("calibri",10),width=17,state="readonly")
        course_combo["values"]=("Select Course","B.Tech.","M.Tech.","B.Sc.","M.Sc.","BBA","MBA","BCA","MCA","Others")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("calibri",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("calibri",10),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CSE","Mechanical","IT","BioTech.","Civil","None(if course other than B.Tech./M.Tech)","Others")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("calibri",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("calibri",10),width=17,state="readonly")
        year_combo["values"]=("Select Year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        sem_label=Label(current_course_frame,text="Semester",font=("calibri",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("calibri",10),width=17,state="readonly")
        sem_combo["values"]=("Select semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information 
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("calibri",14,"bold"))
        class_student_frame.place(x=5,y=260,width=715,height=285)

        #student id
        studentID_label=Label(class_student_frame,text="Student ID",font=("calibri",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("calibri",10))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_student_frame,text=" Student Name",font=("calibri",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("calibri",10))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #section
        section_label=Label(class_student_frame,text=" Section",font=("calibri",12,"bold"),bg="white")
        section_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        section_combo=ttk.Combobox(class_student_frame,textvariable=self.var_section,font=("calibri",10),width=18,state="readonly")
        section_combo["values"]=("Select section","A","B","C","D","E","F","G","H","I","J")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=9,pady=7,sticky=W)

        #roll no
        roll_no_label=Label(class_student_frame,text=" Roll No.",font=("calibri",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("calibri",10))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text=" Gender",font=("calibri",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("calibri",10),width=18,state="readonly")
        gender_combo["values"]=("Select gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=9,pady=7,sticky=W)

        #dob
        dob_label=Label(class_student_frame,text=" DOB",font=("calibri",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("calibri",10))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_student_frame,text=" Email ID",font=("calibri",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("calibri",10))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_label=Label(class_student_frame,text=" Mobile",font=("calibri",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("calibri",10))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(class_student_frame,text=" Address",font=("calibri",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("calibri",10))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher
        teacher_label=Label(class_student_frame,text=" Teacher",font=("calibri",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("calibri",10))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=7,column=0)


        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=7,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=196,width=704,height=30)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=20,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        save_btn.grid(row=0,column=0)

        upd_btn=Button(btn_frame,text="Update",command=self.update_data,width=21,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        upd_btn.grid(row=0,column=1)

        dlt_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=21,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        dlt_btn.grid(row=0,column=2)

        rst_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=21,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        rst_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=2,y=226,width=704,height=30)
        
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=42,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        take_photo_btn.grid(row=0,column=0)

        upde_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=44,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        upde_photo_btn.grid(row=0,column=1)


        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students' Details",font=("calibri",14,"bold"))
        Right_frame.place(x=750,y=10,width=760,height=580)

        img_right=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\student_5.jpg")
        img_right=img_right.resize((742,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=6,y=0,width=742,height=130)

        #search system
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("calibri",14,"bold"))
        search_frame.place(x=5,y=135,width=742,height=70)

        search_label=Label(search_frame,text=" Search By",font=("calibri",12,"bold"),bg="#fefbd8")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("calibri",10),width=17,state="readonly")
        search_combo["values"]=("Select","Roll No","Name","Student ID","Phone no","Email ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("calibri",10))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #buttons
        search_btn=Button(search_frame,text="Search",width=18,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,text="Show All",width=18,font=("calibri",12,"bold"),bg="#87bdd8",fg="black")
        showall_btn.grid(row=0,column=4,padx=4)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=135,width=742,height=410)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","ID","Name","Section","Roll no","Gender","DOB","Email ID","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="Student ID")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Roll no",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email ID",text="Email ID")
        self.student_table.heading("Phone",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Roll no",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email ID",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    
    #========add data into database========

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_id.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error"," All fields are required.",parent=self.root)
        else:
            
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='Kritika@18',port='3306',database='face_recognition_system',auth_plugin = "mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    #==========================fetch data=================
    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='Kritika@18',port='3306',database='face_recognition_system',auth_plugin = "mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
    #=======get cursor========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
        
        
    #=====update data====
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_id.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error"," All fields are required.",parent=self.root)
            
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student's details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='Kritika@18',port='3306',database='face_recognition_system',auth_plugin = "mysql_native_password")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll_no=%s,Gender=%s,DOB=%s,EmailID=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(
                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                        self.var_course.get(),
                                                                                                                                                        self.var_year.get(),
                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                        self.var_name.get(),
                                                                                                                                                        self.var_section.get(),
                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_address.get(),
                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                        self.var_id.get()

                                                                                                                                                        
                                                                                                                                                        ))
                
                else:
                    if not Update:
                        return
                    
                messagebox.showinfo("Success","Student details updated successfully!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                

    #=====delete button====
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID is required.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Student's Details","Do you want to delete this student's details?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='Kritika@18',port='3306',database='face_recognition_system',auth_plugin = "mysql_native_password")
                    my_cursor=conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                    
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted","Students's details deleted successfully!")    
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

             
    #======reset button=====
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_section.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    
    ########Generate data set#######
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_id.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error"," All fields are required.",parent=self.root)
            
        else:
            try:
                
                conn=mysql.connector.connect(host='localhost',user='root',password='Kritika@18',port='3306',database='face_recognition_system',auth_plugin = "mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for i in my_result:
                    id+=1
                my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll_no=%s,Gender=%s,DOB=%s,EmailID=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(
                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                        self.var_course.get(),
                                                                                                                                                        self.var_year.get(),
                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                        self.var_name.get(),
                                                                                                                                                        self.var_section.get(),
                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_address.get(),
                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                        self.var_id.get()==id+1

                                                                                                                                                        
                                                                                                                                                        ))
                
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #=======load predefined data on face frontals from opencv=====
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3 (by default)
                    #minimun neighbour=5 (by default)
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)  #opens web camera
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="datasets/student."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:    #stops after collecting 100 samples or pressing enter
                        break 
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success","Datasets generated successfully!")  
                    
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                
 
 
if __name__=='__main__':
    root=Tk()
    obj=Student(root)
    root.mainloop()