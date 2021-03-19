import tkinter as tk
from tkinter import ttk
from tkinter import HORIZONTAL
import tkinter.font as tkFont
from tkinter import messagebox
import mysql.connector
from cryptography.fernet import Fernet

##################################
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "projectdatabase"
)

mycursor = mydb.cursor()
##################################




class Registruj(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


        parent.grid_columnconfigure(1,weight=1)
        parent.grid_columnconfigure(4,weight=1)
        parent.grid_rowconfigure(1,weight=1)
        parent.grid_rowconfigure(10,weight=1)
        parent.minsize(300,300)
        
        #fontovi

        dobroDosliFont = tkFont.Font(self, family = "Raleway", size = 14)
        ralewayFont = tkFont.Font(self, family = "Raleway", size = 12)
        robotoFont = tkFont.Font(self, family = "Roboto", size = 12)

        #ourcode



        dobroDosli = tk.Label(self, text = "Registracija", font = dobroDosliFont).grid(column=1, row = 1,columnspan = 4, padx= 30, pady = 10)
        separatorLine = ttk.Separator(self, orient = HORIZONTAL).grid(column=0, row = 2, columnspan = 5, sticky = "we",  pady = (0,40))


        self.nametext = tk.StringVar()
        nameLabel = tk.Label(self, text = "Name").grid(column=1, row = 3)
        nameEntry = tk.Entry(self, textvariable = self.nametext, width = 20).grid(row = 4,column=1,padx = 10)
    

        self.surnametext = tk.StringVar()
        surnameLabel = tk.Label(self, text = "Surname").grid(column=1, row = 5)
        surnameEntry = tk.Entry(self, textvariable = self.surnametext, width = 20).grid(row = 6,column=1)

        self.emailtext = tk.StringVar()
        emailLabel = tk.Label(self, text = "Email").grid(column=1, row = 7)
        emailEntry = tk.Entry(self, textvariable = self.emailtext, width = 20).grid(row = 8,column=1)


        self.usernametext = tk.StringVar()
        usernameLabel = tk.Label(self, text = "Userame").grid(column=2, row = 3)
        usernameEntry = tk.Entry(self, textvariable = self.usernametext, width = 20).grid(row = 4, column=2, padx = 10)

        self.passwordtext = tk.StringVar()
        passwordLabel = tk.Label(self, text = "Password").grid(column=2, row = 5)
        passwordEntry = tk.Entry(self, textvariable = self.passwordtext, width = 20, show = "*").grid(row = 6, column=2, padx = 10)

        self.repeatedpasswordtext = tk.StringVar()
        repeatedpasswordLabel = tk.Label(self, text = "Repeat password").grid(column=2, row = 7)
        repeatedpasswordEntry = tk.Entry(self, textvariable = self.repeatedpasswordtext, width = 20, show = "*").grid(row = 8, column=2, padx = 10)
        

        submitBtn = tk.Button(self, text = "Submit", command = self.submitmethod).grid(row = 9, column = 1, columnspan = 2, padx = 50, pady = 20)


        self.defaultpermission = 1
        self.defaultstatus = 0


    def submitmethod(self):
        #enkripcija
        key = b's3wlDzT0Q-sO0i-cDXZLpmNt6b2J3OEfwOm1nrpChMQ='
        temp = Fernet(key)
        self.password = self.passwordtext.get()
        self.encryptedpassword = temp.encrypt(self.password.encode())
        self.passzadb = self.encryptedpassword.decode()
        print(self.passzadb)
        
        mycursor.execute("SELECT username FROM users WHERE username=%s",(self.usernametext.get(),) )
        accounts = mycursor.fetchall()


        

        if self.nametext.get()=="" or self.surnametext.get()=="" or self.emailtext.get() =="" or  self.usernametext.get()=="" or self.passwordtext.get()=="":
            messagebox.showerror(title = "Greška", message = "Niste popunili sva polja")
        elif accounts:
            messagebox.showerror(title = "Greška", message = "Korisničko ime već postoji!")
            self.parent.destroy()
        else:
            querry = "INSERT INTO users (user_name, user_surname, user_email, username, password, permission, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (
                self.nametext.get(),
                self.surnametext.get(),
                self.emailtext.get(),
                self.usernametext.get(),
                self.passzadb,
                self.defaultpermission, 
                self.defaultstatus
            )
            mycursor.execute(querry, values)
            mydb.commit()
            messagebox.showinfo(title = "Uspješna registracija", message = "Dobrodošli...")
            self.parent.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()






    window.mainloop()
