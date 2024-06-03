import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


def add_faculties():
    cursor.execute('''
        INSERT INTO faculties (name) VALUES 
            ("БХФ"),
            ("ИФФ"),
            ("ФМФ"),
            ("ИИЯМС"),
            ('ТЭФ')
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
    
def add_user(last_name, first_name, fathers_name, birth_date, email, phone_number, form_of_education, status, password, pk):
    cursor.execute(f'''
        INSERT INTO users (last_name, first_name, fathers_name, birth_date, email, phone_number, form_of_education, status, password, group_id) VALUES 
            ("{last_name}", "{first_name}", "{fathers_name}", "{birth_date}", "{email}", "{phone_number}", "{form_of_education}", {status}, "{password}", {pk})   
        ''')

def get_faculty_by_name(name):
    cursor.execute(f'''
        SELECT * FROM faculties WHERE name = "{name}" LIMIT 1
        ''')

    return cursor.fetchall()

def get_group_by_name(name):
    cursor.execute(f'''
        SELECT id, name FROM groups WHERE name = "{name}" LIMIT 1
        ''')

    return cursor.fetchall()

groups = [
    {
        'group_name': '123',
        'faculty_name': 'БХФ',
    },{
        'group_name': '124',
        'faculty_name': 'БХФ',
    },{
        'group_name': '133',
        'faculty_name': 'БХФ',
    },{
        'group_name': '134',
        'faculty_name': 'БХФ',
    },{
        'group_name': '331',
        'faculty_name': 'ИФФ',
    },{
        'group_name': '332',
        'faculty_name': 'ИФФ',
    },{
        'group_name': '333',
        'faculty_name': 'ИФФ',
    },{
        'group_name': '335',
        'faculty_name': 'ИФФ',
    },{
        'group_name': '431',
        'faculty_name': 'ФМФ',
    },{
        'group_name': '432',
        'faculty_name': 'ФМФ',
    },{
        'group_name': '421',
        'faculty_name': 'ФМФ',
    },{
        'group_name': '423',
        'faculty_name': 'ФМФ',
    },{
        'group_name': '201',
        'faculty_name': 'ИИЯМС',
    },{
        'group_name': '203',
        'faculty_name': 'ИИЯМС',
    },{
        'group_name': '206',
        'faculty_name': 'ИИЯМС',
    },{
        'group_name': '209',
        'faculty_name': 'ИИЯМС',
    },{
        'group_name': '1101',
        'faculty_name': 'ТЭФ',
    },{
        'group_name': '1103',
        'faculty_name': 'ТЭФ',
    },{
        'group_name': '1111',
        'faculty_name': 'ТЭФ',
    },{
        'group_name': '1113',
        'faculty_name': 'ТЭФ',
    }
]

users = [
    {
        'last_name': 'Козырева',
        'first_name': 'Александра',
        'fathers_name': 'Олеговна',
        'birth_date': '26-09-2000',
        'email': 'kozyreva.a@mail.ru',
        'phone_number': '',
        'form_of_education': 'очная',
        'status': '1',
        'password': '183492',
        'group_name': '423',
    },{
        'last_name': 'Малахова',
        'first_name': 'Алёна',
        'fathers_name': 'Сергеевна',
        'birth_date': '20-01-2002',
        'email': 'malahova.a@mail.ru',
        'phone_number': '8-953-913-48-42',
        'form_of_education': 'очная',
        'status': '1',
        'password': 'paroli123',
        'group_name': '423',
    },{
        'last_name': 'Пионов',
        'first_name': 'Алексей',
        'fathers_name': 'Михайлович',
        'birth_date': '06-07-2001',
        'email': 'lesha.01@mail.ru',
        'phone_number': '',
        'form_of_education': 'заочная',
        'status': '1',
        'password': 'qwerty',
        'group_name': '123',
    },{
        'last_name': 'Кирсанов',
        'first_name': 'Антон',
        'fathers_name': 'Олегович',
        'birth_date': '19-04-2001',
        'email': 'kirsanov.a@mail.ru',
        'phone_number': '8-960-970-34-70',
        'form_of_education': 'очная',
        'status': '1',
        'password': 'kingantoha',
        'group_name': '124',
    },{
        'last_name': 'Седунова',
        'first_name': 'Юлия',
        'fathers_name': 'Александровна',
        'birth_date': '10-11-2000',
        'email': 'yulia.s.a@mail.ru',
        'phone_number': '',
        'form_of_education': 'заочная',
        'status': '1',
        'password': '123454321',
        'group_name': '133',
    },{
        'last_name': 'Твардовская',
        'first_name': 'Екатерина',
        'fathers_name': 'Евгеньевна',
        'birth_date': '18-09-2003',
        'email': 'ekaterina@mail.ru',
        'phone_number': '',
        'form_of_education': 'очная',
        'status': '1',
        'password': '4167487',
        'group_name': '423',
    },{
        'last_name': 'Буханцов',
        'first_name': 'Владислав',
        'fathers_name': 'Валериевич',
        'birth_date': '20-02-2002',
        'email': 'BVV@mail.ru',
        'phone_number': '8-909-544-17-13',
        'form_of_education': 'очная',
        'status': '1',
        'password': 'FB6734FG',
        'group_name': '431',
    },{
        'last_name': 'Иванов',
        'first_name': 'Петр',
        'fathers_name': 'Сергеевич',
        'birth_date': '03-08-2002',
        'email': 'ivasha.sergeevich@mail.ru',
        'phone_number': '',
        'form_of_education': 'очно-заочная',
        'status': '0',
        'password': 'ivanivan2002',
        'group_name': '201',
    },{
        'last_name': 'Петрова',
        'first_name': 'Елизавета',
        'fathers_name': 'Петровна',
        'birth_date': '13-05-2001',
        'email': 'petrov.a@mail.ru',
        'phone_number': '8-999-555-05-50',
        'form_of_education': 'очно-заочная',
        'status': '0',
        'password': 'lizapetrova',
        'group_name': '1101',
    },{
        'last_name': 'Яблочная',
        'first_name': 'Светлана',
        'fathers_name': 'Анатольевна',
        'birth_date': '30-12-2003',
        'email': 'sveta2000.a@mail.ru',
        'phone_number': '',
        'form_of_education': 'очная',
        'status': '1',
        'password': 'hgf47hrf438',
        'group_name': '209',
    },

]

def add_groups():
    for item in groups:
        faculty = get_faculty_by_name(item.get('faculty_name'))
        if not faculty:
            continue
        
        faculty = faculty[0]

        add_group(item.get('group_name'), faculty[0])

def add_users():
    for item in users:
        group = get_group_by_name(item.get('group_name'))
        if not group:
            continue
        
        group = group[0]

        add_user(item.get('last_name'), item.get('first_name'), item.get('fathers_name'), item.get('birth_date'), item.get('email'), item.get('phone_number'), item.get('form_of_education'), item.get('status'), item.get('password'), group[0])

# faculty = get_faculty_by_name('ФМФ')

# if faculty:
#     faculty = faculty[0]

# add_group('423', faculty[0])
# print(faculty)


add_faculties()
add_groups()
add_users()
#truncate_faculties()


connection.commit()
connection.close()