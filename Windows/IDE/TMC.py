import socket
from Network_client import Client

# provide easy to use library for sending commands
class TMC():
    
    def __init__(self, device):
        self.device = device
        self.client = Client()
        self.conn = self.client.connectTMC()

    def close(self):
        self.conn.close()

    def send(self, command):
        return self.client.sendMsg(self.conn, self.device+'::'+command)



