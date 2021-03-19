from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import mysql.connector
from modules.registermodule import Registruj
from modules.mainwindow import MainWindow
from tkinter import messagebox
from cryptography.fernet import Fernet


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "projectdatabase"
)

mycursor = mydb.cursor()

window = Tk()

# window.resizable(False, False)

window.title("Dobrodošli...")
#window.iconbitmap("icon.ico") - DODATI NAKNADNO IKONU!

dobroDosliFont = tkFont.Font(family = "Raleway", size = 14)
ralewayFont = tkFont.Font(family = "Raleway", size = 12)
robotoFont = tkFont.Font(family = "Roboto", size = 12)

#logoSlika = PhotoImage(file = "logo.png") - DODATI NAKNADNO LOGO!



def openregistracija():
    test = Toplevel(window)
    registracija = Registruj(test)
    registracija.grid(column=2, row = 9)
    #registracija.resizeable(False,False)

def openmainwindow():
    test = Toplevel(window)
    mainwindow = MainWindow(test)
    mainwindow.grid(column = 1, row = 1)



def clearentry():
    emailEntry.delete(0, "end")
    emailEntry.insert(0, "")
    passwordEntry.delete(0, "end")
    passwordEntry.insert(0, "")

def logincheck():

    getemail = emailtext.get()
    getpassword = passwordtext.get()

    mycursor.execute("SELECT * from users WHERE user_email = %s",(getemail,))
    result = mycursor.fetchall()
    if not result:
        messagebox.showerror(title = "Greška", message = "Vaš račun nije pronađen.")
        clearentry()

    elif getemail == '' or getpassword == '':
        messagebox.showerror(title = "Greška", message = "Niste unijeli sva polja!")
        clearentry()

    else:
        key = b's3wlDzT0Q-sO0i-cDXZLpmNt6b2J3OEfwOm1nrpChMQ='
        enkripcija = Fernet(key)

        mycursor.execute("SELECT password FROM users WHERE user_email = %s",(getemail,))
     
        result = mycursor.fetchone()
        sifraizbaze = result[0].encode()
        dekriptovanaSifra = (enkripcija.decrypt(sifraizbaze).decode())


        if dekriptovanaSifra == getpassword:
            messagebox.showinfo(title = "Uspješna prijava", message = "Dobrodošli...")
            # window.withdraw()
            openmainwindow()
            
        else:
            messagebox.showerror(title = "Greška", message = "Pogrešan email ili password")
            clearentry()



dobroDosli = Label(window, text = "Dobrodošli nazad", font = dobroDosliFont).grid(column=0, row = 1,columnspan = 4, padx= 30, pady = 10)

separatorLine = ttk.Separator(window, orient = HORIZONTAL).grid(column=0, row = 2, columnspan = 4, sticky = "ew", pady = (0,40))

emailLabel = Label(window, text = "Email", font = robotoFont).grid(column=1, row = 3, padx = (60,15))
emailtext = StringVar()
emailEntry = Entry(window, font = robotoFont, textvariable = emailtext)
emailEntry.grid(column= 2, row = 3, ipady = 5, ipadx = 25, pady = 15, padx = (15,80))


passwordLabel = Label(window, text = "Password", font = robotoFont).grid(column=1, row = 4, padx = (70,15))
passwordtext = StringVar()
passwordEntry = Entry(window, font = robotoFont, show = "*", textvariable = passwordtext)
passwordEntry.grid(column= 2, row = 4, ipady = 5, ipadx = 25, pady = (0,15), padx = (15,80))


prijaviButton = Button(window, text = "Prijavi se", font = robotoFont, command = logincheck).grid(column = 2, row = 5, padx = (0,180), pady = (0,60))

registrujButton = Button(window, text = r"Registruj se", fg = "blue", cursor = "hand2", command = openregistracija, font = robotoFont, highlightthickness = 0, bd = 0).grid(column = 2, row = 5, padx = (1,0), pady = (0,60))


window.grid_columnconfigure(0,  weight =1)
window.grid_columnconfigure(3,  weight =1)
window.grid_rowconfigure(0,weight = 1)
window.grid_rowconfigure(6,weight = 1)


window.minsize(500,300)

window.mainloop()
