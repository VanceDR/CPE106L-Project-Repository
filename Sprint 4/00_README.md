# Pomodoro Time Management Application : A Service Learning Activity 

## Information
A Pomodoro Based Time Management Application.

Created by CPE106L-E01_03 4Q2122.

## Libraries Used
- tkinter (& ttk, messagebox, simpledialog, filedialog, font)
- sqlite3
- chime (needed to be installed)
- json
- os
- pathlib

## Files Included
### Login App
- login_app.py - standalone Login Application
- login_controller.py - the Controller of the Login App, interfaces the login model and view.
- login_model.py - the Model of the Login App, stores the Username and Password as well as SQLite methods.
- login_view.py - the View or GUI of the Login App.

### Pomodoro App
- pomo_app.py - standalone Pomodoro Application
- pomo_controller.py - the Controller of the Pomodoro App, interfaces the pomo model and view.
- pomo_model.py - the Model of the Pomodoro App, stores the tasks and timer counters.
- pomo_view.py - the View or GUI of the Pomodoro App.

### Main App
- main_app.py - used to run both Login and Pomo App to form the whole application collects classes from files.
- full_in_one_app.py - single file code, runs like the main_app.

### Task Lists
- There are three JSON files for example task lists.

### Requirements File
- Requirements (requirements.txt) file is included for the dependencies.

## Instructions
### Python Installation
1. Install python by going to https://python.org/ > downloads > download python. After downloading run the installer.

2. At the Python Installation, there is a option to "Add Python to PATH", make sure that that is ticked/enabled. Then proceed to installation.

### VSCode Installation
1. Install VSCode by going to https://code.visualstudio.com/ and downloading the installer and installing it.

### Running the Application
#### Checking Python Installation
1. Open Visual Studio Code, open a new empty folder.

2. Open a new terminal by clicking "Terminal" at the top menu, and clicking "New Terminal".

3. To test if python is correctly installed type `python` in terminal and it should go to a command line with ">>>"

4. To exit, type `exit()` in the terminal

#### Running the Codes
0. Paste the codes into the opened empty folder in VSCode.

1. Create a Virtual Environment by `python -m venv virtualenv`

2. Activate the virtual environment by `virtualenv\scripts\activate`

3. Install Chime (a notification sound library) `pip install chime` or using the requirements file, by `pip install -r requirements.txt`

4. Run the main application `python main_app.py`

5. To Create New User, Click the `Create New User` hyperlink, input your desired Username and Password, and Re-enter your Password to confirm.

6. You can now login and use the app!

> (Optional, to create your own task list, check the provided JSON Files on how to format your task list to be imported into the application.)
> 
> (You can view the SQLite3 Database (loginDatabase.db) using an extension in VSCode for SQLite3 Explorer)

