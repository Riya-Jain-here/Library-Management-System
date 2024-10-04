import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import mysql.connector
from PIL import ImageTk,Image
from tkcalendar import DateEntry
import Project_available_stock as avail
import Project_add as proadd

def issuebooks():
    try:
        global vi,vi1,vi2,vi3,vi4,vi5,vi6,vi7,vi8,vi9,vi10,inp1,inp2,inp3,inp4,inp6,inp7,inp8,inp9,inp10,inp11,bookchoosen,rootissue
        rootissue=Toplevel()
        rootissue.title("ISSUE BOOKS")
        rootissue.state('zoomed')
        rootissue.config(bg="#f2f2f2")
    
        frame=Frame(rootissue,bg="#e6e6e6",bd=25,relief=RIDGE,padx=20)
        frame1=Frame(rootissue,bg="#ff3300")
        frame1.place(x=25,y=25,width=1320,height=40)

        l=Label(rootissue,text="*Complete the required details:-",font=("Microsoft New Tai Lue",15,"bold"),bg="#ff3300",fg="white")
        l.place(x=28,y=28)
        vi=StringVar()
        vi1=StringVar()
        vi2=StringVar()
        vi3=StringVar()
        vi4=StringVar()
        vi5=StringVar()
        vi6=IntVar()
        vi7=StringVar()
        vi8=IntVar()
        vi9=StringVar()
        vi10=IntVar()

        lt1=Label(rootissue,bg="#e6e6e6",text="Name(Student)",font=("Franklin Gothic Demi Cond",15))
        lt1.place(x=60,y=100)
        lt11=Label(rootissue,bg="#e6e6e6",text="(book issued to whom)",font=("Franklin Gothic Demi Cond",12),fg="red")
        lt11.place(x=45,y=128 )
        inp1=Entry(rootissue,width=30,font=("Calibri (Body)",15),textvariable=vi)
        inp1.place(x=215,y=100)

        lt2=Label(rootissue,bg="#e6e6e6",text="ID(Student)",font=("Franklin Gothic Demi Cond",15))
        lt2.place(x=60,y=170)
        inp2=Entry(rootissue,width=30,font=("Calibri (Body)",15),textvariable=vi6)
        inp2.place(x=215,y=170)
    
        lt3=Label(rootissue,bg="#e6e6e6",text="IssuedOn",font=("Franklin Gothic Demi Cond",15))
        lt3.place(x=60,y=240)
        inp3=DateEntry(rootissue,width=29,font=("Calibri (Body)",15),textvariable=vi1)
        inp3.place(x=215,y=240)

        lt4=Label(rootissue,bg="#e6e6e6",text="DueOn",font=("Franklin Gothic Demi Cond",15))
        lt4.place(x=60,y=310)
        inp4=DateEntry(rootissue,width=29,font=("Calibri (Body)",15),textvariable=vi2)
        inp4.place(x=215,y=310)

        lt1=Label(rootissue,bg="#e6e6e6",text="Name(Book)",font=("Franklin Gothic Demi Cond",15))
        lt1.place(x=60,y=380)

        
        '''def selectBook(event=""):
            conn=mysql.connector.connect(host="localhost",username="root",password="r@jain",database="project")
            c=conn.cursor()
            queryname1="select ID_book from available_book_details where Name_book='{}' having count(ID_book)>0".format(vi3.get())
            c.execute(queryname1)
            result1=c.fetchall()
            lt2=Label(rootissue,bg="#e6e6e6",text="ID(Book):",font=("Franklin Gothic Demi Cond",23))
            lt2.place(x=700,y=240)
            inp6=Entry(rootissue,width=40,font=("Calibri (Body)",15))
            inp6.place(x=870,y=250)
            inp6.insert(0,result1)'''
        
        conn=mysql.connector.connect(host="localhost",username="root",password="riya@16",database="librarymanagementdb")
        c=conn.cursor()
        queryname="select Name_book from available_book_details"
        c.execute(queryname)
        result=c.fetchall()
        bookchoosen=Combobox(rootissue,width=29,font=("calibri (body)",15),textvariable=vi3)
        bookchoosen["values"]=result
        bookchoosen.place(x=215,y=380)
        bookchoosen.current(0)
        conn.close()        

        lt2=Label(rootissue,bg="#e6e6e6",text="ID(Book)",font=("Franklin Gothic Demi Cond",15))
        lt2.place(x=60,y=450)
        inp6=Entry(rootissue,width=30,font=("Calibri (Body)",15),textvariable=vi7)
        inp6.place(x=215,y=450)

        lt3=Label(rootissue,bg="#e6e6e6",text="Author",font=("Franklin Gothic Demi Cond",15))
        lt3.place(x=700,y=100)
        inp7=Entry(rootissue,width=35,font=("Calibri (Body)",15),textvariable=vi4)
        inp7.place(x=855,y=100)

        lt4=Label(rootissue,bg="#e6e6e6",text="Publisher",font=("Franklin Gothic Demi Cond",15))
        lt4.place(x=700,y=170)
        inp8=Entry(rootissue,width=35,font=("Calibri (Body)",15),textvariable=vi5)
        inp8.place(x=855,y=170)

        lt5=Label(rootissue,bg="#e6e6e6",text="Published Year",font=("Franklin Gothic Demi Cond",15))
        lt5.place(x=700,y=240)
        inp9=Entry(rootissue,width=35,font=("Calibri (Body)",15),textvariable=vi8)
        inp9.place(x=855,y=240)

        lt6=Label(rootissue,bg="#e6e6e6",text="Edition",font=("Franklin Gothic Demi Cond",15))
        lt6.place(x=700,y=310)
        inp10=Entry(rootissue,width=35,font=("Calibri (Body)",15),textvariable=vi9)
        inp10.place(x=855,y=310)

        lt7=Label(rootissue,bg="#e6e6e6",text="Price",font=("Franklin Gothic Demi Cond",15))
        lt7.place(x=700,y=380)
        inp11=Entry(rootissue,width=35,font=("Calibri (Body)",15),textvariable=vi10)
        inp11.place(x=855,y=380)
        
        b8=Button(rootissue,text="Available Books",width="13",bg="#00b300",fg="white",font=("Segoe UI Black",14),command=lambda:avail.show_available_data())
        b8.place(x=300,y=510)
        b6=Button(rootissue,text="Issued Books",width="13",bg="#00b300",fg="white",font=("Segoe UI Black",14),command=lambda:show_issued_data())
        b6.place(x=500,y=510)
        b3=Button(rootissue,text="Submit",width="13",bg="#00b300",fg="white",font=("Segoe UI Black",14),command=lambda:show_successful())
        b3.place(x=700,y=510)
        b5=Button(rootissue,text="Reset",width="13",bg="#00b300",fg="white",font=("Segoe UI Black",14),command=lambda:[inp1.delete(0,END),inp2.delete(0,END),inp3.delete(0,END),inp4.delete(0,END),bookchoosen.delete(0,END),inp6.delete(0,END),inp7.delete(0,END),inp8.delete(0,END),inp9.delete(0,END),inp10.delete(0,END),inp11.delete(0,END)])
        b5.place(x=900,y=510)

        frame.place(x=0,y=0,width=1370,height=710) 
        rootissue.mainloop()  
    except:
        print("can't run issue books")  


def show_issued_data():
    try:
        showissuedtable=Toplevel()
        showissuedtable.title("Issued Books Record")
        showissuedtable.state('zoomed')

        framei=Frame(showissuedtable,bg="#e6e6e6",bd=25,relief=RIDGE)
        tvi=Treeview(framei,column=("Student ID","Student Name","Book ID","Book Name","Author","Publisher","Issued Date","Due Date","Published Year","Edition","Price"))
        tvi.heading("Student ID",text="Student ID")
        tvi.heading("Student Name",text="Student Name")
        tvi.heading("Book ID",text="Book ID")
        tvi.heading("Book Name",text="Book Name")
        tvi.heading("Author",text="Author")
        tvi.heading("Publisher",text="Publisher")
        tvi.heading("Issued Date",text="Issued Date")
        tvi.heading("Due Date",text="Due Date")
        tvi.heading("Published Year",text="Published Year")
        tvi.heading("Edition",text="Edition")
        tvi.heading("Price",text="Price")   

        tvi.column("Student ID",width=65)
        tvi.column("Student Name",width=90)
        tvi.column("Book ID",width=100)
        tvi.column("Book Name",width=200)
        tvi.column("Author",width=100)
        tvi.column("Publisher",width=120)
        tvi.column("Issued Date",width=60)
        tvi.column("Due Date",width=60)
        tvi.column("Published Year",width=70)
        tvi.column("Edition",width=30)
        tvi.column("Price",width=25)
                        
        conn=mysql.connector.connect(host="localhost",username="root",password="riya@16",database="librarymanagementdb")
        query="select * from issued_details"
        c=conn.cursor()
        c.execute(query)
        for i in c:
            tvi.insert("",END,values=i)  
        conn.commit()
        conn.close()
        tvi.pack(fill=BOTH,expand=1)
        framei.pack(fill=BOTH,expand=1)
        showissuedtable.mainloop()
    except:
        print("can't run issued data")



def show_successful():
    try:
        if(len(inp1.get())==0 or len(inp2.get())==0 or len(inp3.get())==0 or len(inp4.get())==0 or len(inp6.get())==0 or len(inp7.get())==0 or len(inp8.get())==0 or len(bookchoosen.get())==0 or len(inp9.get())==0 or len(inp10.get())==0 or len(inp11.get())==0):    
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
            convertstu=str(vi6.get())
            convert_issuedate=str(vi1.get())
            convert_duedate=str(vi2.get())
            name=vi.get()
            bookname=vi3.get()
            bookid=vi7.get()
            author=vi4.get()
            publisher=vi5.get()
            Pub_year=str(vi8.get())
            editon=vi9.get()
            price=str(vi10.get())

            conn=mysql.connector.connect(host="localhost",username="root",password="riya@16",database="librarymanagementdb")
            query="create table if not exists issued_details(ID_stud varchar(15),Name_stud varchar(20),ID_book varchar(20) primary key,Name_book varchar(45),Author varchar(30),Publisher varchar(30),Book_Issuedon varchar(10),Book_Dueon varchar(10),Published_Year varchar(10),Edition varchar(10),Price varchar(10))"
            c=conn.cursor()
            queryinsert="insert into issued_details(ID_stud,Name_stud,ID_book,Name_book,Author,Publisher,Book_Issuedon,Book_Dueon,Published_Year,Edition,Price) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(convertstu,name,bookid,bookname,author,publisher,convert_issuedate,convert_duedate,Pub_year,editon,price)
            c.execute(query)
            c.execute(queryinsert)
            conn.commit()
            print("connection successfully created!")
            print("Issued details stored in table")
            conn.close()
                
            showmsg=Toplevel()
            showmsg.title("Data Submitted Succesfully!")
            showmsg.geometry("400x90+550+300")
            showmsg.resizable(0,0)
            showmsg.config(bg="#ffffff")

            c1 = Canvas(showmsg,width=600, height=800)
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
            showmsg.bind("<Configure>", resizedtick)

            llabel=Label(showmsg,text="Book is issued to '{}'".format(vi.get()),font=("Segoe UI Black",12))
            llabel.place(x=100,y=25)
            button2=Button(showmsg,text="Ok",command=showmsg.destroy,width = 10)
            button2.place(x=260,y=60)

            conn=mysql.connector.connect(host="localhost",username="root",password="riya@16",database="librarymanagementdb")
            querydelete="delete from available_book_details where ID_book='{}'".format(vi7.get())
            c=conn.cursor()
            c.execute(querydelete)
            conn.commit()
            print("succesfully deleted from available stock!")
            
            '''txtbox=Text(showroot,bg="#e6e6e6",font=("Franklin Gothic Heavy",15),width=45,height=20)
            txtbox.config(state="normal")
            txtbox.insert(INSERT,"ID(Student)           :    "+  convertstu  +"\n\n")
            txtbox.insert(INSERT,"Name(Student)    :    "+  vi.get()   +"\n\n")
            txtbox.insert(INSERT,"ID(Book)                :    "+  vi7.get()  +"\n\n")
            txtbox.insert(INSERT,"Name(Book)         :    "+  bookname  +"\n\n")
            txtbox.insert(INSERT,"Author                   :    "+  vi4.get()  +"\n\n")
            txtbox.insert(INSERT,"Publisher             :    "+  vi5.get()  +"\n\n")
            txtbox.insert(INSERT,"IssuedOn              :    "+  convert_issuedate  +"\n\n")
            txtbox.insert(INSERT,"DueOn                   :    "+  convert_duedate  +"\n\n")
            txtbox.config(state="disabled")
            txtbox.pack()

            txtbox.tag_add("changingstu","1.26","1.60")
            txtbox.tag_add("changingbook","5.29","5.60")
            txtbox.tag_config("changingstu",foreground="#1a53ff")
            txtbox.tag_config("changingbook",foreground="#1a53ff")'''

            '''conn=mysql.connector.connect(host="localhost",username="root",password="r@jain",database="project")
            querydelete="delete from available_book_details where ID_book=''".format(vi7.get())
            c=conn.cursor()
            c.execute(querydelete)
            conn.commit()
            print("succesfully deleted from available stock!")'''
            
    except:
        print("can't submit issued details")




    
