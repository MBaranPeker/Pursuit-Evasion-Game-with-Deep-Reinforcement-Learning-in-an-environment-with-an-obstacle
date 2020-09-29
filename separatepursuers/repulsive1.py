import numpy as np
from collections import defaultdict

import math
evaderx = 12
evadery = 8

pursuitx = 10
pursuity = 10




p0 = 25

Eta = 1000

Ec_distance_sqr = (evaderx-pursuitx + 0.01)**2 + (evadery-pursuity + 0.01)**2
Ec_distance = math.sqrt((evaderx-pursuitx + 0.01)**2 + (evadery-pursuity + 0.01)**2)

X_distance_EP = (evaderx- pursuitx )
Y_distance_EP = (evadery- pursuity )

X_direction_EP = X_distance_EP/Ec_distance
Y_direction_EP = Y_distance_EP/Ec_distance


ni = np.array([[Y_direction_EP], [X_direction_EP]])



Frep_P = Eta*((1/Ec_distance) - (1/p0))*(1/(Ec_distance_sqr))*ni

Frep_P[1]


#print(Ec_distance)
#print(X_distance_EP)
#print(Y_distance_EP)
#print(X_direction_EP)
#print(Y_direction_EP)
#print(ni)
#print(ni1)
#print(Ec_distance_sqr)

print(Frep_P[0])
#print(Frep_P1)
#print(n)































