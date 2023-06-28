from cgitb import handler
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x950+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("app_icon.ico")
        
        
        title_lbl=Label(self.root,text="DEVELOPERS",font=("times new roman",35,"bold"),bg="white",fg="purple") 
        title_lbl.place(x=0,y=0,width=1560,height=40)
        
        # top img
        img_top=Image.open(r"images\image30.jpg")
        img_top=img_top.resize((1560,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1560,height=750)
        
        # frame
        #main_frame=Frame(f_lbl,bd=2,bg="white")
        #main_frame.place(x=1033,y=0,width=500,height=455)
        
        
        
        # developer info
        dev_label=Label(f_lbl,text="Developer 1: Kritika Chauhan",font=("calibri",20,"bold"),bg="white",fg="purple")
        dev_label.place(x=1190,y=5)
        
        dev_label=Label(f_lbl,text="Developer 2: Sakshi Goyal",font=("calibri",20,"bold"),bg="white",fg="purple")
        dev_label.place(x=1190,y=45)
        
        #dev_label=Label(f_lbl,text="Developer 3: Riya Rastogi",font=("calibri",20,"bold"),bg="white",fg="purple")
        #dev_label.place(x=1190,y=85)
        
        
        
        #img1=Image.open(r"images\image28.jpg")
        #img1=img1.resize((500,320),Image.ANTIALIAS)
        #self.photoimg1=ImageTk.PhotoImage(img1)

        #f_lbl=Label(main_frame,image=self.photoimg1)
        #f_lbl.place(x=0,y=210,width=500,height=320)
        
        
if __name__=='__main__':
    root=Tk()
    obj=Developer(root)
    root.mainloop()