#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile

rate = 44100
length = 1

freq = [1, 2**(2/12), 2**(4/12), 2**(5/12), 2**(7/12), 2**(9/12), 2**(11/12), 2**(12/12)]

signal = []

for f in freq:
    t = np.linspace(0, length, rate * length)
    y = 0.5*np.sin(float(440 * f) * 2 * np.pi * t)
    signal = np.concatenate((signal, y))

wavfile.write('gamme.wav', rate, signal)

length = 5
t = np.linspace(0, length, rate * length)
y = np.sin(float(440) * 2 * np.pi * t)
y += np.sin(float(440 * 2**(5/12)) * 2 * np.pi * t)
y = y/np.amax(y)

wavfile.write('quarte juste.wav', rate, y)

y = np.sin(float(440) * 2 * np.pi * t)
y += np.sin(float(440 * 2**(7/12)) * 2 * np.pi * t)
y = y/np.amax(y)

wavfile.write('quinte juste.wav', rate, y)