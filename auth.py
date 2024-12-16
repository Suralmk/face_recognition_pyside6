import sqlite3
from PySide6.QtWidgets import QMessageBox
from pathlib import Path
import bcrypt 

# Base Directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Location of DB file
DB_FILE = BASE_DIR / "face.db"

def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn

class Authentication:
    """
    Handles Authentication, session and information about the current logged in user
    """
    def __init__(self):
        self.create_user_table()
        self.create_session_table()

        self.current_user = self.get_current_user() or None
        self.all_users = self.get_all_users()

    def create_user_table(self):
        try:
            conn = create_connection(DB_FILE)
            cursor = conn.cursor()
            query = """
                        CREATE TABLE IF NOT EXISTS Users (
                            id INTEGER PRIMARY KEY, 
                            name TEXT,
                            username TEXT UNIQUE,
                            password TEXT,
                            face_encoding BLOB
                        )
                    """
            cursor.execute(query)
            conn.close()
        except Exception as e:
            print(e)

    def create_session_table(self):
        try:
            conn = create_connection(DB_FILE)
            cursor = conn.cursor()
            query = """ CREATE TABLE IF NOT EXISTS Session (
                            id INTEGER PRIMARY KEY, 
                            name TEXT,
                            username TEXT UNIQUE,
                            face_encoding BLOB
                        )
                    """
            cursor.execute(query)
            conn.close()
        except Exception as e:
            print(e)

    def get_current_user(self):
        conn = create_connection(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Session")
        user = cursor.fetchall() or None
        self.current_user = user
        conn.close()
        print(user)
        return user
    
    # handle registering a new user
    def register_user(self, name, username, password):
        user_data = [name, username, self.hash_password(password)]

        try:
            conn = create_connection(DB_FILE)
            cursor = conn.cursor()
            query = "INSERT INTO Users (name, username, password) VALUES (?,?,?)"
            cursor.execute(query, user_data)
            conn.commit()
            conn.close()
            # update all users
            self.all_users = self.get_all_users()
            return True
        except Exception as e:
            print(e)
            conn.rollback()
            return e
        
    def login_user(self, username, password):
        user = self.get_single_user(username)
        if user is not None:
            if self.check_password(password, user[3]):
                self.set_current_user(user)
                self.current_user = self.get_current_user()
                return True
            else:
                return False
        else:
            return False
        
    def face_login(self, username):
        user = self.get_single_user(username)
        if user is not None:
            self.set_current_user(user)
            self.current_user = self.get_current_user()
            return True
        else:
            return False
        
    def logout_user(self):
        conn = create_connection(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Session")
        conn.commit()
        conn.close()
        self.current_user = self.get_current_user() or None

    def get_single_user(self, username):
        conn = create_connection(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE username='{username}'")
        user = cursor.fetchone() or None
        conn.close()
        return user
    
    def set_current_user(self, user):
        # Excluding the password save other data to sesstion table
        user_data = [user[1], user[2], user[4]]
        try: 
            conn = create_connection(DB_FILE)
            cursor = conn.cursor()
            query = "INSERT INTO Session (name, username, face_encoding) VALUES (?,?,?)"
            cursor.execute(query, user_data)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e) 
            conn.rollback()
            return e
        
    def update_encoding(self, encoding, username):
        print(encoding)
        try: 
            conn = create_connection(DB_FILE)
            cursor = conn.cursor()
            query = f"UPDATE Users SET face_encoding=? WHERE username=?"
            cursor.execute(query, (encoding, username))
            conn.commit()
            conn.close()
            self.current_user = self.get_current_user()
        except Exception as e:
            print(e, "Here") 
            conn.rollback()

    @classmethod
    def check_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
    
    @classmethod
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_pass

    @classmethod
    def get_all_users(self):
        try:
            conn = create_connection(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users")
            users = cursor.fetchall()
            conn.close()
            return users
        except Exception as e:
            print(e, "get all  users")