from cgitb import handler
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class HelpDesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x950+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("app_icon.ico")
        
        
        #title_lbl=Label(self.root,text="HELPDESK",font=("times new roman",35,"bold"),bg="white",fg="#00b3b3") 
        #title_lbl.place(x=0,y=0,width=1560,height=40)
        
        # top img
        img_top=Image.open(r"images\image36.png")
        img_top=img_top.resize((1560,950),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1560,height=950)
        
        dev_label=Label(f_lbl,text="Email 1: goyalsakshi7200@gmail.com",font=("times new roman",15,"bold"),bg="#e6e6e6",fg="black")
        dev_label.place(x=85,y=280)
        
        dev_label1=Label(f_lbl,text="Email 2: kritich1811@gmail.com",font=("times new roman",15,"bold"),bg="#e6e6e6",fg="black")
        dev_label1.place(x=85,y=320)
        
        
        
        

if __name__=='__main__':
    root=Tk()
    obj=HelpDesk(root)
    root.mainloop()