import socket
import sqlite3
import pickle
ip = '127.0.0.1'
port = 8080
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, port))
serv.listen(5)
conn, addr = serv.accept()
user_name = conn.recv(1024).decode()
user_password = conn.recv(1024).decode()
currser = sqlite3.connect(r"d:\Users\Cyber\Desktop\Databases\Users.db")
cur = currser.cursor()
sqlcommand = "SELECT Name FROM users WHERE Name=? AND Password=?"
lst = cur.execute(sqlcommand, (user_name, user_password,))   # lst is the list of users with name and password that were sent #
user_exists = False
for row in lst:
    user_exists = True

if not user_exists:
    conn.send("wrong name or password, try again").encode()

if user_exists:   # send all data to user, instead of printing it in server
    products = cur.execute("SELECT * from products")
    print("Opened database successfully")
    list_of_products = []
    for row in products:
        product = []
        product.append("Name = " + str(row[0]))
        product.append("Price = " + str(row[1]))
        list_of_products.append(product)
    print(list_of_products)
    data = pickle.dumps(list_of_products)
    conn.send(data)
    print("Operation done successfully")
    conn.close()
