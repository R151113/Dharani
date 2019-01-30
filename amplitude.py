import matplotlib.pyplot as plot
import numpy as np
t=np.arange(0,100,0.01)
f1=2
fs=40
x1=50*np.sin((2*np.pi*f1*t)/fs+180)
plot.subplot(3,1,1)
plot.plot(t,x1)
plot.title('sin wave-1')
plot.xlabel('time')
plot.ylabel('amp')
x2=10*np.sin((2*np.pi*t*f1)/fs)
plot.subplot(3,1,2)
plot.plot(t,x2)
plot.title('sin wave-2')
plot.show()

