# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,10)

y = np.sin(x)

plt.plot(x,y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Chart")

plt.show()

## scatter

A = pd.read_csv('data_2d.csv').as_matrix()

x = A[:,0]
y = A[:,1]

plt.scatter(x,y)


## histogram

plt.hist(x)
plt.show()
