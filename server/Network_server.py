import socket
from Shell_netVariant import sendToUSBTMC
from Network_largeData import sendMsg, recvMsg, recvall

def listDevices():
    try: #if file not created
        with open('./devList', 'r') as f:
            lines = f.readlines()
            return str(lines)
    except: # return empty
        return ''

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000 
    #print(host)
    server_socket = socket.socket()  # get instance
    # bind host address and port together
    server_socket.bind(('', port))  # blank ip sets the server socket to this device

    
    server_socket.listen(1) # TCP connections such as this one support only one user
    conn, address = server_socket.accept()  # accept new connection
    print("Client ip: " + str(address))
    while True:
        try: # keep server running even if a disconnection happens while receiving data
            data = conn.recv(1024).decode() #1024 bytes
        except:
            pass
        if not data:
            # keep listening for a connection
            server_socket.listen(1)
            conn, address = server_socket.accept()
            continue
        else:
            print("Client ip: " + str(address))
            print(data)
            
        if data.lower() == 'lstmc':
            answer = listDevices()
        elif '::' in data:
            device = data.split('::')[0]
            command = data.split('::')[1]
            answer = sendToUSBTMC('/dev/'+device, command)
        else: # try to correct common errors for console connections
            if data[0:2].lower()=='ls':
                answer='Did you mean \'lstmc\'?'
            else:
                answer='Please enter commands in this format: dev::command'

        if answer!='':
            try:
                sendMsg(conn, answer)
            except:
                pass

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
