from tkinter import *
from PIL import ImageTk,Image
from Project_issued import *
from Project_return import *
from Project_add import *
from Project_LMS1 import *
import Project_available_stock as pas

def library1():
        try:
                global root2
                root2=Toplevel()
                root2.title("WELCOME")
                root2.state('zoomed')
                c = Canvas(root2,width=700, height=800)
                c.pack(expand=YES, fill=BOTH)
                imgg = Image.open("back2.jpg")
                img=ImageTk.PhotoImage(imgg)
                c.create_image(0, 0, image=img, anchor='nw')
                global imagemain, resizedmain, imagemain1,resized5,image11,image12
                width=1370
                height=710
# open image to resize it
                imagemain = Image.open("back2.jpg")
# resize the image with width and height of root
                resizedmain= imagemain.resize((width,height))
                imagemain1 = ImageTk.PhotoImage(resizedmain)
                c.create_image(0,0, image=imagemain1, anchor='nw')
                c.create_text(625,100,text="Welcome to Library",fill="White",font=('Franklin Gothic Demi',45,'bold'))

#btn issues
                photo4=ImageTk.PhotoImage(file='textinput.webp')
                #c.create_image(0,0, image=photo4, anchor="nw")
                width1=540
                height1=60
                image11= Image.open("textinput.webp")
                resized5 = image11.resize((width1, height1))
                image12= ImageTk.PhotoImage(resized5)
                c.create_image(350,160, image=image12, anchor='nw')

#btn returned
                c.create_image(350,230, image=image12, anchor='nw')

#btn add
                c.create_image(350,300, image=image12, anchor='nw')

#btn show available 
                c.create_image(350,370, image=image12, anchor='nw')

#btn show issued
                c.create_image(350,440,image=image12, anchor='nw')

#btn show returned
                c.create_image(350,510,image=image12, anchor='nw')

#btn show added
                c.create_image(350,580,image=image12, anchor='nw')

# Bind the function to configure the parent window
                
                root2.bind("<Configure>", resized5)
                root2.bind("<Configure>", resizedmain)

                #blackbg=Frame(root2,bg="#1a1a1a",bd=5)

                b=Button(root2,text="Click Here for Issue Books",width="30",bg="white",fg="green",font=("Segoe UI Black",14),border=0,command=lambda:issuebooks())
                b.place(x=425,y=170)
                
                b1=Button(root2,text="Click Here for Return Books",width="30",bg="white",fg="green",font=("Segoe UI Black",14),border=0,command=lambda:returnbook())
                b1.place(x=425,y=240)

                b2=Button(root2,text="Click Here for Add Books",width="30",bg="white",fg="green",font=("Segoe UI Black",14),border=0,command=lambda:addbook())
                b2.place(x=425,y=310)

                b3=Button(root2,text="Click Here to show Available Books",width="30",bg="white",fg="green",font=("Segoe UI Black",14),border=0,command=lambda:pas.show_available_data())
                b3.place(x=425,y=378)

                b4=Button(root2,text="Click Here to show Issued Books",width="30",bg="white",fg="green",font=("Segoe UI Black",14),border=0,command=lambda:show_issued_data())
                b4.place(x=425,y=450)

                b5=Button(root2,text="Click Here to show Returned Books",width="30",bg="white",fg="green",font=("Segoe UI Black",14),border=0,command=lambda:show_returned_data())
                b5.place(x=425,y=520)

                b6=Button(root2,text="Click Here to show New Added Books",width="30",bg="white",fg="green",font=("Segoe UI Black",14), border=0,command=lambda:show_add_data())
                b6.place(x=425,y=590)

                #blackbg.place(x=915,y=5,width=450,height=697)
                root2.mainloop()  
        except:
                print("Can't run welcome page") 
        
        