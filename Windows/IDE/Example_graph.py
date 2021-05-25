import matplotlib.pyplot as plt
import numpy as np
from TMC import TMC

myScope = TMC('usbtmc1')
dataS = myScope.send('iwav:data?')
data = list(map(float, dataS[1:-1].replace(' ', '').split(',')))


timeEnd = float(myScope.send('TIM:RANG?').strip())
time=np.linspace(0, timeEnd*1000, len(data)).astype(float)
myScope.close()

plt.plot(time, data)
plt.title('Channel 1')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.show()















