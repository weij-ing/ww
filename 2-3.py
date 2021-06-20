from thinkdsp import TriangleSignal
from thinkdsp import decorate
from winsound import PlaySound
import matplotlib.pyplot as plt
import time
from thinkdsp import SinSignal
from thinkdsp import SquareSignal
from thinkdsp import read_wave

square = SquareSignal(1500).make_wave(duration=0.5, framerate=10000)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

square.make_audio()


SinSignal(500).make_wave(duration=0.5, framerate=10000).make_audio()