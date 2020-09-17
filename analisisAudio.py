import sys
sys.path.insert(1, "dps-modulo")

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave

import thinkplot

waveTelefono = read_wave("telefono.wav")
waveTelefono.plot()
decorate(xlabel="tiempo S")

thinkplot.show()

#espectro = waveTelefono.make_spectrum()
#espectro.plot()
#decorate(xlabel="frecuencia Hz")
#thinkplot.show()

waveDigito1 = waveTelefono.segment(start=0, duration=0.5)
#waveDigito1.plot()
#decorate(xlabel= "tiempo S")
#thinkplot.show()

#TELEFONO 224532

espectroDigito1 = waveDigito1.make_spectrum()
espectroDigito1.plot()
decorate(xlabel = "frecuencia Hz")
thinkplot.show()

waveDigito2 = waveTelefono.segment(start=0.5, duration=0.5)
espectroDigito2 = waveDigito2.make_spectrum()
espectroDigito2.plot()
decorate(xlabel = "frecuencia Hz")
thinkplot.show()

waveDigito3 = waveTelefono.segment(start=1.0, duration=0.5)
espectroDigito3 = waveDigito3.make_spectrum()
espectroDigito3.plot()
decorate(xlabel = "frecuencia Hz")
thinkplot.show()

waveDigito4 = waveTelefono.segment(start=1.5, duration=0.5)
espectroDigito4 = waveDigito4.make_spectrum()
espectroDigito4.plot()
decorate(xlabel = "frecuencia Hz")
thinkplot.show()

waveDigito5 = waveTelefono.segment(start=2.0, duration=0.5)
espectroDigito5 = waveDigito5.make_spectrum()
espectroDigito5.plot()
decorate(xlabel = "frecuencia Hz")
thinkplot.show()

waveDigito6 = waveTelefono.segment(start=2.5, duration=0.5)
espectroDigito6 = waveDigito6.make_spectrum()
espectroDigito6.plot()
decorate(xlabel = "frecuencia Hz")
thinkplot.show()