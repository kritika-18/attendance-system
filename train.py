from cgitb import handler
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x950+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("app_icon.ico")
        
        #top image
        img_top=Image.open(r"images\image23.jpg")
        img_top=img_top.resize((1560,380),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1560,height=380)
        
        #train button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("ariel",25,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=380,width=1560,height=60)
        
        #bottom image
        img_bottom=Image.open(r"images\image24.jpeg")
        img_bottom=img_bottom.resize((1560,380),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1560,height=380)
        
        
    def train_classifier(self):
        data_dir=("datasets")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')  #gray scale conversion
            image_np=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training..",image_np)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
        
     #======train the classifier and saving it into a file===
     
        clf=cv2.face.LBPHFaceRecognizer_create()   #install "pip install opencv-contrib-python" package for this line
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Datasets trained successfully!")
        
if __name__=='__main__':
    root=Tk()
    obj=Train(root)
    root.mainloop()