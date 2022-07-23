import tkinter.ttk as ttk
import tkinter as tk
import tkinter.messagebox as mb

from login_view import LoginView
from login_model import LoginModel

class LoginController(ttk.Frame):
    def __init__(self,master):
        """Connects and Controls the LoginView and LoginModel"""
        super(LoginController,self).__init__(master)

        self.loginView = LoginView(self.master)
        self.loginModel = LoginModel()

        self.loginView.loginButton.config(command=self.loginUser)
        self.loginView.createLabel.bind("<Button-1>", self.gotoCreatePage)
        self.loginView.forgotLabel.bind("<Button-1>", self.gotoForgotPage)

    def gotoCreatePage(self, event):
        '''Navigates from Login to Create Page'''
        self.loginView.showCreateWidgets(event)
        self.loginView.createUserButton.config(command=self.createUser)
        self.loginView.backToLogin.config(command=self.gotoLoginPageFromCreate)

    def gotoForgotPage(self, event):
        '''Navigates from Login to Forget Page'''
        self.loginView.showForgotWidgets(event)
        self.loginView.createUserButton.config(command=self.updatePass)
        self.loginView.backToLogin.config(command=self.gotoLoginPageFromForgot)

    def gotoLoginPageFromCreate(self):
        '''Navigates from Create to Login Page'''
        self.loginView.returnToLoginFromCreate()
        self.loginView.loginButton.config(command=self.loginUser)
        self.loginView.createLabel.bind("<Button-1>", self.gotoCreatePage)
        self.loginView.forgotLabel.bind("<Button-1>", self.gotoForgotPage)

    def gotoLoginPageFromForgot(self):
        '''Navigates from Forget to Login Page'''
        self.loginView.returnToLoginFromForget()
        self.loginView.loginButton.config(command=self.loginUser)
        self.loginView.createLabel.bind("<Button-1>", self.gotoCreatePage)
        self.loginView.forgotLabel.bind("<Button-1>", self.gotoForgotPage)
    

    def updatePass(self):
        '''Updates the User Password'''
        username = self.loginView.usernameEntry.get()
        password = self.loginView.passwordEntry.get()

        self.loginModel._username = username
        self.loginModel._userpass = password

        if self.loginModel.checkDatabase():
            if self.loginView.missingFields():
                if self.loginModel.checkUserName():
                    if self.loginModel.updateUserPass():
                            mb.showinfo("Forget Password", "User Password Changed!")
                            self.gotoLoginPageFromForgot()
                    else:
                        mb.showerror("Error", "User not Password Changed")
                else:
                    mb.showerror("Username Error", "Username is not in Database")
        else:
            mb.showerror("Conection Error", "Error Connecting to Database")


    def createUser(self):
        '''Creates New User'''
        username = self.loginView.usernameEntry.get()
        password = self.loginView.passwordEntry.get()

        self.loginModel._username = username
        self.loginModel._userpass = password

        if self.loginModel.checkDatabase():
            if self.loginView.missingFields():
                if self.loginModel.checkUserName() == False:
                    if self.loginModel.insertToDatabase():
                        mb.showinfo("Create User", "User Created!")
                        self.gotoLoginPageFromCreate()
                    else:
                        mb.showerror("Error", "User not Created")
                else:
                    mb.showwarning("Username Error", "Username already taken")
        else:
            mb.showerror("Conection Error", "Error Connecting to Database")
        
    def loginUser(self):
        '''Verifies the Login of the User'''
        username = self.loginView.usernameEntry.get()
        password = self.loginView.passwordEntry.get()

        self.loginModel._username = username
        self.loginModel._userpass = password

        if self.loginModel.checkDatabase():
            if self.loginView.missingFields():
                if self.loginModel.verifyUser():
                    return
                else:
                    mb.showerror("Login Error", "Username or Password Incorrect")
                    
        else:
            mb.showerror("Connection Error", "Error Connecting to Database")
