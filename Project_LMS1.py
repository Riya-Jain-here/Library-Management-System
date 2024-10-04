from textwrap import fill
from tkinter import *
from PIL import ImageTk,Image
import login_logic_project as llp

class Libraryy:
        def __init__(self,var):
                try:
                        self.var=var
                        var.state('zoomed')
                        var.title("LIBRARY  MANAGEMENT  SYSTEM")
                        photo=ImageTk.PhotoImage(file='back2.jpg')
                        canvas = Canvas(var, width=700, height=350)
                        
                        canvas.pack(fill=BOTH, expand=True)
# Add Image inside the Canvas
                        canvas.create_image(0,0, image=photo, anchor="nw")
                        
                        global image,resized,image2,image3,image4,image5,image6,resized2,resized1,image7,image8,resized3,image9,image10,resized4
                        width=1370
                        height=710
# open image to resize it
                        image = Image.open("back2.jpg")
# resize the image with width and height of root
                        resized = image.resize((width, height))
                        image2 = ImageTk.PhotoImage(resized)
                        canvas.create_image(0,0, image=image2, anchor='nw')
                        canvas.create_text(510,200,text="Login",fill="white",font=('Franklin Gothic Demi',45,'bold'))
                        canvas.create_text(490,295,text="Username",fill="white",font=('Franklin Gothic Demi',20,'bold'))
                        canvas.create_text(485,400,text="Password",fill="white",font=('Franklin Gothic Demi',20,'bold'))
# admin logo 
                        photo1=ImageTk.PhotoImage(file='admin.webp')
                        canvas.create_image(0,0, image=photo1, anchor="nw")
                        width1=210
                        height1=170
                        image3= Image.open("admin.webp")
                        resized1 = image3.resize((width1, height1))
                        image4= ImageTk.PhotoImage(resized1)
                        canvas.create_image(590,110, image=image4, anchor='nw')

#input img1
                        photo2=ImageTk.PhotoImage(file='textinput.webp')
                        canvas.create_image(0,0, image=photo2, anchor="nw")
                        width2=400
                        height2=50
                        image5= Image.open("textinput.webp")
                        resized2 = image5.resize((width2, height2))
                        image6= ImageTk.PhotoImage(resized2)
                        canvas.create_image(410,315, image=image6, anchor='nw')

#input img2
                        photo3=ImageTk.PhotoImage(file='textinput.webp')
                        canvas.create_image(0,0, image=photo3, anchor="nw")
                        width3=400
                        height3=50
                        image7= Image.open("textinput.webp")
                        resized3 = image7.resize((width3, height3))
                        image8= ImageTk.PhotoImage(resized3)
                        canvas.create_image(410,422, image=image8, anchor='nw')

# button img
                        photo4=ImageTk.PhotoImage(file='textinput.webp')
                        canvas.create_image(0,0, image=photo4, anchor="nw")
                        width4=200
                        height4=48
                        image9= Image.open("textinput.webp")
                        resized4 = image9.resize((width4, height4))
                        image10= ImageTk.PhotoImage(resized4)
                        canvas.create_image(600,490, image=image10, anchor='nw')
                        
# Bind the function to configure the parent window
                        var.bind("<Configure>", resized4)
                        var.bind("<Configure>", resized3)
                        var.bind("<Configure>", resized2)
                        var.bind("<Configure>", resized1)
                        var.bind("<Configure>", resized)

# black background frame
                        '''backgd=Frame(var,bg="#003300")
                        backgd.place(x=400,y=90,width=550,height=450)'''

# book image
                        '''photo1=ImageTk.PhotoImage(Image.open("admin.webp"))
                        lab=Label(var,image=photo1)
                        lab.image=photo1
                        lab.place(x=680,y=100,width=100,height=100)'''

                        '''labeltitle2=Label(var,text="Log In ",font=("Franklin Gothic Demi",37),fg="#003300")
                        labeltitle2.place(x=920,y=90)'''   

                        x=StringVar()
                        inp=Entry(var,width=22,font=("Calibri (Body)",13),textvariable=x,border=0,fg="black")
                        #inp.insert(0, "username")
                        inp.place(x=450,y=330)
                        inp.focus()

                        y=StringVar()
                        inp1=Entry(var,width=22,font=("Calibri (Body)",13),textvariable=y,show="*",fg="black",border=0)
                        #inp1.insert(0,"Password")
                        inp1.place(x=450,y=435)
                        
                        button=Button(var,text="Proceed",width="10",border=0,bg="#ffffff",fg="#66a3ff",font=("Segoe UI Black",13),command=lambda:llp.checking(x.get(),y.get()))
                        button.place(x=635,y=495)
                        
                except:
                        print("can't run login window")
         
if __name__=="__main__":
        var=Tk()
        obj=Libraryy(var)
        var.mainloop()

