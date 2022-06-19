import socket
serverName = 'localhost'
serverPort = 12002

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = str.encode(input('digite uma palavra '))
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage)
clientSocket.close()