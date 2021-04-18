from socket import *
serverPort = 10000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocekt.recv(1024)
	allCapsSetence = sentence.upper()
	connectionSocket.send(allCapsSentence)
	connectionSocket.close()