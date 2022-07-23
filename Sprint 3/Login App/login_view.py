import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as mb
import tkinter as tk

class LoginView(ttk.Frame):
    def __init__(self,master):
        """Displays the GUI of the Application"""
        super(LoginView,self).__init__(master)
        self.pack(ipadx=10,ipady=10)
        self.createWindowWidgets()
        self.createWindowFrame.pack_forget()
        self.forgotPasswordWidgets()
        self.forgotPasswordFrame.pack_forget()
        self.loginWindowWidgets()

    def loginWindowWidgets(self):
        '''Displays the Login GUI'''
        self.loginFrame = ttk.Frame(self)
        self.loginLabel = ttk.Label(self.loginFrame, text="Login Page", font=("TkDefaultFont", 20))
        self.loginLabel.grid(row=0,column=0, columnspan=3, pady=(10,0))
        self.usernameLabel = ttk.Label(self.loginFrame, text="Username")
        self.usernameLabel.grid(row=1, column=0, padx=(10, 5), pady=(10,0), sticky='e')
        self.passwordLabel = ttk.Label(self.loginFrame, text="Password")
        self.passwordLabel.grid(row=2, column=0, padx=(10, 5), pady=10, sticky='e')
        self.usernameEntry = tk.Entry(self.loginFrame, width=30)
        self.usernameEntry.grid(row=1,column=1, padx=10, pady=(10,0))
        self.passwordEntry = tk.Entry(self.loginFrame, show='*', width=30)
        self.passwordEntry.grid(row=2,column=1, padx=10, pady=10)
        self.showPass = tk.IntVar()
        self.passShowCheckbox = ttk.Checkbutton(self.loginFrame, text="Show", variable=self.showPass, onvalue=1, offvalue=0, command=self.showPassword)
        self.passShowCheckbox.grid(row=2,column=2)
        self.loginButton = ttk.Button(self.loginFrame, width=10, text="Login")
        self.loginButton.grid(row=3,column=0,columnspan=3)
        self.createForgotFrame = ttk.Frame(self.loginFrame)
        self.createForgotFrame.grid(row=4,column=0,columnspan=3)
        self.hyperlinkFont = font.Font(underline=True, size=10, family="TkDefaultFont")
        self.createLabel = ttk.Label(self.createForgotFrame, text="Create User", foreground="blue", cursor="hand2", font=self.hyperlinkFont)
        self.forgotLabel = ttk.Label(self.createForgotFrame, text="Forgot Password", foreground="blue", cursor="hand2", font=self.hyperlinkFont)
        
        self.createLabel.grid(row=4, column=0, pady=(10,0), padx=(0,15))
        self.forgotLabel.grid(row=4, column=1, pady=(10,0))
        self.createLabel.bind("<Button-1>", self.showCreateWidgets)
        self.forgotLabel.bind("<Button-1>", self.showForgotWidgets)
        self.loginFrame.pack()

    def createWindowWidgets(self):
        '''Displays the Create User GUI'''
        self.createWindowFrame = ttk.Frame(self)
        self.createPageLabel = ttk.Label(self.createWindowFrame, text="Create User Page", font=("TkDefaultFont", 20))
        self.createPageLabel.grid(row=0,column=0, columnspan=3, pady=(10,0))
        self.usernameLabel = ttk.Label(self.createWindowFrame, text="Username")
        self.usernameLabel.grid(row=1, column=0, padx=(10, 5), pady=(10,0), sticky='e')
        self.passwordLabel = ttk.Label(self.createWindowFrame, text="Password")
        self.passwordLabel.grid(row=2, column=0, padx=(10, 5), pady=(10,0), sticky='e')
        self.passwordLabel2 = ttk.Label(self.createWindowFrame, text="Re-enter Password")
        self.passwordLabel2.grid(row=3, column=0, padx=(10, 5), pady=10, sticky='e')
        self.usernameEntry = tk.Entry(self.createWindowFrame, width=30)
        self.usernameEntry.grid(row=1,column=1, padx=10, pady=(10,0))
        self.passwordEntry = tk.Entry(self.createWindowFrame, show="*", width=30)
        self.passwordEntry.grid(row=2,column=1, padx=10, pady=(10,0))
        self.passwordEntry2 = tk.Entry(self.createWindowFrame, show="*", width=30)
        self.passwordEntry2.grid(row=3,column=1, padx=10, pady=10)
        self.showPass = tk.IntVar()
        self.passShowCheckbox1 = ttk.Checkbutton(self.createWindowFrame, text="Show", variable=self.showPass, onvalue=1, offvalue=0, command=self.showPassword)
        self.passShowCheckbox1.grid(row=2,column=2, pady=(10,0))
        self.buttonFrames = ttk.Frame(self.createWindowFrame)
        self.buttonFrames.grid(row=4, column=0, columnspan=3)
        self.backToLogin = ttk.Button(self.buttonFrames, width=15, text="Back to Login", command=self.returnToLoginFromCreate)
        self.backToLogin.grid(row=0,column=0, sticky='e', padx=(0,10))
        self.createUserButton = ttk.Button(self.buttonFrames, width=15, text="Create User")
        self.createUserButton.grid(row=0,column=1, sticky='e')
        self.createWindowFrame.pack()

    def forgotPasswordWidgets(self):
        '''Displays the Forgot Password GUI'''
        self.forgotPasswordFrame = ttk.Frame(self)
        self.forgotPassLabel = ttk.Label(self.forgotPasswordFrame, text="Forgot Password Page", font=("TkDefaultFont", 20))
        self.forgotPassLabel.grid(row=0,column=0, columnspan=3, pady=(10,0))
        self.usernameLabel = ttk.Label(self.forgotPasswordFrame, text="Username")
        self.usernameLabel.grid(row=1, column=0, padx=(10, 5), pady=(10,0), sticky='e')
        self.passwordLabel = ttk.Label(self.forgotPasswordFrame, text="Password")
        self.passwordLabel.grid(row=2, column=0, padx=(10, 5), pady=(10,0), sticky='e')
        self.passwordLabel2 = ttk.Label(self.forgotPasswordFrame, text="Re-enter Password")
        self.passwordLabel2.grid(row=3, column=0, padx=(10, 5), pady=10, sticky='e')
        self.usernameEntry = tk.Entry(self.forgotPasswordFrame, width=30)
        self.usernameEntry.grid(row=1,column=1, padx=10, pady=(10,0))
        self.passwordEntry = tk.Entry(self.forgotPasswordFrame, show="*", width=30)
        self.passwordEntry.grid(row=2,column=1, padx=10, pady=(10,0))
        self.passwordEntry2 = tk.Entry(self.forgotPasswordFrame, show="*", width=30)
        self.passwordEntry2.grid(row=3,column=1, padx=10, pady=10)
        self.showPass = tk.IntVar()
        self.passShowCheckbox2 = ttk.Checkbutton(self.forgotPasswordFrame, text="Show", variable=self.showPass, onvalue=1, offvalue=0, command=self.showPassword)
        self.passShowCheckbox2.grid(row=2,column=2, pady=(10,0))
        self.buttonFrames1 = ttk.Frame(self.forgotPasswordFrame)
        self.buttonFrames1.grid(row=4, column=0, columnspan=3)
        self.backToLogin = ttk.Button(self.buttonFrames1, width=15, text="Back to Login", command=self.returnToLoginFromForget)
        self.backToLogin.grid(row=0,column=0, sticky='e', padx=(0,10))
        self.createUserButton = ttk.Button(self.buttonFrames1, width=20, text="Update Password")
        self.createUserButton.grid(row=0,column=1, sticky='e')
        self.forgotPasswordFrame.pack()

    def showPassword(self):
        '''Shows and Hides the Password in the Password Boxes'''
        if self.showPass.get() == 1:
            self.passwordEntry.config(show='')
            if self.createWindowFrame.winfo_viewable() or self.forgotPasswordFrame.winfo_viewable():
                self.passwordEntry2.config(show='')
        else:
            self.passwordEntry.config(show='*')
            if self.createWindowFrame.winfo_viewable() or self.forgotPasswordFrame.winfo_viewable():
                self.passwordEntry2.config(show='*')

    def returnToLoginFromCreate(self):
        '''Hides Create User Page and Shows Login Page'''
        self.createWindowFrame.pack_forget()
        self.loginWindowWidgets()

    def returnToLoginFromForget(self):
        '''Hides Forgot Password Page and Shows Login Page'''
        self.forgotPasswordFrame.pack_forget()
        self.loginWindowWidgets()

    def showForgotWidgets(self, event):
        '''Opens Forgot Password Page and Hides Login Page'''
        self.loginFrame.pack_forget()
        self.forgotPasswordWidgets()

    def showCreateWidgets(self, event):
        '''Opens Create User Page and Hides Login Page'''
        self.loginFrame.pack_forget()
        self.createWindowWidgets()

    def missingFields(self):
        '''Checks if the Fields are Missing'''
        warnings = ""
        usernameBool = False
        passwordBool = False
        reenterBool = False
        matchBool = False
        if self.usernameEntry.get() == "":
            warnings += "Username Missing\n"
            self.usernameEntry.config(highlightbackground='red', highlightcolor='red',highlightthickness=1)
        else:
            self.usernameEntry.config(highlightbackground=None, highlightcolor=None,highlightthickness=0)
            usernameBool = True
            
        if self.passwordEntry.get() == "":
            warnings += "Password Missing\n"
            self.passwordEntry.config(highlightbackground='red', highlightcolor='red', highlightthickness=1)
        else:
            self.passwordEntry.config(highlightbackground=None, highlightcolor=None,highlightthickness=0)
            passwordBool = True

        if self.createWindowFrame.winfo_viewable() or self.forgotPasswordFrame.winfo_viewable():
            if self.passwordEntry2.get() == "":
                warnings += "Re-enter your Password Missing\n"
                self.passwordEntry2.config(highlightbackground='red', highlightcolor='red', highlightthickness=1)
            else:
                self.passwordEntry2.config(highlightbackground=None, highlightcolor=None,highlightthickness=0)
                reenterBool = True
            if self.passwordEntry.get() != "" and self.passwordEntry2 != "":
                if self.passwordEntry.get() != self.passwordEntry2.get():
                    warnings += "Passwords do not Match\n"
                    self.passwordEntry.config(highlightbackground='red', highlightcolor='red', highlightthickness=1)
                    self.passwordEntry2.config(highlightbackground='red', highlightcolor='red', highlightthickness=1)
                else:
                    self.passwordEntry.config(highlightbackground=None, highlightcolor=None,highlightthickness=0)
                    self.passwordEntry2.config(highlightbackground=None, highlightcolor=None,highlightthickness=0)
                    matchBool = True

        if self.createWindowFrame.winfo_viewable() or self.forgotPasswordFrame.winfo_viewable():
            if usernameBool and passwordBool and reenterBool and matchBool:
                return True
            else:
                mb.showwarning("Warning", warnings)
                return False
        else:
            if usernameBool and passwordBool:
                return True
            else:
                mb.showwarning("Warning", warnings)
                return False

    def __init__(self,master):
        """Displays the GUI of the Application"""
        super(LoginView,self).__init__(master)
        self.pack(ipadx=10,ipady=10)
        self.createWindowWidgets()
        self.createWindowFrame.pack_forget()
        self.forgotPasswordWidgets()
        self.forgotPasswordFrame.pack_forget()
        self.loginWindowWidgets()

    def loginWindowWidgets(self):
        '''Displays the Login GUI'''
        self.loginFrame = ttk.Frame(self)
        self.loginLabel = ttk.Label(self.loginFrame, text="Login Page", font=("TkDefaultFont", 20))
        self.loginLabel.grid(row=0,column=0, columnspan=3, pady=(10,0))
        self.usernameLabel = ttk.Label(self.loginFrame, text="Username")
        self.usernameLabel.grid(row=1, column=0, padx=(10, 5), pady=(10,0), sticky='e')
        self.passwordLabel = ttk.Label(self.loginFrame, text="Password")
        self.passwordLabel.grid(row=2, column=0, padx=(10, 5), pady=10, sticky='e')
        self.usernameEntry = tk.Entry(self.loginFrame, width=30)
        self.usernameEntry.grid(row=1,column=1, padx=10, pady=(10,0))
        self.passwordEntry = tk.Entry(self.loginFrame, show='*', width=30)
        self.passwordEntry.grid(row=2,column=1, padx=10, pady=10)
        self.showPass = tk.IntVar()
        self.passShowCheckbox = ttk.Checkbutton(self.loginFrame, text="Show", variable=self.showPass, onvalue=1, offvalue=0, command=self.showPassword)
        self.passShowCheckbox.grid(row=2,column=2)
        self.loginButton = ttk.Button(self.loginFrame, width=10, text="Login")
        self.loginButton.grid(row=3,column=0,columnspan=3)
        self.createForgotFrame = ttk.Frame(self.loginFrame)
        self.createForgotFrame.grid(row=4,column=0,columnspan=3)
        self.hyperlinkFont = font.Font(underline=True, size=10, family="TkDefaultFont")
        self.createLabel = ttk.Label(self.createForgotFrame, text="Create User", foreground="blue", cursor="hand2", font=self.hyperlinkFont)
        self.forgotLabel = ttk.Label(self.createForgotFrame, text="Forgot Password", foreground="blue", cursor="hand2", font=self.hyperlinkFont)
        
        self.createLabel.grid(row=4, column=0, pady=(10,0), padx=(0,15))
        self.forgotLabel.grid(row=4, column=1, pady=(10,0))
        self.createLabel.bind("<Button-1>", self.openCreateWindow)
        self.forgotLabel.bind("<Button-1>", self.openForgetWindow)
        self.loginFrame.pack()

    def createWindowWidgets(self):
        '''Displays the Create User GUI'''
        self.createWindowFrame = ttk.Frame(self)
        self.createPageLabel = ttk.Label(self.createWindowFrame, text="Create User Page", font=("TkDefaultFont", 20))
        self.createPageLabel.grid(row=0,column=0, columnspan=3, pady=(10,0))
        self.usernameLabel = ttk.Label(self.createWindowFrame, text="Username")
        self.usernameLabel.grid(row=1, column=0, padx=(10, 5), pady=(10,0), sticky='e')
        self.passwordLabel = ttk.Label(self.createWindowFrame, text="Password")
        self.passwordLabel.grid(row=2, column=0, padx=(10, 5), pady=(10,0), sticky='e')
        self.passwordLabel2 = ttk.Label(self.createWindowFrame, text="Re-enter Password")
        self.passwordLabel2.grid(row=3, column=0, padx=(10, 5), pady=10, sticky='e')
        self.usernameEntry = tk.Entry(self.createWindowFrame, width=30)
        self.usernameEntry.grid(row=1,column=1, padx=10, pady=(10,0))
        self.passwordEntry = tk.Entry(self.createWindowFrame, show="*", width=30)
        self.passwordEntry.grid(row=2,column=1, padx=10, pady=(10,0))
        self.passwordEntry2 = tk.Entry(self.createWindowFrame, show="*", width=30)
        self.passwordEntry2.grid(row=3,column=1, padx=10, pady=10)
        self.showPass = tk.IntVar()
        self.passShowCheckbox1 = ttk.Checkbutton(self.createWindowFrame, text="Show", variable=self.showPass, onvalue=1, offvalue=0, command=self.showPassword)
        self.passShowCheckbox1.grid(row=2,column=2, pady=(10,0))
        self.buttonFrames = ttk.Frame(self.createWindowFrame)
        self.buttonFrames.grid(row=4, column=0, columnspan=3)
        self.backToLogin = ttk.Button(self.buttonFrames, width=15, text="Back to Login", command=self.returnToLoginFromCreate)
        self.backToLogin.grid(row=0,column=0, sticky='e', padx=(0,10))
        self.createUserButton = ttk.Button(self.buttonFrames, width=15, text="Create User")
        self.createUserButton.grid(row=0,column=1, sticky='e')
        self.createWindowFrame.pack()

    def forgotPasswordWidgets(self):
        '''Displays the Forgot Password GUI'''
        self.forgotPasswordFrame = ttk.Frame(self)
        self.forgotPassLabel = ttk.Label(self.forgotPasswordFrame, text="Forgot Password Page", font=("TkDefaultFont", 20))
        self.forgotPassLabel.grid(row=0,column=0, columnspan=3, pady=(10,0))
        self.usernameLabel = ttk.Label(self.forgotPasswordFrame, text="Username")
        self.usernameLabel.grid(row=1, column=0, padx=(10, 5), pady=(10,0), sticky='e')
        self.passwordLabel = ttk.Label(self.forgotPasswordFrame, text="Password")
        self.passwordLabel.grid(row=2, column=0, padx=(10, 5), pady=(10,0), sticky='e')
        self.passwordLabel2 = ttk.Label(self.forgotPasswordFrame, text="Re-enter Password")
        self.passwordLabel2.grid(row=3, column=0, padx=(10, 5), pady=10, sticky='e')
        self.usernameEntry = tk.Entry(self.forgotPasswordFrame, width=30)
        self.usernameEntry.grid(row=1,column=1, padx=10, pady=(10,0))
        self.passwordEntry = tk.Entry(self.forgotPasswordFrame, show="*", width=30)
        self.passwordEntry.grid(row=2,column=1, padx=10, pady=(10,0))
        self.passwordEntry2 = tk.Entry(self.forgotPasswordFrame, show="*", width=30)
        self.passwordEntry2.grid(row=3,column=1, padx=10, pady=10)
        self.showPass = tk.IntVar()
        self.passShowCheckbox2 = ttk.Checkbutton(self.forgotPasswordFrame, text="Show", variable=self.showPass, onvalue=1, offvalue=0, command=self.showPassword)
        self.passShowCheckbox2.grid(row=2,column=2, pady=(10,0))
        self.buttonFrames1 = ttk.Frame(self.forgotPasswordFrame)
        self.buttonFrames1.grid(row=4, column=0, columnspan=3)
        self.backToLogin = ttk.Button(self.buttonFrames1, width=15, text="Back to Login", command=self.returnToLoginFromForget)
        self.backToLogin.grid(row=0,column=0, sticky='e', padx=(0,10))
        self.createUserButton = ttk.Button(self.buttonFrames1, width=20, text="Update Password")
        self.createUserButton.grid(row=0,column=1, sticky='e')
        self.forgotPasswordFrame.pack()

    def showPassword(self):
        '''Shows and Hides the Password in the Password Boxes'''
        if self.showPass.get() == 1:
            self.passwordEntry.config(show='')
            if self.createWindowFrame.winfo_viewable() or self.forgotPasswordFrame.winfo_viewable():
                self.passwordEntry2.config(show='')
        else:
            self.passwordEntry.config(show='*')
            if self.createWindowFrame.winfo_viewable() or self.forgotPasswordFrame.winfo_viewable():
                self.passwordEntry2.config(show='*')

    def returnToLoginFromCreate(self):
        '''Hides Create User Page and Shows Login Page'''
        self.createWindowFrame.pack_forget()
        self.loginWindowWidgets()

    def returnToLoginFromForget(self):
        '''Hides Forgot Password Page and Shows Login Page'''
        self.forgotPasswordFrame.pack_forget()
        self.loginWindowWidgets()

    def openForgetWindow(self, event):
        '''Opens Forgot Password Page and Hides Login Page'''
        self.loginFrame.pack_forget()
        self.forgotPasswordWidgets()

    def openCreateWindow(self, event):
        '''Opens Create User Page and Hides Login Page'''
        self.loginFrame.pack_forget()
        self.createWindowWidgets()

    def missingFields(self):
        '''Checks if the Fields are Missing'''
        warnings = ""
        usernameBool = False
        passwordBool = False
        reenterBool = False
        matchBool = False
        if self.usernameEntry.get() == "":
            warnings += "Username Missing\n"
            self.usernameEntry.config(highlightbackground='red', highlightcolor='red',highlightthickness=1)
        else:
            self.usernameEntry.config(highlightbackground=None, highlightcolor=None,highlightthickness=0)
            usernameBool = True
            
        if self.passwordEntry.get() == "":
            warnings += "Password Missing\n"
            self.passwordEntry.config(highlightbackground='red', highlightcolor='red', highlightthickness=1)
        else:
            self.passwordEntry.config(highlightbackground=None, highlightcolor=None,highlightthickness=0)
            passwordBool = True

        if self.createWindowFrame.winfo_viewable() or self.forgotPasswordFrame.winfo_viewable():
            if self.passwordEntry2.get() == "":
                warnings += "Re-enter your Password Missing\n"
                self.passwordEntry2.config(highlightbackground='red', highlightcolor='red', highlightthickness=1)
            else:
                self.passwordEntry2.config(highlightbackground=None, highlightcolor=None,highlightthickness=0)
                reenterBool = True
            if self.passwordEntry.get() != "" and self.passwordEntry2 != "":
                if self.passwordEntry.get() != self.passwordEntry2.get():
                    warnings += "Passwords do not Match\n"
                    self.passwordEntry.config(highlightbackground='red', highlightcolor='red', highlightthickness=1)
                    self.passwordEntry2.config(highlightbackground='red', highlightcolor='red', highlightthickness=1)
                else:
                    self.passwordEntry.config(highlightbackground=None, highlightcolor=None,highlightthickness=0)
                    self.passwordEntry2.config(highlightbackground=None, highlightcolor=None,highlightthickness=0)
                    matchBool = True

        if self.createWindowFrame.winfo_viewable() or self.forgotPasswordFrame.winfo_viewable():
            if usernameBool and passwordBool and reenterBool and matchBool:
                return True
            else:
                mb.showwarning("Warning", warnings)
                return False
        else:
            if usernameBool and passwordBool:
                return True
            else:
                mb.showwarning("Warning", warnings)
                return False

if __name__ == '__main__':
    root = tk.Tk()
    root.title("PomoPython")
    app = LoginView(root)
    root.mainloop()