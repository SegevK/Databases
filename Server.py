import socket
import sqlite3
ip = '0.0.0.0'
port = 8080
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, port))
serv.listen(5)
conn, addr = serv.accept()
(user_name, user_password) = serv.recv(1024)
database = sqlite3.connect('test.db')
sqlcommand = "SELECT name WHERE name = user_name AND password = user_password"
lst = sqlcommand.execute   # lst is the list of users with name and password that were sent #
user_exists = False
for row in lst:
    user_exists = True


if  not user_exists:
    conn.send("wrong name or password, try again")

if user_exists:   # send all data to user, instead of printing it in server
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    print("Opened database successfully")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    print("Operation done successfully")
    conn.close()
