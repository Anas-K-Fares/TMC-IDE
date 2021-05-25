import socket
import os
import struct

#ip='118.138.188.37'
#sub='255.255.252.0'
def lsIP():
    try:
        ip = socket.gethostbyname(socket.gethostname())
        
        gatewayS = os.popen('ipconfig | findstr /i "Gateway"').read()
        gateway = gatewayS[gatewayS.find(': ')+1:].replace(' ','')

        netmaskS=os.popen('ipconfig | findstr /i "Subnet Mask"').read()
        netmask = netmaskS[netmaskS.find(': ')+1:].replace(' ','')
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

















