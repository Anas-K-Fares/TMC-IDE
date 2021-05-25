import socket
import os
import fcntl
import struct

#ip='118.138.188.37'
#sub='255.255.252.0'
def lsIP():
    try:
        ipShow = os.popen("ip -4 route show default").read().split()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((ipShow[2], 0))
        ip = s.getsockname()[0]
        gateway = ipShow[2]
        netmask=socket.inet_ntoa(fcntl.ioctl(s, 35099, struct.pack('256s', bytes(ipShow[4], encoding='UTF-8')))[20:24])
        #print(netmask)

        devDomain=[]
        startIP=[]
        endIP=[]
        hostDomain=''
        for i in range(0, 4):
            devDomain.append(255-int(netmask.split('.')[i]))
            startIP.append(int(ip.split('.')[i]) & int(netmask.split('.')[i]))
            endIP.append(startIP[i] + devDomain[i])
            hostDomain+=str(startIP[i])+'.'

        #print(hostip[:-1])
        ipList=[]
        for x4 in range(0, endIP[0]-startIP[0]+1):
            for x3 in range(0, endIP[1]-startIP[1]+1):
                for x2 in range(0, endIP[2]-startIP[2]+1):
                    for x1 in range(1, endIP[3]-startIP[3]+1):
                        ipList.append(str(startIP[0]+x4)+'.'+str(startIP[1]+x3)+'.'+str(startIP[2]+x2)+'.'+str(startIP[3]+x1))
                       
        return ipList
    except:
        return ''

















