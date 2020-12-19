#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile

rate = 44100
length = 5

t = np.linspace(0, length, rate * length)
y = 0.5*np.sin(float(440) * 2 * np.pi * t)
wavfile.write('La4.wav', rate, y)

y = 0.5*np.sin(float(440 * 5/4) * 2 * np.pi * t)
wavfile.write('Do#5.wav', rate, y)

y = np.sin(float(440) * 2 * np.pi * t)
y += np.sin(float(440 * 5/4) * 2 * np.pi * t)
y = y/np.amax(y)

wavfile.write('tierce.wav', rate, y)

y = 0.5*np.sin(float(440 * 5/3) * 2 * np.pi * t)
wavfile.write('Fa#5.wav', rate, y)

y = np.sin(float(440) * 2 * np.pi * t)
y += np.sin(float(440 * 5/3) * 2 * np.pi * t)
y = y/np.amax(y)

wavfile.write('sixte.wav', rate, y)


