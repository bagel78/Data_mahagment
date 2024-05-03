import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS faculty (
        faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,
        faculty_name VARCHAR(100) NOT NULL                       
    )''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        group_id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name VARCHAR(100) NOT NULL,
        faculty_id INTEGER(11) NOT NULL,
        FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)                                  
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name VARCHAR(60) NOT NULL,
        first_name VARCHAR(30) NOT NULL,
        fathers_name VARCHAR(30),
        birth_date DATE NOT NULL,
        Email VARCHAR(50) NOT NULL,
        phone_number CHAR(20),
        form_of_education VARCHAR(15) CHECK(form_of_education in ("очная", "заочная", "очно-заочная")) NOT NULL,
        status TINYINT(1) DEFAULT 1 NOT NULL,
        pass VARCHAR(32) NOT NULL,
        group_id INTEGER(11) NOT NULL,
        FOREIGN KEY (group_id) REFERENCES groups(group_id)
    )''')
connection.commit()
connection.close()
