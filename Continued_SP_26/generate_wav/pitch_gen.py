import numpy as np
import sounddevice as sd
from scipy import signal
from pynput import keyboard
import time

phase = 0.0
freqs = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
sr = 44100
# init_time = start = time.perf_counter()

notes = {
    'A1':55.0,
    'A#1':58.27047018976124,
    'B1':61.735412657015516,
    'C1':65.40639132514967,
    'C#1':69.29565774421803,
    'D1':73.41619197935191,
    'D#1':77.78174593052024,
    'E1':82.40688922821751,
    'F1':87.307057858251,
    'F#1':92.49860567790863,
    'G1':97.99885899543736,
    'G#1':103.82617439498632,
    'A2':110.00000000000004,
    'A#2':116.54094037952252,
    'B2':123.47082531403107,
    'C2':130.81278265029937,
    'C#2':138.5913154884361,
    'D2':146.83238395870384,
    'D#2':155.56349186104052,
    'E2':164.81377845643505,
    'F2':174.61411571650203,
    'F#2':184.99721135581729,
    'G2':195.99771799087475,
    'G#2':207.65234878997268,
    'A3':220.0000000000001,
    'A#3':233.08188075904508,
    'B3':246.9416506280622,
    'C3':261.6255653005988,
    'C#3':277.1826309768723,
    'D3':293.6647679174078,
    'D#3':311.1269837220812,
    'E3':329.62755691287026,
    'F3':349.2282314330042,
    'F#3':369.9944227116348,
    'G3':391.9954359817497,
    'G#3':415.3046975799456,
    'A4':440.0000000000005,
    'A#4':466.1637615180905,
    'B4':493.88330125612475,
    'C4':523.2511306011979,
    'C#4':554.365261953745,
    'D4':587.3295358348159,
    'D#4':622.2539674441628,
    'E4':659.2551138257409,
    'F4':698.4564628660089,
    'F#4':739.98884542327,
    'G4':783.9908719634999,
    'G#4':830.6093951598917,
    'A5':880.0000000000016,
    'A#5':932.3275230361816,
    'B5':987.7666025122501,
    'C5':1046.5022612023965,
    'C#5':1108.7305239074906,
    'D5':1174.6590716696326,
    'D#5':1244.5079348883262,
    'E5':1318.5102276514824,
    'F5':1396.9129257320185,
    'F#5':1479.9776908465408,
    'G5':1567.9817439270007,
    'G#5':1661.2187903197844,
    'A6':1760.000000000004,
    'A#6':1864.655046072364,
    'B6':1975.533205024501,
    'C6':2093.004522404794,
    'C#6':2217.461047814982,
    'D6':2349.318143339266,
    'D#6':2489.0158697766533,
    'E6':2637.0204553029657,
    'F6':2793.825851464038,
    'F#6':2959.9553816930825,
    'G6':3135.9634878540023,
    'G#6':3322.4375806395697,
    'A7':3520.000000000009,
    'A#7':3729.310092144729,
    'B7':3951.0664100490035,
    'C7':4186.00904480959,
    'C#7':4434.922095629966,
    'D7':4698.636286678534,
    'D#7':4978.031739553308,
    'E7':5274.040910605934,
    'F7':5587.6517029280785,
    'F#7':5919.910763386168,
    'G7':6271.926975708007,
    'G#7':6644.875161279142,
    'A8':7040.000000000021,
    'A#8':7458.620184289462,
    'B8':7902.132820098011,
    'C8':8372.018089619183,
    'C#8':8869.844191259936,
    'D8':9397.272573357073,
    'D#8':9956.063479106622,
    'E8':10548.081821211874,
    'F8':11175.303405856162,
    'F#8':11839.821526772343,
    'G8':12543.853951416022,
    'G#8':13289.750322558291,
}

scale_vals = [notes['A4'], notes['B4'], notes['C#4'], notes['D4'], notes['E4'], notes['F#4'], notes['G#4'], notes['A5'], notes['B5'], notes['C#5']]

def on_press(key):
    keycode_str = key.char

    if keycode_str < '0' or keycode_str > '9':
        return
    else:
        cast_finger = (int(keycode_str) - 1) % 10
        freqs[cast_finger] = scale_vals[cast_finger]

def on_release(key):
    keycode_str = key.char

    if keycode_str < '0' or keycode_str > '9':
        return
    else:
        cast_finger = (int(keycode_str) - 1) % 10
        freqs[cast_finger] = 0

def generate_buffer(frames, instrument):
    global phase
    dt = (np.arange(frames) + phase) / sr
    buf = 0

    for freq in freqs:
        x = freq * dt
        buf += instrument_waveform(instrument, x)

    phase += frames
    return buf

def instrument_waveform(instrument, x):
    if instrument == 'piano':
        return piano_waveform(x)
    elif instrument == 'sawtooth':  
        return sawtooth_waveform(x)
    elif instrument == 'square':
        return square_waveform(x)
    else: # default to sine wave
        return np.sin(2 * np.pi * x)

def piano_waveform(x, volume = 0.05):
    # global start
    # global init_time

    # can we make a chord?
    base_x = x
    # mid_x = x * (2 ** (1/3))
    # high_x = mid_x * (2 ** (1/4))

    base_note = (-1/4) * np.sin(2 * np.pi * base_x) + (1/4) * np.sin(np.pi * base_x) + ((3**0.5/2)) * np.cos(np.pi * base_x) # appx from piano note waveform analysis on forum
    # mid_note = (-1/4) * np.sin(2 * np.pi * mid_x) + (1/4) * np.sin(np.pi * mid_x) + ((3**0.5/2)) * np.cos(np.pi * mid_x) # appx from piano note waveform analysis on forum
    # high_note = (-1/4) * np.sin(2 * np.pi * high_x) + (1/4) * np.sin(np.pi * high_x) + ((3**0.5/2)) * np.cos(np.pi * high_x) # appx from piano note waveform analysis on forum

    # # looks like basically 0 overhead! YIPPEE    
    # if start == init_time:
    #     start = time.perf_counter()
    #     init_time = start
    #     print(start - init_time)
    
    return (volume) * (base_note) # + (mid_note + high_note)

def strings_waveform(x, volume = 0.05):
    # y = 0

    # for k in [1,2,4,5,6,7,8]:
    #     y += A[k] * np.sin(2 * np.pi * k * x * t + φ[k])

    return 

def sawtooth_waveform(x, volume = 0.01):
    return volume * signal.sawtooth(2 * np.pi * x)

def square_waveform(x, volume = 0.01):
    return volume * signal.square(2 * np.pi * x)

def callback(outdata, frames, time_info, status):
    if status:
        print(status)
    outdata[:, 0] = generate_buffer(frames, 'piano').astype(np.float32)

if __name__ == '__main__':
    stream = sd.OutputStream(
        samplerate=sr,
        channels=1,
        callback=callback,
        blocksize=256  # good default
    )

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    stream.start()
    input(f"press enter to stop")
    stream.stop()

    # # generate all notes
    # notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    # for i in range(1, 9):
    #     for note in notes:
    #         key = note + str(i)
    #         value = str(freq)
    #         freq *= (2**(1/12))
    #         print("\'" + key + "\':" + value + ',')
    
    # # play all piano notes
    # for k,v in notes.items():
    #     # print(f"{k}, {v}")
    #     freq = v
    #     stream.start()
    #     input(f"Playing {k}... press enter to half step")
    #     stream.stop()

    # # play A major scale
    # cnt = 0
    # while True:
    #     stream.start()
    #     input("Press Enter to go up the scale...")
    #     stream.stop()
    #     cnt += 1

    #     # A to B:    2, B to C#:   2, C# to D:   1, D to E:    2, E to F#:   2, F# to G#:  2, G# to A:   1
    #     if cnt == 3 or cnt == 7:
    #         freqs[0] *= 2 ** (1/12)
    #     elif cnt != 8:
    #         freqs[0] *= 2 ** (1/6)
    #     else:
    #         cnt = 0
    #         freqs[0] = 440
            
    stream.close()
