import numpy as np
from collections import defaultdict
import math
import random

SIZE = 84
p0 = 10
p0_pursuer = 15
Eta = 1000

class Repulsive:


	def __init__(self, Evader_x, Evader_y, Pursuer_x , Pursuer_y , Pursuer1_x , Pursuer1_y , Pursuer2_x , Pursuer2_y , Pursuer3_x , Pursuer3_y, P_Invisible, P1_Invisible, P2_Invisible, P3_Invisible):


		self.Evader_x = Evader_x
		self.Evader_y = Evader_y

		self.Pursuer_x  = Pursuer_x 
		self.Pursuer_y  = Pursuer_y 

		self.Pursuer1_x  = Pursuer1_x 
		self.Pursuer1_y  = Pursuer1_y 

		self.Pursuer2_x  = Pursuer2_x 
		self.Pursuer2_y  = Pursuer2_y 

		self.Pursuer3_x  = Pursuer3_x 
		self.Pursuer3_y  = Pursuer3_y


		self.P_Invisible = P_Invisible
		self.P1_Invisible = P1_Invisible
		self.P2_Invisible = P2_Invisible
		self.P3_Invisible = P3_Invisible

		self.F_Total = 0

		self.Calculation()



	def Calculation(self):

## P
		if (self.P_Invisible == True) and (self.P1_Invisible == True) and (self.P2_Invisible == True) and (self.P3_Invisible == True):

			P_Frep = np.array([[0], [0]])

		else :

			P_X_distance = (self.Evader_x- self.Pursuer_x + 0.01)
			P_Y_distance = (self.Evader_y- self.Pursuer_y + 0.01)

			P_Ec_distance_sqr = P_X_distance**2 + P_Y_distance**2
			P_Ec_distance = math.sqrt((P_X_distance**2 + P_Y_distance**2))

			P_X_direction = (self.Evader_x- self.Pursuer_x)/P_Ec_distance
			P_Y_direction = (self.Evader_y- self.Pursuer_y)/P_Ec_distance
			P_ni = np.array([[P_Y_direction], [P_X_direction]])


			P_Frep = Eta*(((1/P_Ec_distance) - (1/p0_pursuer))*(1/(P_Ec_distance_sqr)))*P_ni





## WEST Repulsive Force
		if ((self.Pursuer_y - 0) < p0) and (self.Pursuer_y > 0):

			West_distance_sqr =(self.Pursuer_y - 0)**2
			West_Y_distance = (self.Pursuer_y- 0)

			West_ni = np.array([[1], [0]])

			West_Frep = Eta*(((1/West_Y_distance) - (1/p0))*(1/(West_distance_sqr)))

			West_Frep_Vector = Eta*(((1/West_Y_distance) - (1/p0))*(1/(West_distance_sqr)))*West_ni
		else :
			West_Frep_Vector = np.array([[0], [0]])

## EAST Repulsive Force
		if (((SIZE -1) - self.Pursuer_y) < p0) and (self.Pursuer_y < (SIZE -1)):

			East_distance_sqr =((SIZE -1) - self.Pursuer_y)**2
			East_Y_distance = ((SIZE -1) - self.Pursuer_y)

			East_ni = np.array([[-1], [0]])

			East_Frep = Eta*(((1/East_Y_distance) - (1/p0))*(1/(East_distance_sqr)))

			East_Frep_Vector = Eta*(((1/East_Y_distance) - (1/p0))*(1/(East_distance_sqr)))*East_ni
		else :
			East_Frep_Vector = np.array([[0], [0]])

## NORTH Repulsive Force
		if ((self.Pursuer_x - 0) < p0) and (self.Pursuer_x > 0):

			North_distance_sqr =(self.Pursuer_x - 0)**2
			North_X_distance = (self.Pursuer_x- 0)

			North_ni = np.array([[0], [1]])

			North_Frep = Eta*(((1/North_X_distance) - (1/p0))*(1/(North_distance_sqr)))

			North_Frep_Vector = Eta*(((1/North_X_distance) - (1/p0))*(1/(North_distance_sqr)))*North_ni
		else :
			North_Frep_Vector = np.array([[0], [0]])


## SOUTH Repulsive Force

		if (((SIZE -1) - self.Pursuer_x) < p0) and (self.Pursuer_x < (SIZE -1)):

			South_distance_sqr =((SIZE -1) - self.Pursuer_x)**2
			South_X_distance = ((SIZE -1) - self.Pursuer_x)

			South_ni = np.array([[0], [-1]])

			South_Frep = Eta*(((1/South_X_distance) - (1/p0))*(1/(South_distance_sqr)))

			South_Frep_Vector = Eta*(((1/South_X_distance) - (1/p0))*(1/(South_distance_sqr)))*South_ni
		else :
			South_Frep_Vector = np.array([[0], [0]])



## Obs 1

		if ((15 <= self.Pursuer_x <= 39) and (0 <= self.Pursuer_y <= 25) and ((25 - self.Pursuer_y) < p0)):

			Obs1_distance_sqr =(25.01 - self.Pursuer_y)**2
			Obs1_distance = (25.01 - self.Pursuer_y)

			Obs1_ni = np.array([[-1], [0]])

			Obs1_Frep = Eta*(((1/Obs1_distance) - (1/p0))*(1/(Obs1_distance_sqr)))

			Obs1_Frep_Vector = Eta*(((1/Obs1_distance) - (1/p0))*(1/(Obs1_distance_sqr)))*Obs1_ni
		else :
			Obs1_Frep_Vector = np.array([[0], [0]])


## Obs 2

		if ((15 <= self.Pursuer_x <= 30) and (35 <= self.Pursuer_y <= 49) and ((49 - self.Pursuer_y) < p0)):

			Obs2_distance_sqr =(49.01 - self.Pursuer_y)**2
			Obs2_distance = (49.01 - self.Pursuer_y)

			Obs2_ni = np.array([[-1], [0]])

			Obs2_Frep = Eta*(((1/Obs2_distance) - (1/p0))*(1/(Obs2_distance_sqr)))

			Obs2_Frep_Vector = Eta*(((1/Obs2_distance) - (1/p0))*(1/(Obs2_distance_sqr)))*Obs2_ni
		else :
			Obs2_Frep_Vector = np.array([[0], [0]])

## Obs 3

		if ((15 <= self.Pursuer_x <= 30) and (35 <= self.Pursuer_y <= 49) and ((self.Pursuer_y - 35) < p0)):

			Obs3_distance_sqr =(self.Pursuer_y - 34.99)**2
			Obs3_distance = (self.Pursuer_y - 34.99)

			Obs3_ni = np.array([[1], [0]])

			Obs3_Frep = Eta*(((1/Obs3_distance) - (1/p0))*(1/(Obs3_distance_sqr)))

			Obs3_Frep_Vector = Eta*(((1/Obs3_distance) - (1/p0))*(1/(Obs3_distance_sqr)))*Obs3_ni
		else :
			Obs3_Frep_Vector = np.array([[0], [0]])
## Obs 4

		if ((15 <= self.Pursuer_x <= 39) and (59 <= self.Pursuer_y <= SIZE) and ((self.Pursuer_y - 59) < p0)):

			Obs4_distance_sqr =(self.Pursuer_y - 58.99)**2
			Obs4_distance = (self.Pursuer_y - 58.99)

			Obs4_ni = np.array([[1], [0]])

			Obs4_Frep = Eta*(((1/Obs4_distance) - (1/p0))*(1/(Obs4_distance_sqr)))

			Obs4_Frep_Vector = Eta*(((1/Obs4_distance) - (1/p0))*(1/(Obs4_distance_sqr)))*Obs4_ni
		else :
			Obs4_Frep_Vector = np.array([[0], [0]])

## Obs 5

		if ((40 <= self.Pursuer_x <= SIZE) and ( 26 <= self.Pursuer_y <= 58) and ((self.Pursuer_x - 40) < p0)):

			Obs5_distance_sqr =(self.Pursuer_x - 39.99)**2
			Obs5_distance = (self.Pursuer_x - 39.99)

			Obs5_ni = np.array([[0], [1]])

			Obs5_Frep = Eta*(((1/Obs5_distance) - (1/p0))*(1/(Obs5_distance_sqr)))

			Obs5_Frep_Vector = Eta*(((1/Obs5_distance) - (1/p0))*(1/(Obs5_distance_sqr)))*Obs5_ni
		else :
			Obs5_Frep_Vector = np.array([[0], [0]])

## Obs 6

		if ((((0 <= self.Pursuer_x <= 14) and ( 26 <= self.Pursuer_y <= 34)) or ((0 <= self.Pursuer_x <= 14) and ( 50 <= self.Pursuer_y <= 58))) and ((14 - self.Pursuer_x) < p0)):

			Obs6_distance_sqr =(14.01 - self.Pursuer_x)**2
			Obs6_distance = (14.01 - self.Pursuer_x)

			Obs6_ni = np.array([[0], [-1]])

			Obs6_Frep = Eta*(((1/Obs6_distance) - (1/p0))*(1/(Obs6_distance_sqr)))

			Obs6_Frep_Vector = Eta*(((1/Obs6_distance) - (1/p0))*(1/(Obs6_distance_sqr)))*Obs6_ni
		else :
			Obs6_Frep_Vector = np.array([[0], [0]])

## Obs 7

		if (((0 <= self.Pursuer_x <= 30) and ( 35 <= self.Pursuer_y <= 49)) and ((30 - self.Pursuer_x) < p0)):

			Obs7_distance_sqr =(30.01 - self.Pursuer_x)**2
			Obs7_distance = (30.01 - self.Pursuer_x)

			Obs7_ni = np.array([[0], [-1]])

			Obs7_Frep = Eta*(((1/Obs7_distance) - (1/p0))*(1/(Obs7_distance_sqr)))

			Obs7_Frep_Vector = Eta*(((1/Obs7_distance) - (1/p0))*(1/(Obs7_distance_sqr)))*Obs7_ni
		else :
			Obs7_Frep_Vector = np.array([[0], [0]])




		F_Obs_Total_Vector = West_Frep_Vector + South_Frep_Vector + East_Frep_Vector + North_Frep_Vector + Obs1_Frep_Vector + Obs2_Frep_Vector + Obs3_Frep_Vector + Obs4_Frep_Vector + Obs5_Frep_Vector + Obs6_Frep_Vector + Obs7_Frep_Vector

#Pursuers

#		print (P_Frep)
#		print (P_ni)
#		print (self.Pursuer_y)
#		print (self.Evader_y)
#		print (self.Pursuer_x)
#		print (self.Evader_x)

		if abs(P_Frep[0]) == abs(P_Frep[1]) :
			self.Best_Action = random.randint(1, 2)

		elif abs(P_Frep[0]) < abs(P_Frep[1]) :
			if P_Frep[0] < 0 :
				self.Best_Action = 2
			else:
				self.Best_Action = 3

		elif abs(P_Frep[0]) > abs(P_Frep[1]) :
			if P_Frep[1] < 0 :
				self.Best_Action = 4
			else:
				self.Best_Action = 1

#obtacles

		if abs(F_Obs_Total_Vector[0]) == abs(F_Obs_Total_Vector[1]) :
			self.Best_obs_Action = 0

		elif abs(F_Obs_Total_Vector[0]) > abs(F_Obs_Total_Vector[1]) :
			if F_Obs_Total_Vector[0] > 0 :
				self.Best_obs_Action = 2
			else:
				self.Best_obs_Action = 3

		elif abs(F_Obs_Total_Vector[0]) < abs(F_Obs_Total_Vector[1]) :
			if F_Obs_Total_Vector[1] > 0 :
				self.Best_obs_Action = 4
			else:
				self.Best_obs_Action = 1


		

		self.F_Obs_Total = (F_Obs_Total_Vector[0])**2 + (F_Obs_Total_Vector[1])**2

		

































