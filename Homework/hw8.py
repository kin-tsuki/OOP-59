import sqlite3

connect = sqlite3.connect("user_grades.db")

cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade INTEGER NOT NULL,
        subject VARCHAR (50) NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")
connect.commit()


def create_user(name, age, hobby):
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)",
        (name, age, hobby)
    )
    connect.commit()
    print("user added!!")


# create_user("Ren", 16, "Music")
# create_user("Yasu", 14, "Art")
# create_user("Nana", 15, "Photography")

def create_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(subject, grade, user_id) VALUES (?,?,?)',
        (subject, grade, user_id)
    )
    connect.commit()
    print('grade added!!!')


# create_grade(1, "Алегра", 4)
# create_grade(2, "Химия", 4)
# create_grade(3, "Физика", 5)

def read_users_and_grades():
    cursor.execute('''
        SELECT users.name, grades.subject, grades.grade
        FROM users FULL OUTER JOIN grades ON users.id = grades.user_id
    ''')
    users = cursor.fetchall()

    for i in users:
        print(f"NAME: {i[0]} SUBJECT: {i[1]} GRADE: {i[2]}")

# read_users_and_grades()

def create_my_view():
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS user_summary AS
        SELECT name, subject, grade
        FROM users INNER JOIN grades ON users.id = grades.user_id
    """)
    print('VIEW added')
    connect.commit()

create_my_view()

def get_view():
    cursor.execute('SELECT * FROM user_summary')
    users = cursor.fetchall()
    print(users)

get_view()