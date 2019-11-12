import socket
ip = '0.0.0.0'
port = 8080
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, port))
serv.listen(5)
conn, addr = serv.accept()
(name, password) = serv.recv(1024)




if(# name or password not in database):
    conn.send("wrong name or password, try again")
    conn = sqlite3.connect('test.db')
print "Opened database successfully";

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()

# all this script is for getting data from products table * need to change vars and names#


else:
#  send the user "WELCOME" and a list of products from the products database #

conn.close()
print 'client disconnected'
