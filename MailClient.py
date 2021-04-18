from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.csus.edu",25)#Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != '220':
   print('220 reply not received from server.')
# Send HELO command and print(serv)er response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
   print('250 reply not received from server.')
# Send MAIL FROM command and print(serv)er response.
mailFromCommand = 'MAIL FROM: <thomasduynguyen@csus.edu> \r\n'
clientSocket.send(mailFromCommand)
recvMFC = clientSocket.recv(1024)
print(recvMFC)
if recvMFC[:3] != '250':
   print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print(serv)er response.
# Fill in start
RCPTCommand = 'RCPT TO: <thomasduynguyenviet@gmail.com> \r\n'
clientSocket.send(RCPTCommand)
recvRCPTC = clientSocket.recv(1024)
print(recvRCPTC)
if recvRCPTC[:3] != '250':
   print('250 reply not received from server.')

# Send DATA command and print(serv)er response.

dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand)
recvDC = clientSocket.recv(1024)
print(recvDC)
if recvDC[:3] != '354':
   print('354 reply not received from server.')
# Send message data.
clientSocket.send(msg)
# Message ends with a single period.
clientSocket.send(endmsg)
# Send QUIT command and get server response.
quitCommand = 'QUIT \r\n'
clientSocket.send(quitCommand)
recvQC = clientSocket.recv(1024)
print(recvQC)
if recvQC[:3] != '221':
   print('221 reply not receive from server.')
