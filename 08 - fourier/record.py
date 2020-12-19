#!/usr/bin/env python3

import sounddevice as sd
import soundfile as sf

rate = 192000

start = 1
duration = 5

y = sd.rec(int((start+duration) * rate), samplerate=rate, channels=1)
sd.wait()

y = y[int(rate*start):int(rate*(start+duration))]

sf.write("piano.wav", y, rate)
