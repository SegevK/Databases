import socket
import pickle
import tkinter as tk
ip = '127.0.0.1'
port = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))


def get_data():
    name = e1.get()
    name = str(name).encode()
    password = e2.get()
    password = str(password).encode()
    client.send(name)
    client.send(password)
    data = client.recv(4096)
    data = pickle.loads(data)
    if data == "wrong name or password, try again":
        while data == "wrong name or password, try again":
            print("please enter username and password")
            name = input("username")
            name = str(name)
            password = input("password")
            password = str(password)
            client.send(name, password)
            data = client.recv(4096)
    print(data)
    master.quit()


master = tk.Tk()
tk.Label(master, text="username").grid(row=0)
tk.Label(master, text="password").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Login', command=get_data).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()
client.close()
