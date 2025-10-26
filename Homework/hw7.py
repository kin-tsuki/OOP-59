import sqlite3

connect = sqlite3.connect("Users.db")

cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
""")
connect.commit()

def create_user(name, age, hobby):
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)",
        (name, age, hobby)
    )
    connect.commit()

# create_user('Lorelei', 32, 'Photography')

def read_user():
    cursor.execute("SELECT * from users")
    users = cursor.fetchall()
    for i in users:
        print(f'Name: {i[0]}, Age: {i[1]}, Hobby: {i[2]}')

# read_user()

def update_users(rowid, new_name=None, new_age=None, new_hobby=None):
    updates = []
    new_values = []
    if new_name is not None:
        updates.append('name = ?')
        new_values.append(new_name)
    if new_age is not None:
        updates.append('age = ?')
        new_values.append(new_age)
    if new_hobby is not None:
        updates.append('hobby = ?')
        new_values.append(new_hobby)
    if not updates:
        return

    cursor.execute(
        f"UPDATE users SET {','.join (updates)} WHERE rowid = ?",
    new_values + [rowid]
    )
    connect.commit()


update_users(2, 'Rory', new_hobby='Reading')
update_users(3, new_name='Reina', new_age=24)
read_user()

def delete_users(rowid):
    cursor.execute(f'DELETE FROM users WHERE rowid = {rowid}')
    connect.commit()

delete_users(4)
# read_user()

def read_user_by_id(rowid):
    cursor.execute('SELECT rowid, name, age, hobby FROM users WHERE rowid = ?', (rowid,))
    user = cursor.fetchall()
    for i in user:
        print(f'ID: {i[0]}, Name: {i[1]}, Age: {i[2]}, Hobby: {i[3]}')


read_user_by_id(2)