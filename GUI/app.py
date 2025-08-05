from tkinter import *
class NLPapp:

    def __init__(self):
        #login GUI
        self.root = Tk()
        self.root.title("MyApp")
        self.root.iconbitmap("Resources/favicon.ico")
        self.root.geometry("400x600")
        self.root.configure(bg='#34495E')

        self.login()
        self.root.mainloop()

    def login(self):
        self.clear()
        login = Label(self.root, text="Login")
        login.pack(pady=(30,30))
        login.configure(font =('algerian',24,'bold'))

        label0 = Label(self.root, text="Username or Email")
        label0.pack(pady=(10,10))

        self.email_entry = Entry(self.root, width=50)
        self.email_entry.pack(pady=(5,10), ipady=4)

        label1 = Label(self.root, text="Password")
        label1.pack(pady=(10,10))

        self.password = Entry(self.root, width=50,show="*")
        self.password.pack(pady=(5,10), ipady=4)

        login_button = Button(self.root, text="Login", width=30, height=2)
        login_button.pack(pady=(10,10), ipady=4)

        label2 = Label(self.root, text="Not a Member?")
        label2.pack(pady=(10,10))

        redirect_button = Button(self.root, text="Register !", width=30, height=2, command=self.reg_gui)
        redirect_button.pack(pady=(10,10), ipady=4)

    def reg_gui(self):
        self.clear()
        login = Label(self.root, text="Login")
        login.pack(pady=(30, 30))
        login.configure(font=('algerian', 24, 'bold'))

        labelx = Label(self.root, text="Enter Name")
        labelx.pack(pady=(10, 10))

        self.name_entry = Entry(self.root, width=50)
        self.name_entry.pack(pady=(5, 10), ipady=4)

        label0 = Label(self.root, text="Username or Email")
        label0.pack(pady=(10,10))

        self.email_entry = Entry(self.root, width=50)
        self.email_entry.pack(pady=(5,10), ipady=4)

        label1 = Label(self.root, text="Password")
        label1.pack(pady=(10, 10))

        self.password = Entry(self.root, width=50, show="*")
        self.password.pack(pady=(5, 10), ipady=4)

        reg_button = Button(self.root, text="Register", width=30, height=2)
        reg_button.pack(pady=(10, 10), ipady=4,command=self.perform_reg)

        label2 = Label(self.root, text="Already a member?")
        label2.pack(pady=(10, 10))

        redirect_button = Button(self.root, text="Login Now !", width=30, height=2, command=self.login)
        redirect_button.pack(pady=(10, 10), ipady=4)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_reg(self):

        #fetch data from GUI
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password.get()

nlp = NLPapp()