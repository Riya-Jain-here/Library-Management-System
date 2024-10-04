from tkinter import *
from tkinter.ttk import Treeview
import mysql.connector
def show_available_data():
    try:
        global i,tv1
        showavaildata=Toplevel()
        showavaildata.title("Available Books Record")
        showavaildata.state('zoomed')
       
        f1=Frame(showavaildata,bg="#e6e6e6",bd=25,relief=RIDGE)
        tv1=Treeview(f1,column=("Book ID","Book Name","Author","Publisher","Publishing Year","Edition","Price"))
        tv1.heading("Book ID",text="Book ID")
        tv1.heading("Book Name",text="Book Name")
        tv1.heading("Author",text="Author")
        tv1.heading("Publisher",text="Publisher")
        tv1.heading("Publishing Year",text="Publishing Year")
        tv1.heading("Edition",text="Edition")
        tv1.heading("Price",text="Price")

        tv1.column("Book ID",width=150)
        tv1.column("Book Name",width=270)
        tv1.column("Author",width=200)
        tv1.column("Publisher",width=180)
        tv1.column("Publishing Year",width=90)
        tv1.column("Edition",width=70)
        tv1.column("Price",width=50)
        conn=mysql.connector.connect(host="localhost",username="root",password="riya@16",database="librarymanagementdb")
        queryavail="create table if not exists Available_book_details(ID_book varchar(20) primary key,Name_book varchar(45),Author varchar(30),Publisher varchar(30),Published_Year varchar(10),Edition varchar(10),Price varchar(10))"
        c=conn.cursor()
        #query1="insert into Available_book_details(ID_book,Name_book,Author,Publisher,Publishing_Year,Edition,Price) values('484-12-7-23145-12','Introduction To Quantum Mechanics','David J. Griffiths','Cambridge University Press','2016','3rd','1000')"
        c.execute(queryavail)
        #c.execute(query1)
        fetchq="select * from available_book_details" 
        c.execute(fetchq)
        for i in c:
            tv1.insert("",END,values=i)
        conn.commit()
        #conn.close()
        tv1.pack(fill=BOTH,expand=1)
        f1.pack(fill=BOTH,expand=1)
        showavaildata.mainloop()
    except:
        print("can't run show available data")