#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile

rate = 44100
length = 1

freq = [1, 3**2 / 2**3, 3**4 / 2**6, 3**11 / 2**17, 3 / 2, 3**3 / 2**4, 3**5 / 2**7, 3**12 / 2**18]

signal = []

for f in freq:
    t = np.linspace(0, length, rate * length)
    y = np.sin(float(440 * f) * 2 * np.pi * t)
    signal = np.concatenate((signal, y))

wavfile.write('gamme.wav', rate, signal)