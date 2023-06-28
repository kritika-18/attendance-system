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


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x950+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("app_icon.ico")
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("ariel",35,"bold"),bg="white",fg="darkblue") 
        title_lbl.place(x=0,y=0,width=1560,height=45)
        
         # first img
        img_top=Image.open(r"images\image27.jpeg")
        img_top=img_top.resize((830,755),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=830,height=755)
        
        
        #second img
        img_bottom=Image.open(r"images\image26.jpg")
        img_bottom=img_bottom.resize((830,755),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=790,y=45,width=830,height=755)
        
        #button
        b1_1=Button(f_lbl,text="Recognise",cursor="hand2",command=self.face_recog,font=("ariel",20,"bold"),bg="green",fg="white")
        b1_1.place(x=315,y=665,width=200,height=40)
        
        
        
    # attendance mark function
    def mark_attendance(self,i,r,n,d):
        with open ("attendance_Report/attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")          
        
        
    # face recog function
    def face_recog(self): 
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbours)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                ids,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host='localhost',username='root',password='Kritika@18',port='3306',database='face_recognition_system',auth_plugin = "mysql_native_password")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where ID="+str(ids))
                n=my_cursor.fetchone()
                n="+".join(n)     # to concatenate string with id variable
                
                my_cursor.execute("select Roll_no from student where ID="+str(ids))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dept from student where ID="+str(ids))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                
                my_cursor.execute("select ID from student where ID="+str(ids))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll No.:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,h]
                
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)    #0 for the web cam and 1 for other cam
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Recognising..",img)
            
            #if cv2.waitKey(1)==13:
             #   break
            key = cv2.waitKey(1)
             
            if cv2.getWindowProperty("Recognising..", cv2.WND_PROP_VISIBLE) <1:
                break
        
        video_cap.release()
        cv2.destroyAllWindows()
                            
                    
if __name__=='__main__':
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()