#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
	serverSocket = socket(AF_INET, SOCK_STREAM)

	#Prepare a sever socket
	serverSocket.bind("", port)
	#Fill in start
	print("Web server up on port " + str(port))
	#Fill in end
	serverSocket.listen(1)
	while True:
		#Establish the connection
		print('Ready to serve...')
		connectionSocket, addr = serverSocket.accept()#Fill in start      #Fill in end
		try:
			msg = connectionSocket.recv(1024)#Fill in start    #Fill in end
			nameoffile = msg.split()[1]
            
			
			thefile = open(nameoffile[1:])
			outputdata = thefile.read()#Fill in start     #Fill in end
			print(outputdata)
			thefile.close()

			#Send one HTTP header line into socket
			connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
			#Fill in start
			connectionSocket.send(outputdata)

          
			#connectionSocket.close()
			
			#Send the content of the requested file to the client
			for i in range(0, len(outputdata)):
				connectionSocket.send(outputdata[i].encode())
			connectionSocket.send("\r\n".encode())
			connectionSocket.close()
        
		
		except IOError:
			#Send response message for file not found (404)
			print('404 page not found')
			connectionSocket.send('404 Not Found\n\n')
			#connectionSocket.close()	
			
            
		

	serverSocket.close()
	sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
	webServer(13331)
