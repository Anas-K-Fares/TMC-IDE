import socket
import sys
from Network_largeData import sendMsg, recvMsg, recvall
from Network_listIP import lsIP


class Client:
    def connectTMC(self):
        port = 5000  # socket server port number

        clientSocket = socket.socket()
        try:
            with open('./serverIP', 'r') as f:
                    serverIP=f.read()
            clientSocket.connect((serverIP, port)) # connect to the server
            return clientSocket
        except:
            serverIP = self.updateIP(port)
            try:
                clientSocket.connect((serverIP, port))
                return clientSocket
            except:
                pass

    def sendMsg(self, clientSocket, message):
        clientSocket.send(message.encode())  # send message
            #data = client_socket.recv(1024).decode()  # receive response
        data = recvMsg(clientSocket)
        return data  

    def updateIP(self, port):
        ipList = lsIP()
        for ip in ipList:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.03)
            try:
                clientSocket.connect((ip, port))
                clientSocket.close() # close the connection
                serverIP = ip
                break
            except:
                clientSocket.close()
        try:
            with open('./serverIP', 'w+') as f:
                f.write(serverIP)
            return serverIP
        except:
            return ''

