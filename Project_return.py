from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import ImageTk,Image
from tkcalendar import DateEntry
import mysql.connector
def returnbook():
    try:
        #global vr,vr1,vr2,vr3,vr4,vr5,vr6,vr7,vr8,vr9,vr10,vr11,inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12
        global vr1,vr2,vr4,vr6,inp2,inp3,inp5,inp7
        rootreturn=Toplevel()
        rootreturn.title("RETURN BOOKS")
        rootreturn.state('zoomed')
        #rootreturn.geometry("1370x710+0+0")
        rootreturn.config(bg="#b3b3b3")
   
        frame=Frame(rootreturn,bg="#e6e6e6",bd=25,relief=RIDGE,padx=20)
        frame1=Frame(rootreturn,bg="#ff3300")
        frame1.place(x=25,y=25,width=1320,height=40)
        l=Label(rootreturn,text="*Complete the required details:-",font=("Microsoft New Tai Lue",15,"bold"),bg="#ff3300",fg="white")
        l.place(x=28,y=28)

        #vr=StringVar()
        vr1=IntVar()
        vr2=StringVar()
        #vr3=StringVar()
        vr4=IntVar()
        #vr5=StringVar()
        vr6=StringVar()
        #vr7=StringVar()
        #vr8=StringVar()
        #vr9=IntVar()
        #vr10=StringVar()
        #vr11=IntVar()

        '''lt1=Label(rootreturn,bg="#e6e6e6",text="Name(Student):",font=("Franklin Gothic Demi Cond",18))
        lt1.place(x=80,y=110)
        lt11=Label(rootreturn,bg="#e6e6e6",text="(book returned by whom)",font=("Franklin Gothic Demi Cond",13),fg="red")
        lt11.place(x=80,y=145)
        inp1=Entry(rootreturn,width=35,font=("Calibri (Body)",15),textvariable=vr)
        inp1.place(x=235,y=120)'''

        lt2=Label(rootreturn,bg="#e6e6e6",text="ID(Student)",font=("Franklin Gothic Demi Cond",15))
        lt2.place(x=60,y=100)
        inp2=Entry(rootreturn,width=30,font=("Calibri (Body)",15),textvariable=vr1)
        inp2.place(x=215,y=100)

        lt2=Label(rootreturn,bg="#e6e6e6",text="ID(Book)",font=("Franklin Gothic Demi Cond",15))
        lt2.place(x=60,y=170)
        inp7=Entry(rootreturn,width=30,font=("Calibri (Body)",15),textvariable=vr6)
        inp7.place(x=215,y=170)

        lt3=Label(rootreturn,bg="#e6e6e6",text="ReturnedOn",font=("Franklin Gothic Demi Cond",15))
        lt3.place(x=60,y=240)
        inp3=DateEntry(rootreturn,width=28,font=("Calibri (Body)",15),textvariable=vr2)
        inp3.place(x=215,y=240)

        '''lt4=Label(rootreturn,bg="#e6e6e6",text="DueOn:",font=("Franklin Gothic Demi Cond",18))
        lt4.place(x=80,y=350)
        inp4=DateEntry(rootreturn,width=35,font=("Calibri (Body)",15),textvariable=vr3)
        inp4.place(x=235,y=360)'''

        lt5=Label(rootreturn,bg="#e6e6e6",text="Fine Charge",font=("Franklin Gothic Demi Cond",15))
        lt5.place(x=60,y=310)
        lt11=Label(rootreturn,bg="#e6e6e6",text="(if any)",font=("Franklin Gothic Demi Cond",13),fg="red")
        lt11.place(x=58,y=338)
        inp5=Entry(rootreturn,width=30,font=("Calibri (Body)",15),textvariable=vr4)
        inp5.place(x=215,y=310)

        b6=Button(rootreturn,text="Returned Books",width="15",bg="#00b300",fg="white",font=("Segoe UI Black",16),command=lambda:show_returned_data())
        b6.place(x=750,y=100)
        b3=Button(rootreturn,text="Submit",width="15",bg="#00b300",fg="white",font=("Segoe UI Black",16),command=lambda:returned_succesful())
        b3.place(x=750,y=200)
        b5=Button(rootreturn,text="Reset",width="15",bg="#00b300",fg="white",font=("Segoe UI Black",16),command=lambda:[inp2.delete(0,END),inp3.delete(0,END),inp5.delete(0,END),inp7.delete(0,END)])
        b5.place(x=750,y=300)
    
        frame.place(x=0,y=0,width=1370,height=710)       
        rootreturn.mainloop()
    except:
        print("can't run return books")


def show_returned_data():
    try:
        showreturnedtable=Toplevel()
        showreturnedtable.title("Returned Books Record")
        showreturnedtable.state('zoomed')
        framei=Frame(showreturnedtable,bg="#e6e6e6",bd=25,relief=RIDGE)
        tvi=Treeview(framei,column=("Student ID","Student Name","Book ID","Book Name","Price","Book Returned Date","Book Due Date","Fine Charge"))
        tvi.heading("Student ID",text="Student ID")
        tvi.heading("Student Name",text="Student Name")
        tvi.heading("Book ID",text="Book ID")
        tvi.heading("Book Name",text="Book Name")
        tvi.heading("Price",text="Price")   
        tvi.heading("Book Returned Date",text="Book Returned Date")
        tvi.heading("Book Due Date",text="Book Due Date")
        tvi.heading("Fine Charge",text="Fine Charge")

        tvi.column("Student ID",width=60)
        tvi.column("Student Name",width=100)
        tvi.column("Book ID",width=100)
        tvi.column("Book Name",width=200)
        tvi.column("Price",width=30)
        tvi.column("Book Returned Date",width=65)
        tvi.column("Book Due Date",width=50)
        tvi.column("Fine Charge",width=30)

        conn=mysql.connector.connect(host="localhost",username="root",password="riya@16",database="librarymanagementdb")
        query="select * from Returned_book_details"
        c=conn.cursor()
        c.execute(query)
        for i in c:
            tvi.insert("",END,values=i)  
        conn.commit()
        conn.close()
        tvi.pack(fill=BOTH,expand=1)
        framei.pack(fill=BOTH,expand=1)
        showreturnedtable.mainloop()
    except:
        print("can't run show data(return)")

def returned_succesful():
    try:
        if(len(inp2.get())==0 or len(inp3.get())==0 or len(inp5.get())==0 or len(inp7.get())==0):  
            msg=Toplevel()
            msg.title("Incomplete")
            msg.geometry("350x90+550+300")
            msg.resizable(0,0)

            c = Canvas(msg,width=600, height=800)
            c.pack(expand=YES, fill=BOTH)
            photoerr=ImageTk.PhotoImage(Image.open("error_image1.jpg"))
            c.create_image(40, 40, image=photoerr, anchor='nw')
            global image1, resized1, image2
            width=50
            height=50
# open image to resize it
            image1 = Image.open("error_image1.jpg")
# resize the image with width and height of root
            resized1 = image1.resize((width,height))
            image2 = ImageTk.PhotoImage(resized1)
            c.create_image(40,20, image=image2, anchor='nw')
# Bind the function to configure the parent window
            msg.bind("<Configure>", resized1)

            l2=Label(msg,text="Please fill all the details",font=("Segoe UI Black",12))
            l2.place(x=130,y=25)
            button1=Button(msg,text="Ok",command=msg.destroy,width = 10)
            button1.place(x=260,y=60)
        
        else:
            #namebook=vr5.get()
            #author=vr7.get()
            #pub=vr8.get()
            #pub_year=str(vr9.get())
            #edition=vr10.get()
            #price=str(vr11.get())
            #namestud=vr.get()
            #dueon=vr3.get()
            idbook=vr6.get()
            idstud=str(vr1.get())
            finecharge=str(vr4.get())
            returnedon=vr2.get()

            conn2=mysql.connector.connect(host="localhost",username="root",password="r@jain",database="project")
            querycreate="create table if not exists Returned_book_details(ID_stud varchar(15),Name_stud varchar(30),ID_book varchar(20) primary key,Name_book varchar(45),Price varchar(10),Book_Returnedon varchar(10),Book_Dueon varchar(10),Fine_charge varchar(10))"
            cur1=conn2.cursor()
            queryinsert="insert into Returned_book_details(ID_stud,Name_stud,ID_book,Name_book,Price,Book_Dueon) select ID_stud,Name_stud,ID_book,Name_book,Price,Book_Dueon from issued_details where ID_book='{}'".format(idbook)
            queryinsert1="update Returned_book_details set Book_Returnedon='{}',Fine_charge='{}' where ID_book='{}'".format(returnedon,finecharge,idbook)
            
            cur1.execute(queryinsert)
            cur1.execute(queryinsert1)
            conn2.commit()
            print("succesfully inserted into returned books!")
            conn2.close()
           
            conn1=mysql.connector.connect(host="localhost",username="root",password="r@jain",database="project")
            queryinserta="insert into Available_book_details(ID_book,Name_book,Author,Publisher,Published_Year,Edition,Price) select ID_book,Name_book,Author,Publisher,Published_Year,Edition,Price from issued_details where ID_book='{}'".format(idbook)
            cur=conn1.cursor()
            cur.execute(queryinserta)
            conn1.commit()
            print("succesfully inserted into available stock!")
            conn1.close()
            
            conn3=mysql.connector.connect(host="localhost",username="root",password="r@jain",database="project")
            query="delete from issued_details where ID_book='{}'".format(idbook)
            cur2=conn3.cursor()
            cur2.execute(query)
            conn3.commit()
            print("succesfully deleted from issued details!") 
            conn3.close()
        
            showroot=Toplevel()
            showroot.title("Book Returned Successfully!")
            showroot.geometry("400x90+550+300")
            showroot.resizable(0,0)
            showroot.config(bg="#ffffff")
            c1 = Canvas(showroot,width=600, height=800)
            c1.pack(expand=YES, fill=BOTH)
            phototick=ImageTk.PhotoImage(Image.open("green_tick_image.png"))
            c1.create_image(40, 40, image=phototick, anchor='nw')
            global imagetick, resizedtick, imagetick1
            width1=50
            height1=50
# open image to resize it
            imagetick = Image.open("green_tick_image.png")
# resize the image with width and height of root
            resizedtick = imagetick.resize((width1,height1))
            imagetick1 = ImageTk.PhotoImage(resizedtick)
            c1.create_image(40,20, image=imagetick1, anchor='nw')
# Bind the function to configure the parent window
            showroot.bind("<Configure>", resizedtick)

            llabel=Label(showroot,text="Book is returned by {}".format(idstud),font=("Segoe UI Black",12))
            llabel.place(x=110,y=25)
            button2=Button(showroot,text="Ok",command=showroot.destroy,width = 10)
            button2.place(x=260,y=60)
    
            '''txtbox=Text(showroot,bg="#e6e6e6",font=("Franklin Gothic Heavy",15),width=45,height=30)
            conv_id=str(vr1.get())
            conv_fine=str(vr4.get())
            conv_returndate=str(vr2.get())
            conv_duedate=str(vr3.get())
            txtbox.config(state="normal")
            txtbox.insert(INSERT,"ID(Student)           :    "+  conv_id  +"\n\n")
            txtbox.insert(INSERT,"Name(Student)    :    "+  vr.get()   +"\n\n")
            txtbox.insert(INSERT,"ID(Book)                :    "+  vr6.get()  +"\n\n")
            txtbox.insert(INSERT,"Name(Book)         :    "+  vr5.get()  +"\n\n") 
            txtbox.insert(INSERT,"Author                   :    "+  vr7.get()  +"\n\n")
            txtbox.insert(INSERT,"Publisher             :    "+  vr8.get()  +"\n\n")
            txtbox.insert(INSERT,"ReturnedOn         :    "+  conv_returndate  +"\n\n")
            txtbox.insert(INSERT,"DueOn                   :    "+  conv_duedate  +"\n\n")
            txtbox.insert(INSERT,"Fine Charge         :    "+  conv_fine  +"\n\n")
            txtbox.config(state="disabled")
            txtbox.pack()

            txtbox.tag_add("changingstu","1.26","1.60")
            txtbox.tag_add("changingbook","5.29","5.60")
            txtbox.tag_config("changingstu",foreground="#1a53ff")
            txtbox.tag_config("changingbook",foreground="#1a53ff")
            showroot.mainloop()'''
    except:
        print("can't run return book")