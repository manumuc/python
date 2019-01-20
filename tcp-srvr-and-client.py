Usage of script: python tcp_server.py> 
Usage of script: python tcp_client.py>  

#/usr/bin/python 
# Server for TCP -Client – save as tcp-server.py  

Import socket #  

# socket_stream for constant connection between the client and the server 
my_socket_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# set the hostname 
hostname='localhost' 

# set the port number to listen to 
port_number='113' 

# set up and start th TCP listen 
my_socket.bind((hostname,port_number)) 
my_socket.listen(5) 

while true: 
   # wait infinitely for a client to connect 
   # connection and address are new variables 
   Connection, address = my_socket.accept() 

   # after we accept the connection we inform the client that it is connected 
   connection.send('You are connected') 


#/usr/bin/python 
# Client for TCP Server – save as tcp-client.py 

Import socket #  

# create a socket object and assign it to a variable 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# set the servername 
server_name='localhost' 

# set the port number to connect to 
port_number='113' 

client_socket.connect((server_name,port_name)) 
Data = client.socket.recv(1024) 
Print data 
