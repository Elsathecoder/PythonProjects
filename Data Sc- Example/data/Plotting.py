import matplotlib.pyplot as plot
import numpy as num
import Diseaseproject as dp

ypoints = num.array([dp.countries])
xpoints = num.array([dp.people_on_art])

plot.plot(ypoints)
plot.plot(xpoints)
plot.show()