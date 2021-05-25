import os
import time

class USBTMC:
    def __init__(self, device="/dev/usbtmc0"):
            self.f = os.open(device, os.O_RDWR)

    def __del__(self):
        os.close(self.f)

    def write(self, cmd):
        cmdb=bytes(cmd, encoding='UTF-8')
        os.write(self.f, cmdb)
        time.sleep(0.01)

    def read(self):
        outputb = os.read(self.f, 4096)
        return str(outputb,'UTF-8').strip()
       

    def getData(self):
        # setup oscilliscope for reading maximum numbneer of points in ASCI
        self.write('STOP')
        self.write('WAV:POIN:MODE RAW')
        numReads=int(self.ask('WAV:POIN?'))
        self.write('WAV:FORM ASC')
        self.write('WAV:DATA?')

        # init variables for loop allocation
        output=[]
        pointsRead=0 # offset value
        firstReadIter=1
        while pointsRead<numReads: 
            buffers=[] # required by preadv function
            # the real reading happens after in os.read thus ouputv is uneeded 
            outputv=os.preadv(self.f, buffers, pointsRead, 0) 
            if firstReadIter==1:
                time.sleep(0.01)
                
            # real reading happens here
            block = str(os.read(self.f, numReads),'UTF-8').strip()

            # remove header if present
            if firstReadIter==1:
                if block[0] =='#':
                    endOfHeader = block.find(' ')
                    block = block[endOfHeader:]
                firstReadIter=0

            # disect block and append points to the final output variable
            for pointS in block.replace(' ','').split(','):
                if pointS!= '':
                    output.append(float(pointS))


            if type(output)!=None:
                pointsRead=(len(output)+1)
        return str(output)
    
    def ask(self, cmd):      
        if 'iwav:data?' == cmd.lower():
            return self.getData()
        else:
            self.write(cmd)
            return self.read()
