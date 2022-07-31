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

#Image
'''#Put your image file location in (r'') to run
root.iconbitmap(r'C:\\Users\\SYAHMI EDRI\\Desktop\\Unimap Complain System\\unimap.ico')
#Put your image file location in (Image.open()) to run
img1=ImageTk.PhotoImage(Image.open('C:\\Users\\SYAHMI EDRI\\Desktop\\Unimap Complain System\\unimap.jpg'))
imgdisplay=Label(root,image=img1)
imgdisplay.pack(side=RIGHT)
#Put your image file location in (Image.open()) to run
img2=ImageTk.PhotoImage(Image.open('C:\\Users\\SYAHMI EDRI\\Desktop\\Unimap Complain System\\unimap.jpg'))
imgdisplay=Label(root,image=img2)
imgdisplay.pack(side=LEFT)'''

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
title.grid(row=0,columnspan=4,padx=10,pady=20)

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
lblComplaint.grid(row=4,column=0,padx=10,pady=10,sticky='w')

txtComplaint=Text(entries_frame,width=85,height=5,font=('calibri',16))
txtComplaint.grid(row=5,column=0,columnspan=4,padx=10,sticky='w')

#function get data
def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row 
    row=data["values"]
    name.set(row[1])
    matric.set(row[2])
    email.set(row[3])
    address.set(row[4])
    gender.set(row[5])
    date.set(row[6])
    txtComplaint.delete(1.0,END)
    txtComplaint.insert(END,row[7])

#function display
def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

#function add complaint
def add_complaint():
    if txtName.get()=="" or txtMatric.get()=="" or txtEmail.get()=="" or comboAddress.get()=="" or comboGender.get=="" or txtDate.get()=="" or txtComplaint.get(
        1.0,END)=="":
        messagebox.showerror("Error in Input", "Please Fill All the Detail")
        return
    db.insert(txtName.get(),txtMatric.get(),txtEmail.get(),comboAddress.get(),comboGender.get(),txtDate.get(),txtComplaint.get(1.0,END))
    messagebox.showinfo('Success', 'Complain Submitted')
    clear_input()
    displayAll()

#function edit complain
def edit_complaint():
    if txtName.get()=="" or txtMatric.get()=="" or txtEmail.get()=="" or comboAddress.get()=="" or comboGender.get=="" or txtDate.get()=="" or txtComplaint.get(
        1.0,END)=="":
        messagebox.showerror("Error in Input", "Please Fill All the Detail")
        return
    db.update(row[0],txtName.get(),txtMatric.get(),txtEmail.get(),comboAddress.get(),comboGender.get(),txtDate.get(),txtComplaint.get(1.0,END))
    messagebox.showinfo('Success', 'Complain Edited')
    clear_input()
    displayAll()

#function delete complain
def delete_complaint():
    db.remove(row[0])
    clear_input()
    displayAll()

#function clear exist input
def clear_input():
    name.set("")
    matric.set("")
    email.set("")
    address.set("")
    gender.set("")
    date.set("")
    txtComplaint.delete(1.0,END)

#frame for button
btn_frame=Frame(entries_frame,bg='#535c68')
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky='w')

#Button to add complain
btnAdd=Button(btn_frame,command=add_complaint,text='Add Complain',width=15,font=('calibri',16,'bold'),fg='white',bg='#16a085',bd=0).grid(row=0,column=0,padx=10)

#Button to clear exist input
btnClear=Button(btn_frame,command=clear_input,text='Clear Input', width=15,font=('calibri',16,'bold'),fg='white',bg='#f39c12',bd=0).grid(row=0,column=1,padx=10)

#Button to edit exist complain
btnEdit=Button(btn_frame,command=edit_complaint,text='Edit Complaint',width=15,font=('calibri',16,'bold'),fg='white',bg='#2680b9',bd=0).grid(row=0,column=2,padx=10)

#Button to delete complain
btnDelete=Button(btn_frame,command=delete_complaint,text='Delete Complaint',width=15,font=('calibri',16,'bold'),fg='white',bg='#c0392b',bd=0).grid(row=0,column=3,padx=10)


   
#Table Frame for database
tree_frame=Frame(root,bg='#ecf0f1')
tree_frame.place(x=0,y=480,width=1540,height=520)
style=ttk.Style()
style.configure('mystyle.Treeview',font=('calibri',18),rowheight=70)
style.configure('mystyle.Treeview.Heading',font=('calibri',18))

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style='mystyle.Treeview')
tv.heading('1',text='ID')
tv.column('1',width=5)
tv.heading('2',text='Name')
tv.heading('3',text='No.Matric')
tv.heading('4',text='Email')
tv.heading('5',text='Address')
tv.column('5',width=5)
tv.heading('6',text='Gender')
tv.column('6',width=5)
tv.heading('7',text='Date')
tv.column('7',width=5)
tv.heading('8',text='Complaint')
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

displayAll()
root.mainloop()