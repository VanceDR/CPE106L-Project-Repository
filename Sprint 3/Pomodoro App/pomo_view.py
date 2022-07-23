import tkinter.ttk as ttk
import tkinter.font as font
import tkinter as tk

class PomoView(ttk.Frame):
    def __init__(self,master):
        """Displays the GUI of the Application"""
        super(PomoView,self).__init__(master)
        # MENU UI #
        menu = tk.Menu(self.master)
        """Menu"""
        self.master.config(menu=menu)

        fileMenu = tk.Menu(menu, tearoff=0)
        """File Menu"""
        menu.add_cascade(label="File", menu=fileMenu)

        fileMenu.add_command(label="Save Tasks")
        fileMenu.add_command(label="Open Tasks")
        fileMenu.add_command(label="Exit Program")

        settingsMenu = tk.Menu(menu, tearoff=0)
        """Settings Menu"""
        menu.add_cascade(label="Settings", menu=settingsMenu)
        settingsMenu.add_command(label="Change Focus Time")
        settingsMenu.add_command(label="Change Short Break Time")
        settingsMenu.add_command(label="Change Long Break Time")
        settingsMenu.add_command(label="Reset to Default Values")

        # POMODORO COLUMN UI #
        self.pomodoroFrame = ttk.Frame(self)
        """Pomodoro Column"""

        
        self.timerControlsFrame = ttk.Frame(self.pomodoroFrame)
        """Timer Controls"""
        self.startButton = ttk.Button(self.timerControlsFrame, text="▶", width=5)
        self.startButton.pack(side='left')
        self.stopButton = ttk.Button(self.timerControlsFrame, text="■", width=5)
        self.stopButton.pack(side='left', padx=10)
        self.resetButton = ttk.Button(self.timerControlsFrame, text="⏮", width=5)
        self.resetButton.pack(side='left')
        self.timerControlsFrame.grid(row=0, column=0)

        self.timerDisplayFrame = ttk.Frame(self.pomodoroFrame)
        """Timer Display"""
        self.labelvariable = tk.StringVar(self.timerDisplayFrame)
        self.labelvariable.set("00:00")
        self.thelabel = ttk.Label(self.timerDisplayFrame,textvariable = self.labelvariable,font=('Consolas',50))
        self.thelabel.pack(side='top')
        self.currentTimer = ttk.Label(self.timerDisplayFrame,text="Start Pomodoro",font=('Consolas',20))
        self.currentTimer.pack(side='top')
        self.timerDisplayFrame.grid(row=1, column=0,padx=20, pady=10)
    
        
        self.timerDurationControlsFrame = ttk.Frame(self.pomodoroFrame)
        """Timer Duration Controls"""
        self.firstButton = tk.Button(self.timerDurationControlsFrame,text="Pomodoro",command=self.pomodoroTime)
        self.firstButton.grid(sticky='W', row=0, column=0)
        self.pomoTimeLabel = ttk.Label(self.timerDurationControlsFrame, text="25:00")
        self.pomoTimeLabel.grid( row=1, column=0)
        self.secondButton = tk.Button(self.timerDurationControlsFrame,text="Short Break",command=self.shortBreakTime)
        self.secondButton.grid(sticky='W', row=0, column=1, padx=10)
        self.shortTimeLabel = ttk.Label(self.timerDurationControlsFrame, text="05:00")
        self.shortTimeLabel.grid( row=1, column=1)
        self.thirdButton = tk.Button(self.timerDurationControlsFrame,text="Long Break",command=self.longBreakTime)
        self.thirdButton.grid(sticky='W', row=0, column=2)
        self.longTimeLabel = ttk.Label(self.timerDurationControlsFrame, text="10:00")
        self.longTimeLabel.grid( row=1, column=2)
        self.timerDurationControlsFrame.grid(row=2, column=0,padx=10,pady=0)

        
        self.taskAndEstimationDisplay = ttk.Frame(self.pomodoroFrame)
        """Current Task and Estimation Display"""
        self.currentTaskLabel = ttk.Label(self.taskAndEstimationDisplay, text="Current Task: ")
        self.currentTaskLabel.grid(row=0, column=0, columnspan=2)
        self.currentTask = ttk.Label(self.taskAndEstimationDisplay, text="Example Current Task", font=16, wraplength=200)
        self.currentTask.grid(row=1,column=0, columnspan=2)
        self.estimatedPomodorosLabel = ttk.Label(self.taskAndEstimationDisplay, text="Estimated Pomodoros Left: ")
        self.estimatedPomodorosLabel.grid(row=2,column=0)
        self.estimatedPomodoros = ttk.Label(self.taskAndEstimationDisplay, text="2.0", font=16)
        self.estimatedPomodoros.grid(row=3,column=0)
        self.taskAndEstimationDisplay.grid(row=3, column=0,padx=10,pady=5)

        self.pomodoroFrame.grid(column=0, row=0)

        # TASK COLUMN UI #
        self.tasksFrame = ttk.Frame(self)
        """Task Frame"""
        self.tasksListFrame = ttk.Frame(self.tasksFrame)
        """Task List Frame"""

        self.scrollBar = ttk.Scrollbar(self.tasksListFrame, orient='vertical')
        self.scrollBar.pack(side='right', fill='y')

        self.taskTreeview = ttk.Treeview(self.tasksListFrame, columns=('Task Title', 'Left','Initial', 'Status'), selectmode='browse')

        self.doingFont = font.Font(family="Helvetica",size=10, weight="bold")
        self.notstartedFont = font.Font(family="Helvetica",size=10, slant="italic")
        self.doneFont = font.Font(family="Helvetica",size=10, weight="normal", overstrike=1)

        self.taskTreeview.tag_configure('doing', background="tomato", foreground="black", font=self.doingFont)
        self.taskTreeview.tag_configure('notstarted', background="light blue", foreground="black", font=self.notstartedFont)
        self.taskTreeview.tag_configure('done', background="green yellow", foreground="black", font=self.doneFont)

        self.taskTreeview.heading(column='Task Title',text='Task Title',anchor='w')
        self.taskTreeview.column(column='Task Title', width=200,stretch=False)
        
        self.taskTreeview.heading(column='Left',text='Left',anchor='w')
        self.taskTreeview.column(column='Left', width=40,stretch=False)

        self.taskTreeview.heading(column='Initial',text='Initial',anchor='w')
        self.taskTreeview.column(column='Initial', width=40,stretch=False)

        self.taskTreeview.heading(column='Status',text='Status',anchor='w')
        self.taskTreeview.column(column='Status', width=80,stretch=False)

        self.taskTreeview['show'] = 'headings'
        self.taskTreeview.pack(side='left')

        self.taskTreeview.config(yscrollcommand=self.scrollBar.set)
        self.scrollBar.config(command=self.taskTreeview.yview)

        """SAMPLE TASKS IN THE TREEVIEW"""
        tasks = [
            {"Title": "Task 2: Never", "CurrentDuration": 6, "InitialDuration": 6,"Status": "Doing"},
            {"Title": "Task 3: Gonna", "CurrentDuration": 9, "InitialDuration": 9,"Status": "Not Started"},
            {"Title": "Task 4: Give", "CurrentDuration": 4, "InitialDuration": 4,"Status": "Not Started"},
            {"Title": "Task 5: You", "CurrentDuration": 2, "InitialDuration": 2,"Status": "Not Started"},
            {"Title": "Task 1: Up", "CurrentDuration": 0, "InitialDuration": 6,"Status": "Done"},
        ]
        count = 0
        for task in tasks:
            if task["Status"] == "Doing":
                self.taskTreeview.insert(parent='', index='end', iid=count, text="", values=(task["Title"],task["CurrentDuration"],task["InitialDuration"],task["Status"]), tags=('doing',))
            elif task["Status"] == "Done":
                self.taskTreeview.insert(parent='', index='end', iid=count, text="", values=(task["Title"],task["CurrentDuration"],task["InitialDuration"],task["Status"]), tags=('done',))
            else:
                self.taskTreeview.insert(parent='', index='end', iid=count, text="", values=(task["Title"],task["CurrentDuration"],task["InitialDuration"],task["Status"]), tags=('notstarted',))
            count += 1

        
        self.taskEntryFrame = ttk.Frame(self.tasksFrame)
        """Task List Input"""
        self.taskNameLabel = ttk.Label(self.taskEntryFrame, text="Task Name")
        self.taskNameLabel.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.taskNameInput = ttk.Entry(self.taskEntryFrame, width=36)
        self.taskNameInput.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.taskTimeLabel = ttk.Label(self.taskEntryFrame, text="Est Time (in Minutes)")
        self.taskTimeLabel.grid(row=0, column=1, sticky=tk.W+tk.E, padx=(10,0))
        self.taskTimeEstimateInput = ttk.Entry(self.taskEntryFrame)
        self.taskTimeEstimateInput.grid(row=1, column=1, padx=(10,0), sticky=tk.W+tk.E)
        self.taskEntryFrame.grid(row=1,column=0, sticky=tk.W)

        
        self.taskListControls = ttk.Frame(self.tasksFrame)
        """Task List Controls"""
        self.addTaskButton = ttk.Button(self.taskListControls, text="Add")
        self.addTaskButton.pack(side='left')

        self.delTaskButton = ttk.Button(self.taskListControls, text="Remove")
        self.delTaskButton.pack(side='left', padx=16)

        self.moveUpTaskButton = ttk.Button(self.taskListControls, text="Move Up")
        self.moveUpTaskButton.pack(side='left', padx=(0,16))

        self.moveDownTaskButton = ttk.Button(self.taskListControls, text="Move Down")
        self.moveDownTaskButton.pack(side='left')

        self.taskListControls.grid(row=2,column=0, pady=5, sticky=tk.W)

        self.taskStatsFrame = ttk.Frame(self.tasksFrame)
        self.taskStatsFrame.grid(row=3,column=0)
        self.totalTimeLabel = ttk.Label(self.taskStatsFrame, text="Total Task Time: ")
        self.totalTimeVar = ttk.Label(self.taskStatsFrame)
        self.totalTimeLabel.grid(row=0,column=0)
        self.totalTimeVar.grid(row=0,column=1, padx=(0,30))
        self.totalFocusTime = ttk.Label(self.taskStatsFrame, text="Total Focus Time: ")
        self.totalFocusVar = ttk.Label(self.taskStatsFrame)
        self.totalFocusTime.grid(row=0,column=2)
        self.totalFocusVar.grid(row=0,column=3)
        self.tasksListFrame.grid(row=0,column=0)

        self.tasksFrame.grid(column=1, row=0)

        self.pack()

    def pomodoroTime(self):
        """Change Timer Look to Pomodoro (Red)"""
        self.thelabel.config(foreground="tomato")
        self.firstButton.config(background="tomato", foreground='white')
        self.secondButton.config(background='SystemButtonFace', foreground="black")
        self.thirdButton.config(background='SystemButtonFace',foreground="black")
        self.currentTimer.config(text="Focus Time", foreground="tomato")

    def shortBreakTime(self):
        """Change Timer Look to Short Break (Sky Blue)"""
        self.thelabel.config(foreground="sky blue")
        self.firstButton.config(background='SystemButtonFace',foreground="black")
        self.secondButton.config(background="sky blue")
        self.thirdButton.config(background='SystemButtonFace',foreground="black")
        self.currentTimer.config(text="Short Break", foreground="sky blue")

    def longBreakTime(self):
        """Change Timer Look to Long Break (Blue)"""
        self.thelabel.config(foreground="blue")
        self.firstButton.config(background='SystemButtonFace',foreground="black")
        self.secondButton.config(background='SystemButtonFace',foreground="black")
        self.thirdButton.config(background="blue", foreground='white')
        self.currentTimer.config(text="Long Break", foreground="blue")

    def hideTimerControls(self, show):
        """Hide Timer Control Frame"""
        if not show:
            self.timerControlsFrame.grid()
        else:
            self.timerControlsFrame.grid_remove()

    def hideTaskList(self, show):
        """Hide Task List Frame"""
        if not show:
            self.tasksFrame.grid()
        else:
            self.tasksFrame.grid_remove()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("PomoPython")
    app = PomoView(root)
    root.mainloop()