import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()



def get_fullname_by_id(user_id):
    cursor.execute(f'''
        SELECT last_name, first_name, fathers_name, (last_name || ' ' || first_name || ' ' || fathers_name) as fio FROM users WHERE id = "{user_id}" LIMIT 1
        ''')
    
    return cursor.fetchall()[0]

# user = get_fullname_by_id(7)

def get_user_by_id(user_id):
    cursor.execute(f'''
        SELECT users.last_name, users.first_name, users.fathers_name, groups.name, faculties.name 
                   FROM users 
                    JOIN groups ON groups.id = users.group_id
                    JOIN faculties ON faculties.id = groups.faculty_id
                   WHERE users.id = "{user_id}" LIMIT 1
        ''')
    
    return cursor.fetchall()[0]

#user = get_user_by_id(5)

def get_user2_by_id(user_id):
    cursor.execute(f'''
        SELECT last_name, first_name, fathers_name, (SELECT groups.name FROM groups WHERE groups.id = users.group_id) as group_name
                   FROM users 
                   WHERE id = "{user_id}" LIMIT 1
        ''')
    
    return cursor.fetchall()[0]


# user = get_user2_by_id(5)

def get_users_like_by_last_name(text):
    cursor.execute(f'''
       -- SELECT last_name, first_name, fathers_name FROM users WHERE last_name LIKE "%{text}%";
       -- SELECT last_name, first_name, fathers_name FROM users WHERE last_name LIKE "%{text}";
       SELECT last_name, first_name, fathers_name FROM users WHERE last_name LIKE "_{text}%";
        ''')
    
    return cursor.fetchall()

#users = get_users_like_by_last_name('а')

#print(
#    'users', users
#)

def count_students_on_group():
    cursor.execute(f'''
        SELECT COUNT(users.id) AS count_students, groups.name FROM users
            JOIN groups ON groups.id = users.group_id
        GROUP BY users.group_id 
        
        -- HAVING COUNT(users.id) > 1
    ''')
    
    return cursor.fetchall()

# result = count_students_on_group()
# print(result)

def get_birth_days():
    cursor.execute(f'''
        SELECT last_name, strftime('%d-%m', users.birth_date) FROM users
    ''')
    
    return cursor.fetchall()


result = get_birth_days()
print(result)


connection.commit()
connection.close()