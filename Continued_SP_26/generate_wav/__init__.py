import numpy as np
import scipy as sp
import math
import itertools
import time

class WaveGenerator:
    def __init__(self, freq=440, phase=0, sample_rate=44100, shape='sine'):
        self.freq = freq    # controls pitch
        self.shape = shape  # controls tone (square wave, sine wave, ...)
        self.phase = phase              # controls offset (maybe matters for layering)
        self.sample_rate = sample_rate  # controls sound fidelity

    # from synth python blog
    #
    # based on my understanding, this only adjusts the step, so we need to presume
    # iteration rate that given obj = get_sin_oscillator, next(obj) is called at
    # rate of sample_rate
    def get_sin_oscillator(self):
        increment = (2 * math.pi * self.freq)/ self.sample_rate
        return (math.sin(self.phase + v) for v in itertools.count(start=0, step=increment))
    
if __name__ == "__main__":
    w = WaveGenerator()
    temp = w.get_sin_oscillator()
    sample_tick = 1 / 44100
    start = time.perf_counter()

    for _ in range(44100):
        print(next(temp))
        # next(temp)
        time.sleep(sample_tick)

    print(time.perf_counter() - start)
