import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


def add_faculties():
    cursor.execute('''
        INSERT INTO faculties (name) VALUES 
            ("ФМФ"),
            ("ИЯМС"),
            ("ТЭФ"),
            ("БХФ")
        ''')
    
def truncate_faculties():
    cursor.execute('''
    DELETE FROM faculties
    ''')


def add_group(name, pk):
    cursor.execute(f'''
        INSERT INTO groups (name, faculty_id) VALUES 
            ({name}, {pk})   
        ''')
    
def get_faculty_by_name(name):
    cursor.execute(f'''
        SELECT * FROM faculties WHERE name = "{name}" LIMIT 1
        ''')

    return cursor.fetchall()


faculty = get_faculty_by_name('ФМФ')

if faculty:
    faculty = faculty[0]

print(faculty)

#add_faculties()
#truncate_faculties()
add_group('423', faculty[0])


connection.commit()
connection.close()