import pyudev
from Shell_netVariant import sendToUSBTMC

## script needed to detect USBTMC hotplugs

# file creation and updating with current devices available is handled here
def devListF(action, device):
    try: #if file not created
        with open('./devList', 'r') as f:
            lines = f.readlines()
    except: #create file
        with open('./devList', 'w+') as f:
            lines=['']
    if action=='add':
        with open('./devList', 'w') as f:
            idn = sendToUSBTMC('/dev/'+str(device)[-9:-2], '*IDN?')
            devPresent=False
            for line in lines:
                if str(device)[-9:-2] not in line:
                    f.write(line)
                elif idn+'::'+str(device)[-9:-2] == line:
                    f.write(line)
                    devPresent=True
                    
            if devPresent==False:
                print(idn)
                f.write(str(device)[-9:-2]+'::'+idn+'\n')
                
                
    elif action=='remove':
        with open('./devList', 'w') as f:
            for line in lines:
                if str(device)[-9:-2] not in line:
                    f.write(line)
        
# monitoring happens here
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usbmisc')
for action, device in monitor:
    print('{0}: {1}'.format(action, device))
    devListF(action, device)

