import socket
ip = '0.0.0.0'
port = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))
print("please enter username and password")
name = input("username")
name = str(name)
password = input("password")
password = str(password)
client.send(name, password)
data = client.recv(1024)
if data == "wrong name or password, try again":
    while data == "wrong name or password, try again":
        print("please enter username and password")
        name = input("username")
        name = str(name)
        password = input("password")
        password = str(password)
        client.send(name, password)
        data = client.recv(1024)
# now the client will recive and print all the data from the server, remmember to close socket in the end #

client.close()
