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

#Entries Frame
entries_frame=Frame(root,bg='#535c68')
entries_frame.pack(side=TOP)
title=Label(entries_frame,text='Unimap Complain System',font=('calibri',18,'bold'),bg='#535c68',fg='white')
title.grid(row=0,cloumnspan=4,padx=10,pady=20)

#Name
lblName=Label(entries_frame,text='Name',font=('calibri',16),bg='#535c68',fg='white')
lblName.grid(row=1,column=0,padx=10,pady=10,sticky='w')
txtName=Entry(entries_frame,textvariable=name,font=('calibri',16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky='w')

#Matric
lblMatric=Label(entries_frame,text='No.Matric',font=('calibri',16),bg='#535c68',fg='white')
lblMatric.grid(row=1,column=2,padx=10,pady=10,sticky='w')
txtMatric=Entry(entries_frame,textvariable=matric,font=('calibri',16),width=30)
txtMatric.grid(row=1,column=3,padx=10,pady=10,sticky='w')

#Email
lblEmail=Label(entries_frame,text='Email',font=('calibri',16),bg='#535c68',fg='white')
lblEmail.grid(row=2,column=0,padx=10,sticky='w')
txtEmail=Entry(entries_frame,textvariable=email,font=('calibri',16),width=30)
txtEmail.grid(row=2,column=1,padx=10,pady=10,sticky='w')

#Address
lblAddress=Label(entries_frame,text='Address',font=('calibri',16),bg='#535c68',fg='white')
lblAddress.grid(row=2,column=2,padx=10,pady=10,sticky='w')
comboAddress=ttk.Combobox(entries_frame,font=('calibri',16),width=28,textvariable=address)
comboAddress['values']=('Pauh Putra','Uniciti','Bumita','Wang Ulu', 'Simpang Ampat','Kubang Gajah')
comboAddress.grid(row=2,column=3,padx=10,sticky='w')

#Gender
lblGender=Label(entries_frame,text='Gender',font=('calibri',16),bg='#535c68',fg='white')
lblGender.grid(row=3,column=0,padx=10,pady=10,sticky='w')
comboGender=ttk.Combobox(entries_frame,font=('calibri',16),width=28,textvariable=gender)
comboGender['values']=('Male','Female')
comboGender.grid(row=3,column=1,padx=10,sticky='w')

#Date
lblDate=Label(entries_frame,text='Date',font=('calibri',16),bg='#535c68',fg='white')
lblDate.grid(row=3,column=2,padx=10,pady=10,sticky='w')
txtDate=Entry(entries_frame,textvariable=date,font=('calibri',16),width=30)
txtDate.grid(row=3,column=3,padx=10,pady=10,sticky='w')

#Complaint\
lblComplaint=Label(entries_frame,text='Complain',font=('calibri',16),bg='#535c68',fg='white')
lblComplaint.grid(row=3,column=3,padx=10,pady=10,sticky='w')

txtComplaint=Text(entries_frame,width=85,height=5,font=('calibri',16))
txtComplaint.grid(row=5,column=0,columnspan=4,padx=10,sticky='w')



root.mainloop()
