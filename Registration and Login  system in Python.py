import sqlite3

# Sqllite database and table
def sqllitefile():
    global conn
    conn = sqlite3.connect('login_data.db')
    global c
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS login_details
                (USER_ID TEXT PRIMARY  KEY NOT NULL,
                 PASSWORD TEXT NOT NULL);''')

# For choosing between register and login
def choose():
    sqllitefile()
    nc = True
    while nc:
        print('Register or Login')
        lor = input('Type Login or Register to continue: ')
        if lor == 'login' or lor == 'Login' or lor == 'LOGIN' :
            nc = False
            return login()
        elif lor == 'register' or lor == 'Register' or lor == 'REGISTER' :
            nc = False
            return register()
        else :
            print('Please only choose between Login and Register')

# Instructions for registration
def useridins():
    print('email/username Instructions:')
    print('1. email/username should have "@" and followed by "."')
    print('2. It should not be like this                                Eg:- @gmail.com')
    print('3. There should not be any "." immediate next to "@"         Eg:- my@.in')
    print('4. It should not start with special characters and numbers   Eg:- 123#@gmail.com')
def passwordins():
    print('Password Instructions:')
    print('1. Password length must be between 5 and 15 \n2. Password must contain atleast one special character')
    print('3. Password must contain atleast one number')
    print('4. Password must contain atleast one upper case character')
    print('5. password must contain atleast contain one lower case character')

# For conditions in user id for registration
def user_id_check_func(u):
    numbers = '0123456789'
    sc = """~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"""
    ati, doti = 0, 0
    for i in range(len(u)):
        if u[i]=='@': ati = i
        elif u[i]=='.': doti = i
    if ((u[0] not in numbers) and (u[0] not in sc)) and (doti > (ati +1)) :
        return True
    else: return False
    
# For conditions in password for registration
def password_check_func(p):
    sc = """~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"""
    numbers = '0123456789'
    uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lc = 'abcdefghijklmnopqrstuvwxyz'
    scb, numbers_b, ucb, lcb = False, False, False, False
    for i in range(len(p)):
        if p[i] in sc: scb = True
        elif p[i] in numbers: numbers_b = True
        elif p[i] in uc: ucb = True
        elif p[i] in lc: lcb = True
    if scb == numbers_b == ucb == lcb == True :
        return True
    else:
        return False

# For Registeration
def register():
    # User Name
    nu = True
    while nu :
        useridins()
        print('---------------------------------------\n ')
        user_id = input('Enter your email/username to register: ')
        user_id_check = user_id_check_func(user_id)
        if user_id_check == False :
            print('--------------------------------------\n ')
            print('Read the below instructions carefully:')
        else: nu = False

    #If user_name already exists
    exist = conn.execute("select USER_ID from login_details where USER_ID like ?", (user_id,)).fetchone()
    if exist :
        print('------------------------------------------\n ')
        print('user_name not available')
        print('Please use different user name to register')
        register()

    # Password
    np = True
    while np:
        passwordins()
        print('----------------------------\n ')
        password = input('Enter password to register: ')
        password_check = password_check_func(password)
        if 5 < len(password) < 16 and password_check:
            np = False
        else:
            print('--------------------------------------\n ')
            print('Read the below instructions carefully:')

    # File Handling
    c.execute("INSERT INTO login_details (USER_ID, PASSWORD) \
          VALUES (?, ?)", (user_id, password))
    conn.commit()
    c.close()
    conn.close()
    print('------------------------\n ')
    print('congratulation....')
    print('Registration is complete')

# For Password in Login
def login_password():
    #Password
    print('-------------------------------------------------------------------------------------\n ')
    print("Enter any number other than 1 to type password or Enter 1 if you forgot your password")
    pc = input()
    if pc == '1' :
        password_id = c.execute("select password from login_details \
                    where user_id = ?", (user_id,)).fetchone()
        print('-----------------------------------------------------------------\n ')
        print(f'Password for the mentioned username - {user_id} is :')
        print(password_id[0])
    else:
        print('--------------------------\n ')
        password = input('Enter Password for login: ')
        password_id_exists = c.execute("select password from login_details \
        where user_id = ? and password = ?", (user_id,password,)).fetchone()
        if password_id_exists:
            print('------------------\n ')
            print('Login Successfull \nWelcome....')
        else:
            print('--------------------------------\n ')
            print('Password is Incorrect, Try again')
            login_password()

# For Username in Login
def login():
    #User Name
    unchoice = 1
    global user_id
    print(          '------------------------------------\n ')
    user_id = input('Enter your username/email to login: ')
    user_id_exists = c.execute("select USER_ID from login_details where USER_ID like ?", (user_id,)).fetchone()
    if not user_id_exists :
        print('------------------------------------------------------------------\n ')
        print('user name does not exist, Please Register first')
        print('choose 1 to register or choose any other number to try login again')
        unlchoice = input()
        if unlchoice != '1': login()
        else:
            unchoice = 0
            register()

    #password
    if unchoice:
        login_password()


if __name__=='__main__':
    choose()
