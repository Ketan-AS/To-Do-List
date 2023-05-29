from tkinter import *
import tkinter.font as font
from To_do_main import *


def validateLogin():
    Font1 = font.Font(family='Helvetica',size=12)
    if(usernameEntry.get()=="Ketan" and userpasswordEntry.get()=="Ketan123"):
        login.destroy()
        main()
        
    else:
        resultlbl.config(fg="red",font=Font1 )
        resultlbl["text"]="Incorrect Username/Password !"
        resultlbl.place(x=700,y=300)
        
#login
login = Tk()  
login.geometry("800x600+100+50")  
login.title('To-Do-List Login')

#Define Image
bg =PhotoImage(file="todo.png")

#label
mylabel = Label(login,image =bg)
mylabel.place(x=0,y=0,relwidth =1,relheight=1)

welcomelabel = Label(login,text="Enter Login Details",font=("Times", 25), fg='black', bg='white')
welcomelabel.place(x=670, y=250)

usernamelabel = Label(login,text="Username", font=("Comic Sans MS", 15))
usernamelabel.place(x=570, y=370)
usernameEntry = Entry(login, font=("Comic Sans MS", 15))
usernameEntry.place(x=680, y=370)

#entry for user input
userpasswordlabel = Label(login,text="Password",font=("Comic Sans MS", 15))
userpasswordlabel.place(x=570, y=450)
userpasswordEntry = Entry(login,font=("Comic Sans MS", 15),show='*')
userpasswordEntry.place(x=680, y=450)

#submit button
loginButton = Button(login, text="Login",font=("Comic Sans MS", 15) ,command=validateLogin)
loginButton.place(x=710, y=500)

#place label in grid
resultlbl=Label(login)
resultlbl.grid(row=6,column=0)

#login loop
login.mainloop()