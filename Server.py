''' Designed by BROOWNN DeVELOPERs'''
## Code for the server ##
import socket

def server_program():
	host = socket.gethostname()
	port = 5000

	Serv_socket= socket.socket()


	Serv_socket.bind((host,port))
	Serv_socket.listen(2)
	conn, address = Serv_socket.accept()
	print("Connection from: " + str(address))	
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print("Ms Client :~ " + str(data))
		data = input('You :~ ')
		conn.send(data.encode())

	conn.close()

if __name__ == '__main__':
	server_program()			


