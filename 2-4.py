from thinkdsp import TriangleSignal
from thinkdsp import decorate
from winsound import PlaySound
import matplotlib.pyplot as plt
import time
from thinkdsp import SquareSignal
from thinkdsp import read_wave

triangle = TriangleSignal().make_wave(duration=0.01)
triangle.plot()
decorate(xlabel='Time (s)')
plt.show()


spectrum = triangle.make_spectrum()
spectrum.hs[0]

spectrum.hs[0] = 100
triangle.plot(color='gray')
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')
plt.show()