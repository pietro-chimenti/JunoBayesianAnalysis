""" This code is am example of a complete bayesian analysis.
    Data are taken from table 15.5 of Dekking, et.al, "A Modern Introduction to
    Probability and Statistics" """

import numpy as np
import matplotlib.pyplot as plt

print("Bayesian model of Density and Hardness of Australian Timber")

Data = np.array([ 
   [24.7,484],
   [24.8,427],
   [27.3,413],
   [28.4,517],
   [28.4,549],
   [29.0,648],
   [30.3,587],
   [32.7,704],
   [35.6,979],
   [38.5,914],
   [38.8,1070],
   [39.3,1020],
   [39.4,1210],
   [39.9,989],
   [40.3,1160],
   [40.6,1010],
   [40.7,1100],
   [40.7,1130],
   [42.9,1270],
   [45.8,1180],
   [46.9,1400],
   [48.2,1760],
   [51.5,1710],
   [51.5,2010],
   [53.4,1880],
   [56.0,1980],
   [56.5,1820],
   [57.3,2020],
   [57.6,1980],
   [59.2,2310],
   [59.8,1940],
   [66.0,3260],
   [67.4,2700],
   [68.8,2890],
   [69.1,2740],
   [69.1,3140]])
print("Data: ", Data)

plt.scatter(Data[:,0],Data[:,1])
plt.show()


