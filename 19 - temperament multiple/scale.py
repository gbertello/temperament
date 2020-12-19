#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile

rate = 44100
length = 1

freq = [1, 2**(1/19), 2**(2/19), 2**(3/19), 2**(4/19), 2**(5/19), 2**(6/19), 2**(7/19), 2**(8/19), 2**(9/19), 2**(10/19), 2**(11/19), 2**(12/19), 2**(13/19), 2**(14/19), 2**(15/19), 2**(16/19), 2**(17/19), 2**(18/19), 2**(19/19)]

signal = []

for f in freq:
    t = np.linspace(0, length, rate * length)
    y = np.sin(float(440 * f) * 2 * np.pi * t)
    signal = np.concatenate((signal, y))

wavfile.write('gamme.wav', rate, signal)