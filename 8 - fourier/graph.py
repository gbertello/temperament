#!/usr/bin/env python3

import numpy as np
import soundfile as sf
from matplotlib.pyplot import *
from numpy.fft import *

y, rate = sf.read('piano.wav')
y = y.reshape(y.size,)
x = np.arange(y.size)/rate

yf = np.absolute(fft(y))
xf = np.arange(yf.size)*1.0/yf.size*rate

yf = yf[:int(yf.size/2)]
xf = xf[:int(xf.size/2)]

fig, ax = subplots()

vlines(xf, [0], yf, 'r')
xlabel('f (Hz)')
ylabel('A')
grid()
axis([xf[0], 4000, 0, np.amax(yf)*1.1])

show()
input()
