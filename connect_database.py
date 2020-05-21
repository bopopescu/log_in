import mysql.connector


def connect(username, password):
    global mydb

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="log_in")

    if (mydb):
        print("Connection with db Succesfull")
    else:
        print("Connection with db unsuccesfull")


def is_user_registered(username):
    mycursor = mydb.cursor()
    sql = "SELECT nombre from usuarios"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for row in myresult:
        if row.__contains__(username):
            return True

    return False


def is_password_correct(username, password):
    mycursor = mydb.cursor()
    sql = "SELECT contraseña from usuarios WHERE nombre='" + username + "'"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    if myresult.__contains__(password):
        return True


def add_user(username, password):
    mycursor = mydb.cursor()
    sql = "INSERT INTO usuarios (nombre,contraseña) VALUES (%s,%s)"
    usuary = [(username, password)]
    mycursor.executemany(sql, usuary)

    mydb.commit()
