#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile

rate = 44100
length = 5

t = np.linspace(0, length, rate * length)
y = np.sin(float(440) * 2 * np.pi * t)

wavfile.write('La4.wav', rate, y)
