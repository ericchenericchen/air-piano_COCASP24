import numpy as np
import sounddevice as sd
from scipy.fft import fft, fftfreq
import time


samples = np.loadtxt("output.txt") # this appears correct
# duration = 3  # seconds

# def callback(indata, outdata, frames, time, status):
#     if status:
#         print(status)
#     outdata[:] = samples

# with sd.Stream(channels=1, callback=callback, samplerate=44100):
#     sd.sleep(int(duration * 1000))

start = time.perf_counter()
sd.play(samples, samplerate = 44100//1)
sd.wait()
print(time.perf_counter() - start)

yf = np.abs(fft(samples.squeeze()))
xf = fftfreq(len(samples), 1/44100)

# peaks = xf[np.argsort(np.abs(yf))[-20:]]
# print(np.sort(peaks))

mag = np.abs(yf[:44100//2])
freqs = xf[:44100//2]

from scipy.signal import find_peaks
peaks, props = find_peaks(mag, height=np.max(mag)*0.1)

print(freqs[peaks])
