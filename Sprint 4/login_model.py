import tkinter.messagebox as mb
import sqlite3
import pathlib
import os

class LoginModel:
    def __init__(self):
        '''The Model of the User for Login'''
        self._username = ""
        self._userpass = ""
        self._initDir = os.path.join(pathlib.Path().resolve(),pathlib.Path("loginDatabase.db"))
    
    def checkDatabase(self):
        '''Checks if the Database can be Connected and Creates Table if not.'''
        self.conn = sqlite3.connect(self._initDir)
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "Users" (
                "user_id"	INTEGER NOT NULL,
                "user_name"	TEXT NOT NULL,
                "user_pass"	TEXT NOT NULL,
                PRIMARY KEY("user_id" AUTOINCREMENT)
            );
            """)
            self.conn.commit()
            self.conn.close()
            return True
        except Exception as ex:
            mb.showerror("Error", ex)
            return False

    def insertToDatabase(self):
        '''Inserts Username and User Password into the Database'''
        self.conn = sqlite3.connect(self._initDir)
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
            INSERT INTO "Users" (user_name, user_pass) VALUES (?, ?)""",
            (self._username, self._userpass))
            self.conn.commit()
            self.conn.close()
            return True
        except Exception as ex:
            mb.showerror("Error", ex)
            return False

    def checkUserName(self):
        '''Checks if the Username is already Taken'''
        self.conn = sqlite3.connect(self._initDir)
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
            SELECT COUNT(1) FROM "Users" WHERE user_name = ?
            """,(self._username,))
            result = self.cursor.fetchall()
            if result[0][0] == 1:
                return True
            else:
                return False
        except Exception as ex:
            mb.showerror("Error", ex)
            return False

    def verifyUser(self):
        '''Checks if the Username Password Combination is in the Database'''
        self.conn = sqlite3.connect(self._initDir)
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
            SELECT * FROM "Users" WHERE user_name = ? AND user_pass = ?
            """,
            (self._username,self._userpass))
            result = self.cursor.fetchall()
            if result:
                return True
            else:
                return False
        except Exception as ex:
            mb.showerror("Error", ex)
            return False

    def updateUserPass(self):
        '''Updates the Password of the User'''
        self.conn = sqlite3.connect(self._initDir)
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
            UPDATE "Users" SET user_pass = ? WHERE user_name = ?
            """,
            (self._userpass, self._username))
            self.conn.commit()
            self.conn.close()
            return True
        except Exception as ex:
            mb.showerror("Error", ex)
            return False
