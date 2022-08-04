# Pomodoro Time Management Application : A Service Learning Activity 

## Information
A Pomodoro Based Time Management Application.
Created by CPE106L-E01_03 4Q2122 with Mentor IVVillamor and Instructor DAPadilla

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

1. Create a Virtual Environment by `python -m venv virtualenv`

2. Activate the virtual environment by `virtualenv\scripts\activate`

3. Install Chime (a notification sound library) `pip install chime`

4. Run the main application `python main_app.py`

5. To Create New User, Click the `Create New User` hyperlink, input your desired Username and Password, and Re-enter your Password to confirm.

6. You can now login and use the app!

> (Optional, to create your own task list, check the provided JSON Files on how to format your task list to be imported into the application.)
> 
> (You can view the SQLite3 Database (loginDatabase.db) using an extension in VSCode for SQLite3 Explorer)

