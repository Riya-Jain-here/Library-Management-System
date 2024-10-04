from calendar import calendar
from optparse import Values
from tkinter import *
from tkinter.ttk import Treeview
from PIL import ImageTk,Image
import mysql.connector
from tkcalendar import DateEntry

def addbook():
    try:
        global vr,vr1,vr2,vr3,vr4,vr5,vr6,vr7,inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8
        rootadd=Toplevel()
        rootadd.title("ADD BOOKS")
        rootadd.state('zoomed')
        #rootadd.geometry("1370x710+0+0")
        rootadd.config(bg="#b3b3b3")
   
        frame=Frame(rootadd,bg="#e6e6e6",bd=25,relief=RIDGE,padx=20)
        frame1=Frame(rootadd,bg="#ff3300")
        frame1.place(x=25,y=25,width=1320,height=40)
        l=Label(rootadd,text="*Complete the required details:-",font=("Microsoft New Tai Lue",15,"bold"),bg="#ff3300",fg="white")
        l.place(x=28,y=28)

        vr=StringVar()
        vr1=StringVar()
        vr2=StringVar()
        vr3=StringVar()
        vr4=IntVar()
        vr5=StringVar()
        vr6=IntVar()
        vr7=StringVar()
    
        lt1=Label(rootadd,bg="#e6e6e6",text="Name(Book)",font=("Franklin Gothic Demi Cond",15))
        lt1.place(x=60,y=100)
        inp1=Entry(rootadd,width=30,font=("Calibri (Body)",15),textvariable=vr)
        inp1.place(x=215,y=100)

        lt2=Label(rootadd,bg="#e6e6e6",text="ID(Book)",font=("Franklin Gothic Demi Cond",15))
        lt2.place(x=60,y=170)
        inp2=Entry(rootadd,width=30,font=("Calibri (Body)",15),textvariable=vr1)
        inp2.place(x=215,y=170)

        lt3=Label(rootadd,bg="#e6e6e6",text="Publisher",font=("Franklin Gothic Demi Cond",15))
        lt3.place(x=60,y=240)
        inp3=Entry(rootadd,width=30,font=("Calibri (Body)",15),textvariable=vr2)
        inp3.place(x=215,y=240)

        lt4=Label(rootadd,bg="#e6e6e6",text="Author",font=("Franklin Gothic Demi Cond",15))
        lt4.place(x=60,y=310)
        inp4=Entry(rootadd,width=30,font=("Calibri (Body)",15),textvariable=vr3)
        inp4.place(x=215,y=310)

        lt1=Label(rootadd,bg="#e6e6e6",text="Published Year",font=("Franklin Gothic Demi Cond",15))
        lt1.place(x=700,y=100)
        inp5=Entry(rootadd,width=30,font=("Calibri (Body)",15),textvariable=vr4)
        inp5.place(x=855,y=100)

        lt2=Label(rootadd,bg="#e6e6e6",text="Edition",font=("Franklin Gothic Demi Cond",15))
        lt2.place(x=700,y=170)
        inp6=Entry(rootadd,width=30,font=("Calibri (Body)",15),textvariable=vr5)
        inp6.place(x=855,y=170)

        lt3=Label(rootadd,bg="#e6e6e6",text="Price",font=("Franklin Gothic Demi Cond",15))
        lt3.place(x=700,y=240)
        inp7=Entry(rootadd,width=30,font=("Calibri (Body)",15),textvariable=vr6)
        inp7.place(x=855,y=240)

        lt4=Label(rootadd,bg="#e6e6e6",text="Book Added Date",font=("Franklin Gothic Demi Cond",15))
        lt4.place(x=700,y=310)
        inp8=DateEntry(rootadd,width=29,font=("Calibri (Body)",15),textvariable=vr7)
        inp8.place(x=855,y=310)


        b6=Button(rootadd,text="Show Add Data",width="13",bg="#00b300",fg="white",font=("Segoe UI Black",15),command=lambda:show_add_data())
        b6.place(x=400,y=510)
        b3=Button(rootadd,text="Submit",width="13",bg="#00b300",fg="white",font=("Segoe UI Black",15),command=lambda:show_add_details())
        b3.place(x=600,y=510)
        b5=Button(rootadd,text="Reset",width="13",bg="#00b300",fg="white",font=("Segoe UI Black",15),command=lambda:[inp1.delete(0,END),inp2.delete(0,END),inp3.delete(0,END),inp4.delete(0,END),inp5.delete(0,END),inp6.delete(0,END),inp7.delete(0,END),inp8.delete(0,END)])
        b5.place(x=800,y=510)

        frame.place(x=0,y=0,width=1370,height=710)       
        rootadd.mainloop()
    except:
        print("can't run add books")

def show_add_data():
    try:
        showtable=Toplevel()
        showtable.title("New Books Record")
        showtable.state('zoomed')
        '''showtable.geometry("1000x500+250+100")
        showtable.resizable(0,0)'''
       
        frame=Frame(showtable,bg="#e6e6e6",bd=25,relief=RIDGE)
        tv=Treeview(frame,column=("Book ID","Book Name","Author","Publisher","Published Year","Edition","Price","Book Added Date"))
        tv.heading("Book ID",text="Book ID")
        tv.heading("Book Name",text="Book Name")
        tv.heading("Author",text="Author")
        tv.heading("Publisher",text="Publisher")
        tv.heading("Published Year",text="Published Year")
        tv.heading("Edition",text="Edition")
        tv.heading("Price",text="Price")
        tv.heading("Book Added Date",text="Book Added Date")

        tv.column("Book ID",width=100)
        tv.column("Book Name",width=270)
        tv.column("Author",width=130)
        tv.column("Publisher",width=140)
        tv.column("Published Year",width=70)
        tv.column("Edition",width=35)
        tv.column("Price",width=20)
        tv.column("Book Added Date",width=70)
        conn=mysql.connector.connect(host="localhost",username="root",password="riya@16",database="librarymanagementdb")
        query="select * from New_book_details"
        c=conn.cursor()
        c.execute(query)
        for i in c:
            tv.insert("",END,values=i)  
        conn.commit()
        conn.close()
        tv.pack(fill=BOTH,expand=1)
        frame.pack(fill=BOTH,expand=1)
        showtable.mainloop()
    except:
        print("can't run show data")

def show_add_details():
    try:
        if(len(inp1.get())==0 or len(inp2.get())==0 or len(inp3.get())==0 or len(inp4.get())==0 or len(inp6.get())==0 or len(inp7.get())==0 or len(inp8.get())==0):
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
            bookid=vr1.get()
            bookname=vr.get()
            auth=vr3.get()
            pub=vr2.get()
            conv_publishing=str(vr4.get())
            conv_price=str(vr6.get())
            ed=vr5.get()
            addeddate=vr7.get()

            conn=mysql.connector.connect(host="localhost",username="root",password="riya@16",database="librarymanagementdb")
            query="create table if not exists New_book_details(ID_book varchar(20) primary key,Name_book varchar(45),Author varchar(30),Publisher varchar(30),Published_Year varchar(10),Edition varchar(10),Price varchar(10),Book_Added_Date varchar(15))"
            c=conn.cursor()
            queryinsert="insert into New_book_details(ID_book,Name_book,Author,Publisher,Published_Year,Edition,Price,Book_Added_Date) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(bookid,bookname,auth,pub,conv_publishing,ed,conv_price,addeddate)
            queryinsert_availabe="insert into Available_book_details(ID_book,Name_book,Author,Publisher,Published_Year,Edition,Price) select ID_book,Name_book,Author,Publisher,Published_Year,Edition,Price from New_book_details where ID_book='{}'".format(bookid)
            #queryinsert="insert into issued_details values(%s,%s,%s,%s,%s,%s,%s,%s)"
            #t1=(inp2,inp1,inp6,bookchoosen,inp7,inp8,inp3,inp4)
            c.execute(query)
            c.execute(queryinsert)
            c.execute(queryinsert_availabe)
            conn.commit()
            print("connection successfully created!")
            print("Add details stored in both table")

            showroot=Toplevel()
            showroot.title("Data Submitted Sucssessfully!")
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

            llabel=Label(showroot,text="Book is added",font=("Segoe UI Black",12))
            llabel.place(x=115,y=25)
            button2=Button(showroot,text="Ok",command=showroot.destroy,width = 10)
            button2.place(x=260,y=60)

            '''txtbox=Text(showroot,bg="#e6e6e6",font=("Franklin Gothic Heavy",15),width=45,height=25)
            txtbox.config(state="normal")
            txtbox.insert(INSERT,"ID(Book)                     :    "+  vr1.get()  +"\n\n")
            txtbox.insert(INSERT,"Name(Book)              :    "+  vr.get()   +"\n\n")
            txtbox.insert(INSERT,"Author                        :    "+  vr3.get()  +"\n\n")
            txtbox.insert(INSERT,"Publisher                  :    "+  vr2.get()  +"\n\n")
            txtbox.insert(INSERT,"Publishing Year       :    "+  conv_publishing  +"\n\n")
            txtbox.insert(INSERT,"Edition                        :    "+  vr5.get()  +"\n\n")
            txtbox.insert(INSERT,"Price                            :    "+  conv_price  +"\n\n")
            txtbox.config(state="disabled")
            txtbox.pack()

            txtbox.tag_add("changing","1.34","1.60")
            txtbox.tag_config("changing",foreground="#1a53ff")
            showroot.mainloop()'''
    except:
        print("Can't run show add details")
        
