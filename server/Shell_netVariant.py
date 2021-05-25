import sys

from Driver_USBTMC import USBTMC

def sendToUSBTMC(devAddress, message):

    try:  
        dev = USBTMC(devAddress)

         # read and execute commands
        try:
            
            if message.find('?') >= 0:
                answer = dev.ask(message)
                return answer
            else:
                dev.write(message)
                return ''
        except EOFError:
            pass
    except: # keep connection alive and give the user another chance to connect to a valid device
        return 'can\'t find device '
