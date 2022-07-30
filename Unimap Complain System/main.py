from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from db import Database

#Configure
db=Database('Complaints.db')
root=Tk()
root.title('Unimap Complain System')
root.geometry('1920x1080+0+0')
root.config(bg='#2c3e50')
root.state('zoomed')
#Put your image file location in (r'') to run
root.iconbitmap(r'C:\\Users\\SYAHMI EDRI\\Desktop\\Unimap Complain System\\unimap.ico')
#Put your image file location in (Image.open()) to run
img1=ImageTk.PhotoImage(Image.open('C:\\Users\\SYAHMI EDRI\\Desktop\\Unimap Complain System\\unimap.jpg'))
imgdisplay=Label(root,image=img1)
imgdisplay.pack(side=RIGHT)
#Put your image file location in (Image.open()) to run
img2=ImageTk.PhotoImage(Image.open('C:\\Users\\SYAHMI EDRI\\Desktop\\Unimap Complain System\\unimap.jpg'))
imgdisplay=Label(root,image=img2)
imgdisplay.pack(side=LEFT)

#Variable
name=StringVar()
matric=StringVar()
email=StringVar()
address=StringVar()
gender=StringVar()
date=StringVar()

root.mainloop()
