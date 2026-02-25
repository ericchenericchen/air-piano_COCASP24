import pyglet
import pyautogui
import pathlib
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment

SLICE_SIZE = 0.15
# pyautogui.press('Any key combination')
def main():
    # audio = AudioSegment.from_mp3("./sample.mp3")

    # sample_count = audio.frame_count()
    # sample_rate = audio.frame_rate    

    # samples = audio.get_array_of_samples()
    # # it appears that the frame_count is not the same size as get_array_of_samples() output somehow in some cases.
    # # it doesn't work on the DTMF_audio.

    # # print(len(samples))
    # # print(sample_count)
    # period = 1/sample_rate                  # the period of each sample
    # duration = sample_count/sample_rate     # length of full audio in seconds
    # time = np.arange(0, duration, period)   # generate a array of time values from 0 to [duration] with step of [period]


    # slice_frame_size = int(SLICE_SIZE*sample_rate)   # get the number of elements expected for [SLICE_SIZE] seconds
    # start_index = int(0*sample_rate)        # get the starting index for the given [start_time]
    # end_index = start_index + slice_frame_size       # find the ending index for the slice

    # time_slice = time[start_index: end_index]        # take a slice from the time array for the given start and end index 
    # sample_slice = samples[start_index: end_index]   # take a slice from the samples array for the given start and end index

    # # Plot
    # plt.subplot(222)
    # # TODO: Plot the sample slice as a subplot (make sure to include labels)
    # plt.plot(time_slice, sample_slice)
    # plt.subplot(222).set_title("Tone Window")
    # plt.subplot(222).set_xlabel("Time")
    # plt.subplot(222).set_ylabel("Amplitude")
    
    counter = 0
    while(1):
        if counter == 0:
            pyautogui.press('a')
        elif counter == 1:
            pyautogui.press('a')
        counter = (counter + 1) % 2

    # effectA = pyglet.resource.media("yarg.aiff", streaming=False)
    # while(1):
    #     effectA.play()
    #     pyglet.clock.schedule_once(lambda dt: pyglet.app.exit(), effectA.duration)
    #     pyglet.app.run()

if __name__ == "__main__":
    main()