import sounddevice as sd
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

# print(sd.query_devices())

# print(sd.check_input_settings(samplerate=44100))
# print(sd.check_output_settings(samplerate=44100))

duration = 1  # seconds
fs = 44100

def piano_note(freq, t):
    return (-1/4) * np.sin(2 * np.pi * freq * t) + (1/4) * np.sin(np.pi * freq * t) + ((3**0.5/2)) * np.cos(np.pi * freq * t)

# def callback(indata, outdata, frames, time, status):
#     if status:
#         print(status)
#     outdata[:] = indata

# with sd.Stream(samplerate=44100, channels=1, callback=callback):    # NEED TO SPEC SAMPLERATE AND CHANNELS == 1
#     sd.sleep(int(duration * 1000))

myrecording = sd.rec(int(duration * fs), channels=1, samplerate=44100)
sd.wait()

np.savetxt("output.txt", myrecording)
t = np.arange(fs * duration) / fs
# samples = piano_note(440, t) # + piano_note(220, t) + piano_note(880, t)

myrecording_f = fft(myrecording)
tf = fftfreq(44100, 1.0/44100.0)[:44100//2]

plt.plot(tf, 2.0/44100 * np.abs(myrecording_f[0:44100//2]))
plt.grid()
plt.show()
