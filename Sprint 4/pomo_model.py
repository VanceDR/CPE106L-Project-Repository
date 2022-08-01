class PomoModel:
    def __init__(self):
        """Stores the Values of the Application"""
        self._count = 0
        self._tasks = [
            {"Title": "Task 2: Never", "CurrentDuration": 6, "InitialDuration": 6,"Status": "Doing"},
            {"Title": "Task 3: Gonna", "CurrentDuration": 9, "InitialDuration": 9,"Status": "Not Started"},
            {"Title": "Task 4: Give", "CurrentDuration": 4, "InitialDuration": 4,"Status": "Not Started"},
            {"Title": "Task 5: You", "CurrentDuration": 2, "InitialDuration": 2,"Status": "Not Started"},
            {"Title": "Task 1: Up", "CurrentDuration": 0, "InitialDuration": 6,"Status": "Done"},
        ]
        self._focus = True
        self._alarm_id = None
        self._paused = False
        self._startTime = 25 * 60
        self._taskTime = 0
        self._totalFocus = 0
        self._elapsedTime = -1
        self._pomodoroTime = 25 * 60
        self._shortBreakTime = 5 * 60
        self._longBreakTime = 10 * 60
        self._numRepetitions = 1

    def addToTotalFocusTime(self):
        self._totalFocus += self._elapsedTime / float(60)

    def subtractTaskElasped(self):
        """Task Time - Elapsed Time"""
        self._taskTime = self._taskTime - self._elapsedTime
        self._taskTime = self._taskTime / 60

    def resetToDefault(self):
        """Sets Default Values for Timers"""
        self._longBreakTime = 10 * 60
        self._shortBreakTime = 5 * 60
        self._pomodoroTime = 25 * 60
