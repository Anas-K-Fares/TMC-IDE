# https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
import socket
import struct

def sendMsg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg=bytes(msg, encoding='UTF-8')
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recvMsg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return str(recvall(sock, msglen),'UTF-8')

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data
