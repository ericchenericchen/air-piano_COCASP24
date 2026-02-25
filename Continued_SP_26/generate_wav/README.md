ATTENTION!

WE HAVE MADE A WORKING KEYBOARD PIANO!!
WWWWWWW

curr keybinds digits 0-9 (LH: 1-5; RH: 6-0)
curr notes mapping: A4 Major scale

Steps:
1. create .venv and install packages from requirements.txt 
2. python pitch_gen.py
3. go crazy

Design Philosophy:
- For audio engineering standpoint, multithreading is not the correct approach because there is only one audio/video driver (or limited num to my understanding)
- This is not an obstacle though because from a DFT perspective we can construct any chord/combination of notes very easily by just adding the waveforms
- Since audio is generated based on vibrations of a speaker at a specific sample rate, multiple notes together can just be simulated by calculating the change of
their waveform-sum over a small dt