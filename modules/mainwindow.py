from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import mysql.connector
from modules.test import KorisniciModule




##################################
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "projectdatabase"
)

mycursor = mydb.cursor()
##################################





class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.parent.geometry("780x390")
        self.parent.resizable(False, False)
        
        #images
        self.usersimage = tk.PhotoImage(file = "img/group.png")
        self.clientsimage = tk.PhotoImage(file = "img/clients.png")
        self.tasksimage = tk.PhotoImage(file = "img/clipboard.png")
        self.logoutimage = tk.PhotoImage(file = "img/logout.png")
        self.projectimage = tk.PhotoImage(file = "img/project.png")
        self.leadsimage = tk.PhotoImage(file = "img/leads.png")
        self.reportsimage = tk.PhotoImage(file = "img/report.png")
        #images

        #fonts
        self.headingFont = tkFont.Font(family = "Raleway", size = 14)
        self.ralewayFont = tkFont.Font(family = "Raleway", size = 12)
        self.robotoFont = tkFont.Font(family = "Roboto", size = 12)
        #

        def removeWidgets():
            ############# MAIN MENU #####
            welcomeLabel.grid_forget()
            ######### KORISNICI ##########
            korisnici_label1.grid_forget()
            korisniciButton1.grid_forget()
            korisniciButton2.grid_forget()
            korisniciButton3.grid_forget()
            tree.grid_forget()
            korisnici_Approve.grid_forget()

            

            klijenti_label1.grid_forget()
            klijenti_label2.grid_forget()

            taskovi_label1.grid_forget()
            taskovi_label2.grid_forget()

            labelneki.grid_forget()

            labelpet.grid_forget()

            labelenver.grid_forget()


        def moduloneopen(event):
            removeWidgets() #Odma remova sve prozore, pa zatim griduje ove widgete..

            korisnici_label1.grid(column = 2, row = 0,pady=(20,0), padx=20, columnspan = 4)
            korisniciButton1.grid(column = 2 , row = 1, pady= 10, padx= 20)
            korisniciButton2.grid(column=3, row = 1,padx=(0,20))
            korisniciButton3.grid(column=4, row = 1, padx = (0,20))
            korisnici_Approve.grid(column=5, row=1,padx=(0,20))
            tree.grid(column = 2, row = 2, rowspan = 7,columnspan = 4,padx=10,pady=(0,10))

            for i in tree.get_children():
                tree.delete(i)
            

            mycursor.execute("SELECT user_id, username, user_email, user_name, user_surname, status FROM users")
            results = mycursor.fetchall()
            brojac = 0
            for result in results:
                tree.insert('','end',iid=brojac,text='',values= result)
                brojac = brojac+1


        def modultwoopen(event):
            removeWidgets()
            klijenti_label1.grid(row=1,column = 2)
            klijenti_label2.grid(row=1,column = 3)
        
        def modulthreeopen(event):
            removeWidgets()
            taskovi_label1.grid(row=1, column=2)
            taskovi_label2.grid(row=2,column = 2)
        def modulefouropen(event):
            removeWidgets()
            labelneki.grid(row=1, column = 3)
        def modulefiveopen(event):
            removeWidgets()
            labelpet.grid(row = 1, column = 3)
        def modulesixopen(event):
            removeWidgets()
            labelenver.grid(row = 1, column = 3)
            #xd = KorisniciModule(parent)
            

        def exitprogram(event):
            self.parent.destroy()
        #moduli

        def deleteUser():
            selected_item=tree.selection()[0]
            item_text = tree.item(selected_item,"values")
            user_id = item_text[0]
            user_name = item_text[1]
            mycursor.execute("DELETE FROM users WHERE user_id =%s",(user_id,))
            mydb.commit()
            tree.delete(selected_item)
            
        def editUser():

            def SubmitEdit():
                tree.item(selected_item, text="", values= (user_id, usernametext.get(),emailtext.get(),nametext.get(),surnametext.get(),status) )

                querry = "UPDATE users SET username = %s,user_name=%s,user_email=%s,user_surname=%s WHERE user_id = %s"
                values = (usernametext.get(), nametext.get(), emailtext.get(), surnametext.get(), user_id )
                mycursor.execute(querry, values)
                mydb.commit()
                messagebox.showinfo(title = "Uspješan edit", message = f"Uspješno ste editovali korisnika ID {user_id}")
                edituser.destroy()

            selected_item = tree.selection()[0]
            item_text = tree.item(selected_item, "values")

            edituser = Toplevel(parent)
            edituser.title("Edit user")
            user_id = item_text[0]
            user_username = item_text[1]
            user_email = item_text[2]
            user_name = item_text[3]
            user_surname = item_text[4]
            status = item_text[5]

            usernametext = StringVar()
            usernameLabel = Label(edituser, text = "Username").grid(column = 0, row = 0)
            usernameEntry = Entry(edituser, command = None,textvariable=usernametext)
            usernameEntry.grid(column = 1, row = 0)
            usernameEntry.insert(0, user_username)

            emailtext = StringVar()
            emailLabel = Label(edituser, text = "Email").grid(column = 2, row = 0)
            emailEntry = Entry(edituser, command = None, textvariable = emailtext)
            emailEntry.grid(column = 3, row = 0)
            emailEntry.insert(0, user_email)

            nametext = StringVar()
            nameLabel = Label(edituser, text = "Name").grid(column = 0, row = 1)
            nameEntry = Entry(edituser, command = None, textvariable = nametext)
            nameEntry.grid(column = 1, row = 1)
            nameEntry.insert(0, user_name)

            surnametext = StringVar()
            surnameLabel = Label(edituser, text = "Surname").grid(column = 2, row = 1)
            surnameEntry = Entry(edituser, command = None, textvariable = surnametext)
            surnameEntry.grid(column = 3, row = 1)
            surnameEntry.insert(0, user_surname)

            submitButton = Button(edituser, text = "Submit", command = SubmitEdit).grid(columnspan = 4)

        def ApprovedUsers():
            for i in tree.get_children():
                tree.delete(i)
            
            mycursor.execute("SELECT user_id, username, user_email, user_name, user_surname, status FROM users WHERE status = 0")
            results = mycursor.fetchall()
            brojac = 0
            for result in results:
                tree.insert('','end',iid=brojac,text='',values= result)
                brojac = brojac+1

        def ApproveUser():
            selected_item = tree.selection()[0]
            item_text = tree.item(selected_item, "values")
            user_id = item_text[0]
            user_username = item_text[1]
            user_email = item_text[2]
            user_name = item_text[3]
            user_surname = item_text[4]
            status = "1"
            tree.item(selected_item, text="", values= (user_id, user_username, user_email,user_name,user_surname,status) )
            mycursor.execute("UPDATE users SET status = %s WHERE user_id = %s",(status, user_id))
            mydb.commit()
            messagebox.showinfo(title = "Uspješno odobravanje", message = f"Uspješno ste odobrili korisnika ID {user_id}")

        #widgets



        menulabel = tk.Label(self,text = "Glavni meni",font=self.ralewayFont)
        menulabel.grid(row=0, column =0,pady=(20,0))

        welcomeLabel = tk.Label(self, text="Dobrodošli nazad...")
        welcomeLabel.grid(row = 0, column = 2, rowspan = 8, padx=(100,0))
        welcomeLabel.config(font=(self.headingFont, 36, "italic"))
        welcomeLabel.config(fg = "#c5c6c7")

        button_moduleone = tk.Button(
            self,
            text = "Korisnici",
            padx = 20,
            width = 80, 
            image = self.usersimage,
            compound = RIGHT,
            font = self.ralewayFont)
        button_moduleone.grid(column = 0, row = 1, padx = 10, pady = 10)

        button_moduletwo = tk.Button(
            self,
            text = "Klijenti",
            padx = 20,
            width = 80,
            image = self.clientsimage,
            compound = RIGHT,
            font = self.ralewayFont)
        button_moduletwo.grid(column = 0, row = 2, padx = 5, pady=(0,10))

        button_modulethree = tk.Button(
            self,
            text = "Taskovi",
            padx = 20,
            width = 80,
            image = self.tasksimage,
            compound = RIGHT,
            font = self.ralewayFont)
        button_modulethree.grid(column = 0, row = 3, padx = 5, pady=(0,10))

        button_modulefour = tk.Button(
            self,
            text = "Projekti",
            padx = 20,
            width = 80,
            image = self.projectimage,
            compound = RIGHT,
            font = self.ralewayFont)
        button_modulefour.grid(column = 0, row = 4, padx = 5, pady=(0,10))

        button_modulefive = tk.Button(
            self,
            text = "Leadovi",
            padx = 20,
            width = 80,
            image = self.leadsimage,
            compound = RIGHT,
            font = self.ralewayFont)
        button_modulefive.grid(column = 0, row = 5, padx = 5, pady=(0,10))

        button_modulesix = tk.Button(
            self,
            text = "Reports",
            padx = 20,
            width = 80,
            image = self.reportsimage,
            compound = RIGHT,
            font = self.ralewayFont)
        button_modulesix.grid(column = 0, row = 6, padx = 5, pady=(0,10))

        button_exitmodule = tk.Button(
            self,
            text = "Exit",
            padx = 20,
            image = self.logoutimage,
            width = 28,
            height = 28)
        button_exitmodule.grid(column = 0, row = 7, padx = 9, pady=10, sticky = "ES")

        separator = ttk.Separator(self, orient = VERTICAL).grid(column = 1, row = 0, rowspan = 20, sticky = "ns")

        button_moduleone.bind('<Button-1>', moduloneopen)
        button_moduletwo.bind('<Button-1>', modultwoopen)
        button_modulethree.bind('<Button-1>', modulthreeopen)
        button_modulefour.bind('<Button-1>', modulefouropen)
        button_modulefive.bind('<Button-1>', modulefiveopen)
        button_modulesix.bind('<Button-1>', modulesixopen)
        button_exitmodule.bind('<Button-1>', exitprogram)


    ############################################################################
    ######################## MODUL 1 ###########################################

        korisnici_label1 = tk.Label(self, text = "Korisnici Panel",font = self.ralewayFont,width=15) 
        korisniciButton1 = tk.Button(self, text="Uredi korisnika", command = editUser,width=15)           
        korisniciButton2 = tk.Button(self,text="Obrisi korisnika",command = deleteUser,width=15)
        korisniciButton3 = tk.Button(self, text="Prikazi neodobrene", command=ApprovedUsers,width=15) 
        korisnici_Approve = tk.Button(self, text="Odobri",command=ApproveUser,width=15)             

 


        tree = ttk.Treeview(self, columns=('ID', 'Username', 'Email', 'Ime','Prezime','Status'))
        #tree = ttk.Treeview(self)
        tree['columns']= ('ID', 'Username', 'Email', 'Ime','Prezime','Status')

        tree.column("#0",width = 0,stretch= NO)
        tree.column("ID",anchor=W,width = 60)
        tree.column("Username",anchor=W,width=120)
        tree.column("Email",anchor=W,width=150)
        tree.column("Ime",anchor=W,width=100)
        tree.column("Prezime",anchor=W,width=100)
        tree.column("Status",anchor=W,width=80)
        # Set the heading (Attribute Names)
        tree.heading('#0', text='')
        tree.heading('ID', text='ID')
        tree.heading('Username', text='Username')
        tree.heading('Email', text='Email')
        tree.heading('Ime', text='Ime')
        tree.heading('Prezime', text='Prezime')
        tree.heading('Status', text='Status')
 
        

    ############################################################################
    ######################## MODUL 2 ###########################################

        klijenti_label1 = tk.Label(self, text = "Klijent")
        klijenti_label2 = tk.Label(self, text = "Klijent1")

    ############################################################################
    ######################## MODUL 3 ###########################################
        taskovi_label1 = tk.Label(self, text= "Taskovi")
        taskovi_label2 = tk.Label(self, text= "Taskovi2")

    ################################# MODUL 4 ###############################
    #########################################################################
        labelneki = tk.Label(self, text="Nesot") 


    ################################# MODUL 5 ###############################   
    #########################################################################
        labelpet = tk.Label(self, text = "Module 5")
    ################################# MODUL 6 ###############################   
    #########################################################################

        labelenver = tk.Label(self, text = "Modul 6 xD")