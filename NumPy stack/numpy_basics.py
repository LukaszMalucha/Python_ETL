# -*- coding: utf-8 -*-

import numpy as np

a = np.array([1,2])

b = np.array([2,1])


## generating array
Z = np.zeros(10)
O = np.ones((10,10))
R = np.random.random((10,10))
G = np.random.randn(10,10)

G.mean()
G.var(0.83)

############################################################## MULTIPLICATION ################################################
## for loop multiplication

dot = 0

for e, f in zip(a, b):
    dot += e*f
    
## vector multiplication  - x30  times faster

np.sum(a*b)
(a*b).sum()
   

## better

np.dot(a,b)
a.dot(b)


############################################################## ANGLE BETWEEN #################################################

amag = np.sqrt((a*a).sum())

## better

amag = np.linalg.norm(a)


cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))

angle = np.arccos(cosangle)


################################################################ TASK ######################################################

## admission fee - $1.50 child, $4.00 adult.

## 2200 ppl entered and $5050 was collected

## How many children/adults

A = np.array([[1,1], [1.5,4]])
b = np.array([2200, 5050])

np.linalg.solve(A,b)

## 1500 children & 700 adults







