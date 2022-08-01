import tkinter as tk
from tkinter.tix import Tree
import tkinter.ttk as ttk
import tkinter.simpledialog as sd
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import chime
import pathlib
import json

from pomo_view import PomoView
from pomo_model import PomoModel

class PomoController(ttk.Frame):
    def __init__(self, master):
        """PomoController of the PomoView and the PomoModel"""
        super(PomoController,self).__init__(master)
        self.view = PomoView(self.master)
        self.model = PomoModel()
        chime.theme('material')
        menu = tk.Menu(self)
        """Menu"""
        self.master.config(menu=menu)

        loginMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Users", menu=loginMenu)
        loginMenu.add_command(label="Logout", command=self.logoutUser)
        loginMenu.add_command(label="Exit Program", command=self.closeProgram)

        fileMenu = tk.Menu(menu, tearoff=0)
        """File Menu"""
        menu.add_cascade(label="File", menu=fileMenu)

        fileMenu.add_command(label="Save Tasks", command=self.saveTasks)
        fileMenu.add_command(label="Open Tasks", command=self.importTasks)
        

        settingsMenu = tk.Menu(menu, tearoff=0)
        """Settings Menu"""
        menu.add_cascade(label="Settings", menu=settingsMenu)
        settingsMenu.add_command(label="Change Focus Time", command=self.changePomodoroTime)
        settingsMenu.add_command(label="Change Short Break Time", command=self.changeShortBreakTime)
        settingsMenu.add_command(label="Change Long Break Time", command=self.changeLongBreakTime)
        settingsMenu.add_command(label="Reset to Default Values", command=self.resetToDefaultValues)

        """Binding Commands to Controls in PomoView"""
        self.view.moveUpTaskButton.config(command=self.moveUpTask)
        self.view.moveDownTaskButton.config(command=self.moveDownTask)
        self.view.addTaskButton.config(command=self.addTask)
        self.view.delTaskButton.config(command=self.delTask)
        self.view.firstButton.config(command=self.pomodoro)
        self.view.secondButton.config(command=self.shortBreak)
        self.view.thirdButton.config(command=self.longBreak)
        self.view.startButton.config(command=self.startTime)
        self.view.stopButton.config(command=self.stopTime)
        self.view.resetButton.config(command=self.resetTime)
        self.view.taskTreeview.bind('<Button-1>', self.handleResize)
        

        """Initial Methods"""
        self.returnTimerSettings()
        self.hideTimerControls(True)
        self.getCurrentTask()

    def logoutUser(self):
        '''Logouts user and returns Login Application'''
        answer = mb.askyesno("Logout", "Do you want to Logout?")
        if answer:
            mb.showinfo("Logout", "Successfuly Logged Out")
            from login_controller import LoginController
            self.master.destroy()
            main = tk.Tk()
            main.title("PomoPython")
            main.resizable(False, False)
            app = LoginController(main)
            main.focus()
            main.mainloop()

    def saveTasks(self):
        '''Saves Current Tasks in the List in a JSON File'''
        initDir = pathlib.Path().resolve()
        jsonObject = json.dumps(self.model._tasks, indent=4)
        f = fd.asksaveasfile(mode='w', defaultextension=[("JSON Files", "*.json")],filetypes=[("JSON Files", "*.json")], initialfile="Untitled.json", initialdir=initDir)
        if f is None:
            return
        f.write(jsonObject)
        f.close()
        mb.showinfo("Save File", "File Saved ")

    def importTasks(self):
        '''Imports Tasks into the List from a JSON File'''
        initDir = pathlib.Path().resolve()
        f = fd.askopenfile(mode='r', filetypes=[("JSON Files", "*.json")], defaultextension=[("JSON Files", "*.json")], initialdir=initDir)
        if f is not None:
            files = json.load(f)
            self.model._tasks = files
            self.updateList()

    def closeProgram(self):
        '''Closes the Program'''
        answer = mb.askokcancel("Exit Program", "Do you wish to Exit the Program?")
        if answer:
            self.master.destroy()

    #@@@@@@@@@@@@@@@@@@@@@@@@ TASK FUNCTIONS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    def moveUpTask(self):
        """Moving Selected Task Up in Treeview"""
        if self.model._tasks:
            newrow = self.view.taskTreeview.selection()[0]
            if newrow is not None:
                if int(newrow)-1 < 0:
                    return
                else:
                    self.model._tasks.insert(self.view.taskTreeview.index(int(newrow)-1), self.model._tasks.pop(int(newrow)))
                    self.updateList()
                    self.view.taskTreeview.selection_clear()
                    self.view.taskTreeview.selection_set(int(newrow)-1)

    def moveDownTask(self):
        """Moving Selected Task Down in Treeview"""
        if self.model._tasks:
            newrow = self.view.taskTreeview.selection()[0]
            if newrow is not None:
                if int(newrow)+1 >= self.model._count:
                    return
                else:
                    self.model._tasks.insert(self.view.taskTreeview.index(int(newrow))+1, self.model._tasks.pop(int(newrow)))
                    self.updateList()
                    self.view.taskTreeview.selection_clear()
                    self.view.taskTreeview.selection_set(int(newrow)+1)

    def updateList(self):
        """Updating the Treeview"""
        self.clearList()
        self.model._count = 0
        for task in self.model._tasks:
            if (task["Status"] == "Doing" and self.model._count != 0) or task["Status"] != "Done" and self.model._count != 0:
                task["Status"] = "Not Started"
            if (self.model._count == 0):
                task["Status"] = "Doing"
            if task["Status"] == "Doing":
                self.view.taskTreeview.insert(parent='', index='end', iid=self.model._count, text="", values=(task["Title"],task["CurrentDuration"],task["InitialDuration"],task["Status"]), tags=('doing',))
            elif task["Status"] == "Done":
                self.view.taskTreeview.insert(parent='', index='end', iid=self.model._count, text="", values=(task["Title"],task["CurrentDuration"],task["InitialDuration"],task["Status"]), tags=('done',))
            else:
                self.view.taskTreeview.insert(parent='', index='end', iid=self.model._count, text="", values=(task["Title"],task["CurrentDuration"],task["InitialDuration"],task["Status"]), tags=('notstarted',))
            self.model._count += 1
        self.getCurrentTask()
        self.getEstimatedPomodoros()

    def getCurrentTask(self):
        """Displays the Current Task"""
        if self.model._tasks:
            self.view.currentTask.config(text=self.model._tasks[0]["Title"])
            self.model._taskTime = self.model._tasks[0]["CurrentDuration"] * 60
            self.model._tasks[0]["Status"] = "Doing"
        else:
            self.view.currentTask.config(text=" ")

    def updateCurrentTaskTime(self):
        """Updates the Task's Time when Pomodoro Ended and Time Still left in the Task"""
        if self.model._tasks:
            self.model._tasks[0]["CurrentDuration"] = self.model._taskTime
        self.updateList()

    def getEstimatedPomodoros(self):
        """Gets the Estimated Number of Pomodoro needed to Complete the Tast List"""
        if self.model._tasks:
            est = 0
            total = 0
            for task in self.model._tasks:
                est += task["CurrentDuration"]
                total += task["InitialDuration"]
            est = est * 60
            est = float(est) / self.model._startTime
            self.view.estimatedPomodoros.config(text=est)
            self.view.totalTimeVar.config(text=total)
            self.view.totalFocusVar.config(text=self.model._totalFocus)
        else:
            self.view.estimatedPomodoros.config(text=" ")

    def clearList(self):
        """Clearing the Treeview"""
        for entry in self.view.taskTreeview.get_children():
            self.view.taskTreeview.delete(entry)

        self.view.taskNameInput.delete(0, 'end')
        self.view.taskTimeEstimateInput.delete(0, 'end')

    def setTaskToDone(self):
        """Sets the Current / Topmost Task Status to Done"""
        if self.model._tasks:
            self.model._tasks[0]["Status"] = "Done"
            self.model._tasks.append(self.model._tasks.pop(0))
            self.updateList()

    def delTask(self):
        """Deletes the Selected Task in the List"""
        if self.model._tasks:
            selected = self.view.taskTreeview.selection()[0]
            if selected is not None:
                # print("Deleted: ",self.model._tasks[int(selected)])
                del self.model._tasks[int(selected)]
                self.view.taskTreeview.delete(int(selected))
                self.updateList()

    def addTask(self):
        """Adding Task into the Treeview"""
        if (self.view.taskNameInput.get() != "" and self.view.taskTimeEstimateInput.get() != ""):
            self.model._tasks.insert(
                self.model._count, 
                {"Title": str(self.view.taskNameInput.get()), "CurrentDuration":float(self.view.taskTimeEstimateInput.get()),"InitialDuration":float(self.view.taskTimeEstimateInput.get()), "Status":"Not Started"}
                )
            self.updateList()

    def handleResize(self, event):
        """Disables Resizing on the Treeview"""
        if self.view.taskTreeview.identify_region(event.x, event.y) == "separator":
            return "break"

    #@@@@@@@@@@@@@@@@@@@@@@@@ TIMER FUNCTIONS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    def hideTimerControls(self, show):
        """Hides the Timer Controls"""
        self.view.hideTimerControls(show)

    def hideTaskList(self, show):
        """Hides the Task List"""
        self.view.hideTaskList(show)

    def returnTimerSettings(self):
        """Returns the Current Timer Values Set"""
        currentSetting = [self.model._pomodoroTime, self.model._shortBreakTime, self.model._longBreakTime]
        currentSettingString = []
        for time in currentSetting:
            mins, secs = divmod(time, 60)
            timeformat = "{0:02d}:{1:02d}".format(mins, secs)
            currentSettingString.append(timeformat)
        self.model._startTime = self.model._pomodoroTime
        self.view.pomoTimeLabel.config(text=currentSettingString[0])
        self.view.shortTimeLabel.config(text=currentSettingString[1])
        self.view.longTimeLabel.config(text=currentSettingString[2])
        self.getEstimatedPomodoros()

    def changePomodoroTime(self):
        """Changes the Focus Time"""
        answer = sd.askinteger("Input", "Enter your Focus Time in Minutes")
        if answer is not None:
            self.model._pomodoroTime = answer * 60
        self.returnTimerSettings()

    def changeShortBreakTime(self):
        """Changes the Short Break Time"""
        answer = sd.askinteger("Input", "Enter your Short Break Time in Minutes")
        if answer is not None:
            self.model._shortBreakTime = answer * 60
        self.returnTimerSettings()

    def changeLongBreakTime(self):
        """Changes the Long Break Time"""
        answer = sd.askinteger("Input", "Enter your Long Break Time in Minutes")
        if answer is not None:
            self.model._longBreakTime = answer * 60
        self.returnTimerSettings()

    def checkTasks(self):
        """Checks the Number of Pomodoro Done"""
        if self.model._tasks:
            if self.model._numRepetitions % 8 == 0:
                self.longBreak()
                self.model._paused = True
            elif self.model._numRepetitions % 2 == 0:
                self.shortBreak()
                self.model._paused = True
            else:
                self.pomodoro()
                self.model._paused = True

    def resetToDefaultValues(self):
        """Resets the Timers into Default Values"""
        self.model.resetToDefault()
        self.returnTimerSettings()

    def pomodoro(self):
        """Timer Set for Pomodoro"""
        startTime = self.model._pomodoroTime
        if self.model._alarm_id is not None:
            self.master.after_cancel(self.model._alarm_id)
        self.model._paused = False
        self.model._focus = True
        self.view.pomodoroTime()
        self.countdown(startTime)

    def shortBreak(self):
        """Timer Set for Short Break"""
        startTime = self.model._shortBreakTime
        if self.model._alarm_id is not None:
            self.master.after_cancel(self.model._alarm_id)
        self.model._paused = False
        self.model._focus = False
        self.view.shortBreakTime()
        self.countdown(startTime)

    def longBreak(self):
        """Timer Set for Long Break"""
        startTime = self.model._longBreakTime
        if self.model._alarm_id is not None:
            self.master.after_cancel(self.model._alarm_id)
        self.model._paused = False
        self.model._focus = False
        self.view.longBreakTime()
        self.countdown(startTime)

    def startTime(self):
        """ Resume """
        self.model._paused = False
        if self.model._alarm_id is None:
            self.countdown(self.model._startTime)
        self.hideTaskList(True)

    def stopTime(self):
        """ Pause """
        if self.model._alarm_id is not None:
            self.model._paused = True
        self.hideTaskList(False)

    def resetTime(self):
        """ Restore to last countdown value. """
        if self.model._alarm_id is not None:
            self.master.after_cancel(self.model._alarm_id)
            self.model._alarm_id = None
            self.model._paused = False
            self.countdown(self.model._startTime)
            self.model._paused = True
        self.hideTaskList(True)

    def makeWindowTopMost(self):
        self.master.attributes('-topmost',1)
        self.master.attributes('-topmost',0)


    def countdown(self, timeInSeconds, start=True):
        """Changing the Display"""
        
        if start:
            self.model._startTime = timeInSeconds
            self.model._elapsedTime = -1
            self.hideTimerControls(False)
            self.hideTaskList(True)
        if self.model._paused:
            self.model._alarm_id = self.master.after(1000, self.countdown, timeInSeconds, False)
            self.hideTaskList(False)
            self.hideTimerControls(False)
        else:
            self.hideTaskList(True)
            self.hideTimerControls(False)
            mins, secs = divmod(timeInSeconds, 60)
            timeformat = "{0:02d}:{1:02d}".format(mins, secs)
            self.view.labelvariable.set(timeformat)
            self.model._alarm_id = self.master.after(1000, self.countdown, timeInSeconds-1, False)

            if self.model._focus:
                self.model._elapsedTime += 1
                if self.model._elapsedTime == self.model._taskTime:
                    self.model.subtractTaskElasped()
                    self.model.addToTotalFocusTime()
                    self.updateCurrentTaskTime()
                    self.setTaskToDone()
                    self.model._elapsedTime = 0
                
                if timeInSeconds == 0 and self.model._elapsedTime <= self.model._taskTime:
                    self.model.subtractTaskElasped()
                    self.model.addToTotalFocusTime()
                    self.updateCurrentTaskTime()
                    

            if timeInSeconds == 0:
                self.model._numRepetitions += 1
                self.resetTime()
                self.checkTasks()
                self.hideTimerControls(True)
                self.hideTaskList(False)
                self.makeWindowTopMost()
                chime.success()

