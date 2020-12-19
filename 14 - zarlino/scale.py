#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile

rate = 44100
length = 1

freq = [1, 9/8, 5/4, 4/3, 3/2, 5/3, 15/8, 2]

signal = []

for f in freq:
    t = np.linspace(0, length, rate * length)
    y = np.sin(float(440 * f) * 2 * np.pi * t)
    signal = np.concatenate((signal, y))

wavfile.write('gamme.wav', rate, signal)