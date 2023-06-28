from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    obj=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x950+0+0")
        self.root.title("Login Page")
        self.root.wm_iconbitmap("app_icon.ico")
        
        
        bg=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\image38.png")
        bg=bg.resize((1560,950),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        #image 1
        img_1=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\image39.jpg")
        img_1=img_1.resize((100,100),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        f_lbl=Label(image=self.photoimg_1,bg="black",borderwidth=0)
        f_lbl.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("calibri",18,"bold"),fg="white",bg="black")
        get_str.place(x=110,y=100)
        
        #labels
        username_label=Label(frame,text="Username",font=("calibri",13,"bold"),fg="white",bg="black")
        username_label.place(x=70,y=155)

        self.textuser=ttk.Entry(frame,font=("calibri",12))
        self.textuser.place(x=40,y=180,width=270)
        
        password_label=Label(frame,text="Password",font=("calibri",13,"bold"),fg="white",bg="black")
        password_label.place(x=70,y=225)

        self.textpass=ttk.Entry(frame,font=("calibri",12), show='*')
        self.textpass.place(x=40,y=250,width=270)
        
        #icons
        img_2=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\image40.jpg")
        img_2=img_2.resize((20,20),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        f_lbl=Label(frame,image=self.photoimg_2,bg="black",borderwidth=0)
        f_lbl.place(x=50,y=155)
        
        img_3=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\image41.png")
        img_3=img_3.resize((20,20),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        f_lbl=Label(frame,image=self.photoimg_3,bg="black",borderwidth=0)
        f_lbl.place(x=50,y=225)
        
        #button
        login_btn=Button(frame,command=self.login,text="Login",width=20,font=("calibri",12,"bold"),bg="orange",fg="black",activebackground="orange",activeforeground="black")
        login_btn.place(x=110,y=300,width=120,height=35)
        
        register_btn=Button(frame,text="New User Register",command=self.register,width=20,font=("calibri",12,"bold"),borderwidth=0,bg="black",fg="orange",activebackground="black",activeforeground="orange")
        register_btn.place(x=30,y=340,width=150,height=35)
        
        forgot_btn=Button(frame,text="Forgot Password?",command=self.forgot_password_window,width=20,font=("calibri",12,"bold"),borderwidth=0,bg="black",fg="orange",activebackground="black",activeforeground="orange")
        forgot_btn.place(x=30,y=365,width=150,height=35)
        
    
    def register(self):
        self.new_win=Toplevel(self.root)
        self.obj=Register_Window(self.new_win)
        
            
    
    def login(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","All fields are required!")
            
        elif self.textuser.get()=="kritika" and self.textpass.get()=="hello":
            messagebox.showinfo("Success","Welcome to the attendance management system!")
        
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Kritika@18',port='3306',database='face_recognition_system')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                self.textuser.get(),
                                                                                self.textpass.get()
                                                                                    ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password!")
            else:
                open_main=messagebox.askyesno("YesNo","Access only authority person?")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
  
# reset password
    def reset_password(self):
        if self.sec_combo.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security_ans.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Kritika@18',port='3306',database='face_recognition_system')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.textuser.get(),self.sec_combo.get(),self.txt_security_ans.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query1=("update register set password=%s where email=%s")
                value1=(self.txt_new_password.get(),self.textuser.get())
                my_cursor.execute(query1,value1)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please Login.",parent=self.root2)
                self.root2.destroy()            
            
            
# forgot password window
    def forgot_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Username Required !!")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Kritika@18',port='3306',database='face_recognition_system')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("Error","Please enter valid username !!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x450+550+170")
                
                l=Label(self.root2,text="Reset Password",font=("calibri",15,"bold"),fg="red")
                l.place(x=0,y=10,relwidth=1)
                
                security_ques=Label(self.root2,text="Select Security Question",font=("calibri",15,"bold"))
                security_ques.place(x=50,y=80)
                
                
                self.sec_combo=ttk.Combobox(self.root2,font=("calibri",13),state="readonly")
                self.sec_combo["values"]=("Select ","What is your Birth Place ?","What is your pet name ?","What is your first school name ?","What is your favourite dish ?")
                self.sec_combo.place(x=50,y=110,width=250)
                self.sec_combo.current(0)
                
                security_ans=Label(self.root2,text="Security Answer",font=("calibri",13,"bold"))
                security_ans.place(x=50,y=150)
                
                self.txt_security_ans=ttk.Entry(self.root2,font=("calibri",13))
                self.txt_security_ans.place(x=50,y=185,width=250)
                
                # reset password
                new_password=Label(self.root2,text="New Password",font=("calibri",15,"bold"))
                new_password.place(x=50,y=240)
                
                self.txt_new_password=ttk.Entry(self.root2,font=("calibri",13), show='*')
                self.txt_new_password.place(x=50,y=265,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("calibri",13,""),fg="white",bg="green")
                btn.place(x=150,y=330,width=100)
                
                
            
class Register_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x950+0+0")
        self.root.title("Register Page")
        
        # variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        #background image
        bg=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\image38.png")
        bg=bg.resize((1560,950),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        #left image
        left_img=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\image42.jpg")
        left_img=left_img.resize((450,570),Image.ANTIALIAS)
        self.left_img=ImageTk.PhotoImage(left_img)
        
        lbl_left_img=Label(self.root,image=self.left_img)
        lbl_left_img.place(x=200,y=120)
        
        # mainframe
        frame=Frame(self.root,bg="#99ffbb")
        frame.place(x=650,y=120,width=710,height=574)
        
        
        register_label=Label(frame,text="REGISTER HERE",font=("calibri",20,"bold"),bg="#99ffbb",fg="#5c00e6")
        register_label.place(x=30,y=20)

        #labels
        fname=Label(frame,text="First Name",font=("calibri",17,"bold"),bg="#99ffbb")
        fname.place(x=60,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("calibri",12))
        fname_entry.place(x=60,y=135,width=200)
        
        
        lname=Label(frame,text="Last Name",font=("calibri",17,"bold"),bg="#99ffbb")
        lname.place(x=310,y=100)
        
        self.text_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("calibri",12))
        self.text_lname.place(x=310,y=135,width=200)
        
        contact=Label(frame,text="Phone No.",font=("calibri",17,"bold"),bg="#99ffbb")
        contact.place(x=60,y=190)
        
        self.text_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("calibri",12))
        self.text_contact.place(x=60,y=225,width=200)
        
        email=Label(frame,text="Email ID",font=("calibri",17,"bold"),bg="#99ffbb")
        email.place(x=310,y=190)
        
        self.text_email=ttk.Entry(frame,textvariable=self.var_email,font=("calibri",12))
        self.text_email.place(x=310,y=225,width=200)
        
        security=Label(frame,text="Security Question",font=("calibri",17,"bold"),bg="#99ffbb")
        security.place(x=60,y=280)
        
        self.text_security=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("calibri",12),state="readonly")
        self.text_security['values']=("Select","What is your Birth Place ?","What is your pet name ?","What is your first school name ?","What is your favourite dish ?")
        self.text_security.place(x=60,y=315,width=200)
        self.text_security.current(0)
        
        security_ans=Label(frame,text="Security Answer",font=("calibri",17,"bold"),bg="#99ffbb")
        security_ans.place(x=310,y=280)
        
        self.text_security_ans=ttk.Entry(frame,textvariable=self.var_securityA,font=("calibri",12))
        self.text_security_ans.place(x=310,y=315,width=200)
        
        passwrd=Label(frame,text="Password",font=("calibri",17,"bold"),bg="#99ffbb")
        passwrd.place(x=60,y=370)
        
        self.text_passwrd=ttk.Entry(frame,textvariable=self.var_pass,font=("calibri",12), show='*')
        self.text_passwrd.place(x=60,y=405,width=200)
        
        confirm_pass=Label(frame,text="Confirm Password",font=("calibri",17,"bold"),bg="#99ffbb")
        confirm_pass.place(x=310,y=370)
        
        self.text_confirm_pass=ttk.Entry(frame,textvariable=self.var_confpass,font=("calibri",12), show='*')
        self.text_confirm_pass.place(x=310,y=405,width=200)
        
        
        #check button
        check_btn=Checkbutton(frame,variable=self.var_check,text="I agree to the terms and conditions.",font=("calibri",12,"bold"),bg="#99ffbb",onvalue=1,offvalue=0)
        check_btn.place(x=60,y=445)
        
        #buttons
        img_btn1=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\register.png")
        img_btn1=img_btn1.resize((200,55),Image.ANTIALIAS)
        self.photoimage_btn1=ImageTk.PhotoImage(img_btn1)

        b1=Button(frame,image=self.photoimage_btn1,command=self.register_data,borderwidth=0, cursor="hand2",bg="#99ffbb",activebackground="#99ffbb")
        b1.place(x=60,y=500,width=200)
        
        img_btn2=Image.open(r"C:\Users\kriti\OneDrive\Desktop\major_project\images\login.PNG")
        img_btn2=img_btn2.resize((200,55),Image.ANTIALIAS)
        self.photoimage_btn2=ImageTk.PhotoImage(img_btn2)
        b2=Button(frame,image=self.photoimage_btn2,command=self.return_login,borderwidth=0,cursor="hand2",bg="#99ffbb",activebackground="#99ffbb")
        b2.place(x=310,y=500,width=200)
        
# function
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required !!",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Passwords do not match !!",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to terms and conditions !!",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Kritika@18',port='3306',database='face_recognition_system')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, Please try another email.",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()
                                                                                    
                                                                                    ))
                messagebox.showinfo("Success","Registered Successfully !!",parent=self.root)    
            conn.commit()
            conn.close()
            
    def return_login(self):
        self.root.destroy()
            

if __name__=='__main__':
    main()        