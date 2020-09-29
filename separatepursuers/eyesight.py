import numpy as np
import time
import random
from tqdm import tqdm
import os
from PIL import Image
import cv2


class Eyesight:


	def __init__(self, Evader_x, Evader_y, Pursuer_x , Pursuer_y , Pursuer1_x , Pursuer1_y , Pursuer2_x , Pursuer2_y , Pursuer3_x , Pursuer3_y ):


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

		self.P_Unvisible = False
		self.P1_Unvisible = False
		self.P2_Unvisible = False
		self.P3_Unvisible = False

		self.invis_check()


	def invis_check(self):

## Evader Area


		if ((0 <= self.Evader_y < 26) and (0 <= self.Evader_x < 15)):
			E_Area = 1
		if ((0 <= self.Evader_y < 26) and (15 <= self.Evader_x < 40)):
			E_Area = 2
		if ((0 <= self.Evader_y < 26) and (40 <= self.Evader_x <= 84)):
			E_Area = 3
		if ((26 <= self.Evader_y < 59) and (40 <= self.Evader_x <= 84)):
			E_Area = 4
		if ((59 <= self.Evader_y <= 84) and (40 <= self.Evader_x <= 84)):
			E_Area = 5
		if ((59 <= self.Evader_y <= 84) and (15 <= self.Evader_x < 40)):
			E_Area = 6
		if ((59 <= self.Evader_y <= 84) and (0 <= self.Evader_x < 15)):
			E_Area = 7
		if ((50 <= self.Evader_y <= 58) and (0 <= self.Evader_x < 15)):
			E_Area = 8
		if ((34 < self.Evader_y < 50) and (0 <= self.Evader_x < 15)):
			E_Area = 9
		if ((34 < self.Evader_y < 50) and (15 <= self.Evader_x < 31)):
			E_Area = 10
		if ((26 <= self.Evader_y <= 34) and (0 <= self.Evader_x < 15)):
			E_Area = 11
		else:
			E_Area = 0

## P Area 

		if ((0 <= self.Pursuer_y  < 26) and (0 <= self.Pursuer_x  < 15)):
			P_Area = 1
		if ((0 <= self.Pursuer_y  < 26) and (15 <= self.Pursuer_x  < 40)):
			P_Area = 2
		if ((0 <= self.Pursuer_y  < 26) and (40 <= self.Pursuer_x  <= 84)):
			P_Area = 3
		if ((26 <= self.Pursuer_y  < 59) and (40 <= self.Pursuer_x  <= 84)):
			P_Area = 4
		if ((59 <= self.Pursuer_y  <= 84) and (40 <= self.Pursuer_x  <= 84)):
			P_Area = 5
		if ((59 <= self.Pursuer_y  <= 84) and (15 <= self.Pursuer_x  < 40)):
			P_Area = 6
		if ((59 <= self.Pursuer_y  <= 84) and (0 <= self.Pursuer_x  < 15)):
			P_Area = 7
		if ((50 <= self.Pursuer_y  <= 58) and (0 <= self.Pursuer_x  < 15)):
			P_Area = 8
		if ((34 < self.Pursuer_y  < 50) and (0 <= self.Pursuer_x  < 15)):
			P_Area = 9
		if ((34 < self.Pursuer_y  < 50) and (15 <= self.Pursuer_x  < 31)):
			P_Area = 10
		if ((26 <= self.Pursuer_y  <= 34) and (0 <= self.Pursuer_x  < 15)):
			P_Area = 11
		else:
			P_Area = 0

## P1 Area 

		if ((0 <= self.Pursuer1_y  < 26) and (0 <= self.Pursuer1_x  < 15)):
			P1_Area = 1
		if ((0 <= self.Pursuer1_y  < 26) and (15 <= self.Pursuer1_x  < 40)):
			P1_Area = 2
		if ((0 <= self.Pursuer1_y  < 26) and (40 <= self.Pursuer1_x  <= 84)):
			P1_Area = 3
		if ((26 <= self.Pursuer1_y  < 59) and (40 <= self.Pursuer1_x  <= 84)):
			P1_Area = 4
		if ((59 <= self.Pursuer1_y  <= 84) and (40 <= self.Pursuer1_x  <= 84)):
			P1_Area = 5
		if ((59 <= self.Pursuer1_y  <= 84) and (15 <= self.Pursuer1_x  < 40)):
			P1_Area = 6
		if ((59 <= self.Pursuer1_y  <= 84) and (0 <= self.Pursuer1_x  < 15)):
			P1_Area = 7
		if ((50 <= self.Pursuer1_y  <= 58) and (0 <= self.Pursuer1_x  < 15)):
			P1_Area = 8
		if ((34 < self.Pursuer1_y  < 50) and (0 <= self.Pursuer1_x  < 15)):
			P1_Area = 9
		if ((34 < self.Pursuer1_y  < 50) and (15 <= self.Pursuer1_x  < 31)):
			P1_Area = 10
		if ((26 <= self.Pursuer1_y  <= 34) and (0 <= self.Pursuer1_x  < 15)):
			P1_Area = 11
		else:
			P1_Area = 0


## P2 Area 

		if ((0 <= self.Pursuer2_y  < 26) and (0 <= self.Pursuer2_x  < 15)):
			P2_Area = 1
		if ((0 <= self.Pursuer2_y  < 26) and (15 <= self.Pursuer2_x  < 40)):
			P2_Area = 2
		if ((0 <= self.Pursuer2_y  < 26) and (40 <= self.Pursuer2_x  <= 84)):
			P2_Area = 3
		if ((26 <= self.Pursuer2_y  < 59) and (40 <= self.Pursuer2_x  <= 84)):
			P2_Area = 4
		if ((59 <= self.Pursuer2_y  <= 84) and (40 <= self.Pursuer2_x  <= 84)):
			P2_Area = 5
		if ((59 <= self.Pursuer2_y  <= 84) and (15 <= self.Pursuer2_x  < 40)):
			P2_Area = 6
		if ((59 <= self.Pursuer2_y  <= 84) and (0 <= self.Pursuer2_x  < 15)):
			P2_Area = 7
		if ((50 <= self.Pursuer2_y  <= 58) and (0 <= self.Pursuer2_x  < 15)):
			P2_Area = 8
		if ((34 < self.Pursuer2_y  < 50) and (0 <= self.Pursuer2_x  < 15)):
			P2_Area = 9
		if ((34 < self.Pursuer2_y  < 50) and (15 <= self.Pursuer2_x  < 31)):
			P2_Area = 10
		if ((26 <= self.Pursuer2_y  <= 34) and (0 <= self.Pursuer2_x  < 15)):
			P2_Area = 11
		else:
			P2_Area = 0
## P3 Area 

		if ((0 <= self.Pursuer3_y  < 26) and (0 <= self.Pursuer3_x  < 15)):
			P3_Area = 1
		if ((0 <= self.Pursuer3_y  < 26) and (15 <= self.Pursuer3_x  < 40)):
			P3_Area = 2
		if ((0 <= self.Pursuer3_y  < 26) and (40 <= self.Pursuer3_x  <= 84)):
			P3_Area = 3
		if ((26 <= self.Pursuer3_y  < 59) and (40 <= self.Pursuer3_x  <= 84)):
			P3_Area = 4
		if ((59 <= self.Pursuer3_y  <= 84) and (40 <= self.Pursuer3_x  <= 84)):
			P3_Area = 5
		if ((59 <= self.Pursuer3_y  <= 84) and (15 <= self.Pursuer3_x  < 40)):
			P3_Area = 6
		if ((59 <= self.Pursuer3_y  <= 84) and (0 <= self.Pursuer3_x  < 15)):
			P3_Area = 7
		if ((50 <= self.Pursuer3_y  <= 58) and (0 <= self.Pursuer3_x  < 15)):
			P3_Area = 8
		if ((34 < self.Pursuer3_y  < 50) and (0 <= self.Pursuer3_x  < 15)):
			P3_Area = 9
		if ((34 < self.Pursuer3_y  < 50) and (15 <= self.Pursuer3_x  < 31)):
			P3_Area = 10
		if ((26 <= self.Pursuer3_y  <= 34) and (0 <= self.Pursuer3_x  < 15)):
			P3_Area = 11

		else:
			P3_Area = 0



### AREA 1


		if E_Area == 1:
			
			E_tan_a = abs(self.Evader_y-26) / abs(self.Evader_x-40.1)
			E_tan_b = abs(self.Evader_y-59) / abs(self.Evader_x-15.1)
			E_tan_c = abs(self.Evader_y-35) / abs(self.Evader_x-15.1)

################# P
			if (P_Area == 4) or (P_Area == 5):
				P_tan_a = abs(self.Pursuer_y -26) / abs(self.Pursuer_x -40.1)
				if E_tan_a < P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 5) or (P_Area == 6):
				P_tan_b = abs(self.Pursuer_y -59) / abs(self.Pursuer_x -15.1)
				if E_tan_b > P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 10) :
				P_tan_c = abs(self.Pursuer_y -35) / abs(self.Pursuer_x -15.1)
				if E_tan_c > P_tan_c:
					self.P_Unvisible = True

################# P1
			if (P1_Area == 4) or (P1_Area == 5):
				P1_tan_a = abs(self.Pursuer1_y -26) / abs(self.Pursuer1_x -40.1)
				if E_tan_a < P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 5) or (P1_Area == 6):
				P1_tan_b = abs(self.Pursuer1_y -59) / abs(self.Pursuer1_x -15.1)
				if E_tan_b > P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 10) :
				P1_tan_c = abs(self.Pursuer1_y -35) / abs(self.Pursuer1_x -15.1)
				if E_tan_c > P1_tan_c:
					self.P1_Unvisible = True

################# P2
			if (P2_Area == 4) or (P2_Area == 5):
				P2_tan_a = abs(self.Pursuer2_y -26) / abs(self.Pursuer2_x -40.1)
				if E_tan_a < P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 5) or (P2_Area == 6):
				P2_tan_b = abs(self.Pursuer2_y -59) / abs(self.Pursuer2_x -15.1)
				if E_tan_b > P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 10) :
				P2_tan_c = abs(self.Pursuer2_y -35) / abs(self.Pursuer2_x -15.1)
				if E_tan_c > P2_tan_c:
					self.P2_Unvisible = True

################# P3
			if (P3_Area == 4) or (P3_Area == 5):
				P3_tan_a = abs(self.Pursuer3_y -26) / abs(self.Pursuer3_x -40.1)
				if E_tan_a < P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 5) or (P3_Area == 6):
				P3_tan_b = abs(self.Pursuer3_y -59) / abs(self.Pursuer3_x -15.1)
				if E_tan_b > P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 10) :
				P3_tan_c = abs(self.Pursuer3_y -35) / abs(self.Pursuer3_x -15.1)
				if E_tan_c > P3_tan_c:
					self.P3_Unvisible = True






### AREA 2
		if E_Area == 2:
			
			E_tan_a = abs(self.Evader_y-26) / abs(self.Evader_x-15.1)
			E_tan_b = abs(self.Evader_y-26) / abs(self.Evader_x-40.1)

################# P
			if (P_Area == 7) or (P_Area == 8) or (P_Area == 9) or (P_Area == 11) :
				P_tan_a = abs(self.Pursuer_y -26) / abs(self.Pursuer_x -15.1)
				if E_tan_a < P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 4) or (P_Area == 5):
				P_tan_b = abs(self.Pursuer_y -26) / abs(self.Pursuer_x -40.1)
				if E_tan_b < P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 10) or (P_Area == 6):
				self.P_Unvisible = True

################# P1
			if (P1_Area == 7) or (P1_Area == 8) or (P1_Area == 9) or (P1_Area == 11) :
				P1_tan_a = abs(self.Pursuer1_y -26) / abs(self.Pursuer1_x -15.1)
				if E_tan_a < P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 4) or (P1_Area == 5):
				P1_tan_b = abs(self.Pursuer1_y -26) / abs(self.Pursuer1_x -40.1)
				if E_tan_b < P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 10) or (P1_Area == 6):
				self.P1_Unvisible = True

################# P2
			if (P2_Area == 7) or (P2_Area == 8) or (P2_Area == 9) or (P2_Area == 11) :
				P2_tan_a = abs(self.Pursuer2_y -26) / abs(self.Pursuer2_x -15.1)
				if E_tan_a < P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 4) or (P2_Area == 5):
				P2_tan_b = abs(self.Pursuer2_y -26) / abs(self.Pursuer2_x -40.1)
				if E_tan_b < P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 10) or (P2_Area == 6):
				self.P2_Unvisible = True

################# P3
			if (P3_Area == 7) or (P3_Area == 8) or (P3_Area == 9) or (P3_Area == 11) :
				P3_tan_a = abs(self.Pursuer3_y -26) / abs(self.Pursuer3_x -15.1)
				if E_tan_a < P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 4) or (P3_Area == 5):
				P3_tan_b = abs(self.Pursuer3_y -26) / abs(self.Pursuer3_x -40.1)
				if E_tan_b < P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 10) or (P3_Area == 6):
				self.P3_Unvisible = True





### AREA 3
		if E_Area == 3:
			
			E_tan_a = abs(self.Evader_y-26) / abs(self.Evader_x-15.1)
			E_tan_b = abs(self.Evader_y-59) / abs(self.Evader_x-40.1)

################# P
			if (P_Area == 7) or (P_Area == 8) or (P_Area == 9) or (P_Area == 11) :
				P_tan_a = abs(self.Pursuer_y -26) / abs(self.Pursuer_x -15.1)
				if E_tan_a < P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 6) or (P_Area == 7):
				P_tan_b = abs(self.Pursuer_y -59) / abs(self.Pursuer_x -40.1)
				if E_tan_b > P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 10):
				self.P_Unvisible = True

################# P1
			if (P1_Area == 7) or (P1_Area == 8) or (P1_Area == 9) or (P1_Area == 11) :
				P1_tan_a = abs(self.Pursuer1_y -26) / abs(self.Pursuer1_x -15.1)
				if E_tan_a < P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 6) or (P1_Area == 7):
				P1_tan_b = abs(self.Pursuer1_y -59) / abs(self.Pursuer1_x -40.1)
				if E_tan_b > P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 10):
				self.P1_Unvisible = True

################# P2
			if (P2_Area == 7) or (P2_Area == 8) or (P2_Area == 9) or (P2_Area == 11) :
				P2_tan_a = abs(self.Pursuer2_y -26) / abs(self.Pursuer2_x -15.1)
				if E_tan_a < P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 6) or (P2_Area == 7):
				P2_tan_b = abs(self.Pursuer2_y -59) / abs(self.Pursuer2_x -40.1)
				if E_tan_b > P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 10):
				self.P2_Unvisible = True

################# P3
			if (P3_Area == 7) or (P3_Area == 8) or (P3_Area == 9) or (P3_Area == 11) :
				P3_tan_a = abs(self.Pursuer3_y -26) / abs(self.Pursuer3_x -15.1)
				if E_tan_a < P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 6) or (P3_Area == 7):
				P3_tan_b = abs(self.Pursuer3_y -59) / abs(self.Pursuer3_x -40.1)
				if E_tan_b > P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 10):
				self.P3_Unvisible = True





### AREA 4
		if E_Area == 4:
			
			E_tan_a = abs(self.Evader_y-26) / abs(self.Evader_x-40.1)
			E_tan_b = abs(self.Evader_y-59) / abs(self.Evader_x-40.1)

################# P
			if (P_Area == 1) or (P_Area == 2) :
				P_tan_a = abs(self.Pursuer_y -26) / abs(self.Pursuer_x -40.1)
				if E_tan_a > P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 6) or (P_Area == 7):
				P_tan_b = abs(self.Pursuer_y -59) / abs(self.Pursuer_x -40.1)
				if E_tan_b > P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 8) or (P_Area == 9) or (P_Area == 10) or (P_Area == 11):
				self.P_Unvisible = True

################# P1
			if (P1_Area == 1) or (P1_Area == 2) :
				P1_tan_a = abs(self.Pursuer1_y -26) / abs(self.Pursuer1_x -40.1)
				if E_tan_a > P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 6) or (P1_Area == 7):
				P1_tan_b = abs(self.Pursuer1_y -59) / abs(self.Pursuer1_x -40.1)
				if E_tan_b > P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 8) or (P1_Area == 9) or (P1_Area == 10) or (P1_Area == 11):
				self.P1_Unvisible = True

################# P2
			if (P2_Area == 1) or (P2_Area == 2) :
				P2_tan_a = abs(self.Pursuer2_y -26) / abs(self.Pursuer2_x -40.1)
				if E_tan_a > P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 6) or (P2_Area == 7):
				P2_tan_b = abs(self.Pursuer2_y -59) / abs(self.Pursuer2_x -40.1)
				if E_tan_b > P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 8) or (P2_Area == 9) or (P2_Area == 10) or (P2_Area == 11):
				self.P2_Unvisible = True

################# P3
			if (P3_Area == 1) or (P3_Area == 2) :
				P3_tan_a = abs(self.Pursuer3_y -26) / abs(self.Pursuer3_x -40.1)
				if E_tan_a > P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 6) or (P3_Area == 7):
				P3_tan_b = abs(self.Pursuer3_y -59) / abs(self.Pursuer3_x -40.1)
				if E_tan_b > P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 8) or (P3_Area == 9) or (P3_Area == 10) or (P3_Area == 11):
				self.P3_Unvisible = True





### AREA 5
		if E_Area == 5:
			
			E_tan_a = abs(self.Evader_y-26) / abs(self.Evader_x-40.1)
			E_tan_b = abs(self.Evader_y-59) / abs(self.Evader_x-15.1)

################# P
			if (P_Area == 1) or (P_Area == 2) :
				P_tan_a = abs(self.Pursuer_y -26) / abs(self.Pursuer_x -40.1)
				if E_tan_a > P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 8) or (P_Area == 9) or (P_Area == 11) or (P_Area == 1):
				P_tan_b = abs(self.Pursuer_y -59) / abs(self.Pursuer_x -15.1)
				if E_tan_b < P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 10):
				self.P_Unvisible = True

################# P1
			if (P1_Area == 1) or (P1_Area == 2) :
				P1_tan_a = abs(self.Pursuer1_y -26) / abs(self.Pursuer1_x -40.1)
				if E_tan_a > P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 8) or (P1_Area == 9) or (P1_Area == 11) or (P1_Area == 1):
				P1_tan_b = abs(self.Pursuer1_y -59) / abs(self.Pursuer1_x -15.1)
				if E_tan_b < P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 10):
				self.P1_Unvisible = True

################# P2
			if (P2_Area == 1) or (P2_Area == 2) :
				P2_tan_a = abs(self.Pursuer2_y -26) / abs(self.Pursuer2_x -40.1)
				if E_tan_a > P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 8) or (P2_Area == 9) or (P2_Area == 11) or (P2_Area == 1):
				P2_tan_b = abs(self.Pursuer2_y -59) / abs(self.Pursuer2_x -15.1)
				if E_tan_b < P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 10):
				self.P2_Unvisible = True

################# P3
			if (P3_Area == 1) or (P3_Area == 2) :
				P3_tan_a = abs(self.Pursuer3_y -26) / abs(self.Pursuer3_x -40.1)
				if E_tan_a > P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 8) or (P3_Area == 9) or (P3_Area == 11) or (P3_Area == 1):
				P3_tan_b = abs(self.Pursuer3_y -59) / abs(self.Pursuer3_x -15.1)
				if E_tan_b < P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 10):
				self.P3_Unvisible = True





### AREA 6
		if E_Area == 6:
			
			E_tan_a = abs(self.Evader_y-59) / abs(self.Evader_x-15.1)
			E_tan_b = abs(self.Evader_y-59) / abs(self.Evader_x-40.1)

################# P
			if (P_Area == 1) or (P_Area == 8) or (P_Area == 9) or (P_Area == 11):
				P_tan_a = abs(self.Pursuer_y -59) / abs(self.Pursuer_x -15.1)
				if E_tan_a < P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 3) or (P_Area == 4):
				P_tan_b = abs(self.Pursuer_y -59) / abs(self.Pursuer_x -40.1)
				if E_tan_b < P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 10) or (P_Area == 2):
				self.P_Unvisible = True

################# P1
			if (P1_Area == 1) or (P1_Area == 8) or (P1_Area == 9) or (P1_Area == 11):
				P1_tan_a = abs(self.Pursuer1_y -59) / abs(self.Pursuer1_x -15.1)
				if E_tan_a < P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 3) or (P1_Area == 4):
				P1_tan_b = abs(self.Pursuer1_y -59) / abs(self.Pursuer1_x -40.1)
				if E_tan_b < P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 10) or (P1_Area == 2):
				self.P1_Unvisible = True

################# P2
			if (P2_Area == 1) or (P2_Area == 8) or (P2_Area == 9) or (P2_Area == 11):
				P2_tan_a = abs(self.Pursuer2_y -59) / abs(self.Pursuer2_x -15.1)
				if E_tan_a < P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 3) or (P2_Area == 4):
				P2_tan_b = abs(self.Pursuer2_y -59) / abs(self.Pursuer2_x -40.1)
				if E_tan_b < P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 10) or (P2_Area == 2):
				self.P2_Unvisible = True

################# P3
			if (P3_Area == 1) or (P3_Area == 8) or (P3_Area == 9) or (P3_Area == 11):
				P3_tan_a = abs(self.Pursuer3_y -59) / abs(self.Pursuer3_x -15.1)
				if E_tan_a < P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 3) or (P3_Area == 4):
				P3_tan_b = abs(self.Pursuer3_y -59) / abs(self.Pursuer3_x -40.1)
				if E_tan_b < P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 10) or (P3_Area == 2):
				self.P3_Unvisible = True






### AREA 7
		if E_Area == 7:
			
			E_tan_a = abs(self.Evader_y-59) / abs(self.Evader_x-40.1)
			E_tan_b = abs(self.Evader_y-26) / abs(self.Evader_x-15.1)
			E_tan_c = abs(self.Evader_y-50) / abs(self.Evader_x-15.1)

################# P
			if (P_Area == 3) or (P_Area == 4):
				P_tan_a = abs(self.Pursuer_y -59) / abs(self.Pursuer_x -40.1)
				if E_tan_a < P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 2) or (P_Area == 3):
				P_tan_b = abs(self.Pursuer_y -26) / abs(self.Pursuer_x -15.1)
				if E_tan_b > P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 10) :
				P_tan_c = abs(self.Pursuer_y -50) / abs(self.Pursuer_x -15.1)
				if E_tan_c > P_tan_c:
					self.P_Unvisible = True

################# P1
			if (P1_Area == 3) or (P1_Area == 4):
				P1_tan_a = abs(self.Pursuer1_y -59) / abs(self.Pursuer1_x -40.1)
				if E_tan_a < P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 2) or (P1_Area == 3):
				P1_tan_b = abs(self.Pursuer1_y -26) / abs(self.Pursuer1_x -15.1)
				if E_tan_b > P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 10) :
				P1_tan_c = abs(self.Pursuer1_y -50) / abs(self.Pursuer1_x -15.1)
				if E_tan_c > P1_tan_c:
					self.P1_Unvisible = True

################# P2
			if (P2_Area == 3) or (P2_Area == 4):
				P2_tan_a = abs(self.Pursuer2_y -59) / abs(self.Pursuer2_x -40.1)
				if E_tan_a < P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 2) or (P2_Area == 3):
				P2_tan_b = abs(self.Pursuer2_y -26) / abs(self.Pursuer2_x -15.1)
				if E_tan_b > P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 10) :
				P2_tan_c = abs(self.Pursuer2_y -50) / abs(self.Pursuer2_x -15.1)
				if E_tan_c > P2_tan_c:
					self.P2_Unvisible = True

################# P3
			if (P3_Area == 3) or (P3_Area == 4):
				P3_tan_a = abs(self.Pursuer3_y -59) / abs(self.Pursuer3_x -40.1)
				if E_tan_a < P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 2) or (P3_Area == 3):
				P3_tan_b = abs(self.Pursuer3_y -26) / abs(self.Pursuer3_x -15.1)
				if E_tan_b > P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 10) :
				P3_tan_c = abs(self.Pursuer3_y -50) / abs(self.Pursuer3_x -15.1)
				if E_tan_c > P3_tan_c:
					self.P3_Unvisible = True





### AREA 8
		if E_Area == 8:
			
			E_tan_a = abs(self.Evader_y-59) / abs(self.Evader_x-15.1)
			E_tan_b = abs(self.Evader_y-26) / abs(self.Evader_x-15.1)
			E_tan_c = abs(self.Evader_y-50) / abs(self.Evader_x-15.1)

################# P
			if (P_Area == 5) or (P_Area == 6):
				P_tan_a = abs(self.Pursuer_y -59) / abs(self.Pursuer_x -15.1)
				if E_tan_a > P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 2) or (P_Area == 3):
				P_tan_b = abs(self.Pursuer_y -26) / abs(self.Pursuer_x -15.1)
				if E_tan_b > P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 10) :
				P_tan_c = abs(self.Pursuer_y -50) / abs(self.Pursuer_x -15.1)
				if E_tan_c > P_tan_c:
					self.P_Unvisible = True

			if (P_Area == 4):
				self.P_Unvisible = True

################# P1
			if (P1_Area == 5) or (P1_Area == 6):
				P1_tan_a = abs(self.Pursuer1_y -59) / abs(self.Pursuer1_x -15.1)
				if E_tan_a > P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 2) or (P1_Area == 3):
				P1_tan_b = abs(self.Pursuer1_y -26) / abs(self.Pursuer1_x -15.1)
				if E_tan_b > P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 10) :
				P1_tan_c = abs(self.Pursuer1_y -50) / abs(self.Pursuer1_x -15.1)
				if E_tan_c > P1_tan_c:
					self.P1_Unvisible = True

			if (P1_Area == 4):
				self.P1_Unvisible = True

################# P2
			if (P2_Area == 5) or (P2_Area == 6):
				P2_tan_a = abs(self.Pursuer2_y -59) / abs(self.Pursuer2_x -15.1)
				if E_tan_a > P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 2) or (P2_Area == 3):
				P2_tan_b = abs(self.Pursuer2_y -26) / abs(self.Pursuer2_x -15.1)
				if E_tan_b > P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 10) :
				P2_tan_c = abs(self.Pursuer2_y -50) / abs(self.Pursuer2_x -15.1)
				if E_tan_c > P2_tan_c:
					self.P2_Unvisible = True

			if (P2_Area == 4):
				self.P2_Unvisible = True

################# P3
			if (P3_Area == 5) or (P3_Area == 6):
				P3_tan_a = abs(self.Pursuer3_y -59) / abs(self.Pursuer3_x -15.1)
				if E_tan_a > P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 2) or (P3_Area == 3):
				P3_tan_b = abs(self.Pursuer3_y -26) / abs(self.Pursuer3_x -15.1)
				if E_tan_b > P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 10) :
				P3_tan_c = abs(self.Pursuer3_y -50) / abs(self.Pursuer3_x -15.1)
				if E_tan_c > P3_tan_c:
					self.P3_Unvisible = True

			if (P3_Area == 4):
				self.P3_Unvisible = True






### AREA 9
		if E_Area == 9:
			
			E_tan_a = abs(self.Evader_y-59) / abs(self.Evader_x-15.1)
			E_tan_b = abs(self.Evader_y-26) / abs(self.Evader_x-15.1)

################# P
			if (P_Area == 5) or (P_Area == 6):
				P_tan_a = abs(self.Pursuer_y -59) / abs(self.Pursuer_x -15.1)
				if E_tan_a > P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 2) or (P_Area == 3):
				P_tan_b = abs(self.Pursuer_y -26) / abs(self.Pursuer_x -15.1)
				if E_tan_b > P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 4):
				self.P_Unvisible = True

################# P1
			if (P1_Area == 5) or (P1_Area == 6):
				P1_tan_a = abs(self.Pursuer1_y -59) / abs(self.Pursuer1_x -15.1)
				if E_tan_a > P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 2) or (P1_Area == 3):
				P1_tan_b = abs(self.Pursuer1_y -26) / abs(self.Pursuer1_x -15.1)
				if E_tan_b > P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 4):
				self.P1_Unvisible = True

################# P2
			if (P2_Area == 5) or (P2_Area == 6):
				P2_tan_a = abs(self.Pursuer2_y -59) / abs(self.Pursuer2_x -15.1)
				if E_tan_a > P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 2) or (P2_Area == 3):
				P2_tan_b = abs(self.Pursuer2_y -26) / abs(self.Pursuer2_x -15.1)
				if E_tan_b > P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 4):
				self.P2_Unvisible = True

################# P3
			if (P3_Area == 5) or (P3_Area == 6):
				P3_tan_a = abs(self.Pursuer3_y -59) / abs(self.Pursuer3_x -15.1)
				if E_tan_a > P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 2) or (P3_Area == 3):
				P3_tan_b = abs(self.Pursuer3_y -26) / abs(self.Pursuer3_x -15.1)
				if E_tan_b > P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 4):
				self.P3_Unvisible = True





### AREA 10
		if E_Area == 10:
			
			E_tan_a = abs(self.Evader_y-35) / abs(self.Evader_x-15.1)
			E_tan_b = abs(self.Evader_y-50) / abs(self.Evader_x-15.1)

################# P
			if (P_Area == 5) or (P_Area == 6):
				P_tan_a = abs(self.Pursuer_y -35) / abs(self.Pursuer_x -15.1)
				if E_tan_a < P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 2) or (P_Area == 3):
				P_tan_b = abs(self.Pursuer_y -50) / abs(self.Pursuer_x -15.1)
				if E_tan_b < P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 2) or (P_Area == 3) or (P_Area == 4) or (P_Area == 5) or (P_Area == 6):
				self.P_Unvisible = True

################# P1
			if (P1_Area == 5) or (P1_Area == 6):
				P1_tan_a = abs(self.Pursuer1_y -35) / abs(self.Pursuer1_x -15.1)
				if E_tan_a < P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 2) or (P1_Area == 3):
				P1_tan_b = abs(self.Pursuer1_y -50) / abs(self.Pursuer1_x -15.1)
				if E_tan_b < P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 2) or (P1_Area == 3) or (P1_Area == 4) or (P1_Area == 5) or (P1_Area == 6):
				self.P1_Unvisible = True

################# P2
			if (P2_Area == 5) or (P2_Area == 6):
				P2_tan_a = abs(self.Pursuer2_y -35) / abs(self.Pursuer2_x -15.1)
				if E_tan_a < P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 2) or (P2_Area == 3):
				P2_tan_b = abs(self.Pursuer2_y -50) / abs(self.Pursuer2_x -15.1)
				if E_tan_b < P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 2) or (P2_Area == 3) or (P2_Area == 4) or (P2_Area == 5) or (P2_Area == 6):
				self.P2_Unvisible = True

################# P3
			if (P3_Area == 5) or (P3_Area == 6):
				P3_tan_a = abs(self.Pursuer3_y -35) / abs(self.Pursuer3_x -15.1)
				if E_tan_a < P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 2) or (P3_Area == 3):
				P3_tan_b = abs(self.Pursuer3_y -50) / abs(self.Pursuer3_x -15.1)
				if E_tan_b < P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 2) or (P3_Area == 3) or (P3_Area == 4) or (P3_Area == 5) or (P3_Area == 6):
				self.P3_Unvisible = True





### AREA 11
		if E_Area == 11:
			
			E_tan_a = abs(self.Evader_y-59) / abs(self.Evader_x-15.1)
			E_tan_b = abs(self.Evader_y-26) / abs(self.Evader_x-15.1)
			E_tan_c = abs(self.Evader_y-35) / abs(self.Evader_x-15.1)

################# P
			if (P_Area == 5) or (P_Area == 6):
				P_tan_a = abs(self.Pursuer_y -59) / abs(self.Pursuer_x -15.1)
				if E_tan_a > P_tan_a:
					self.P_Unvisible = True

			if (P_Area == 2) or (P_Area == 3):
				P_tan_b = abs(self.Pursuer_y -26) / abs(self.Pursuer_x -15.1)
				if E_tan_b > P_tan_b:
					self.P_Unvisible = True

			if (P_Area == 10) :
				P_tan_c = abs(self.Pursuer_y -35) / abs(self.Pursuer_x -15.1)
				if E_tan_c > P_tan_c:
					self.P_Unvisible = True

			if (P_Area == 4):
				self.P_Unvisible = True

################# P1
			if (P1_Area == 5) or (P1_Area == 6):
				P1_tan_a = abs(self.Pursuer1_y -59) / abs(self.Pursuer1_x -15.1)
				if E_tan_a > P1_tan_a:
					self.P1_Unvisible = True

			if (P1_Area == 2) or (P1_Area == 3):
				P1_tan_b = abs(self.Pursuer1_y -26) / abs(self.Pursuer1_x -15.1)
				if E_tan_b > P1_tan_b:
					self.P1_Unvisible = True

			if (P1_Area == 10) :
				P1_tan_c = abs(self.Pursuer1_y -35) / abs(self.Pursuer1_x -15.1)
				if E_tan_c > P1_tan_c:
					self.P1_Unvisible = True

			if (P1_Area == 4):
				self.P1_Unvisible = True

################# P2
			if (P2_Area == 5) or (P2_Area == 6):
				P2_tan_a = abs(self.Pursuer2_y -59) / abs(self.Pursuer2_x -15.1)
				if E_tan_a > P2_tan_a:
					self.P2_Unvisible = True

			if (P2_Area == 2) or (P2_Area == 3):
				P2_tan_b = abs(self.Pursuer2_y -26) / abs(self.Pursuer2_x -15.1)
				if E_tan_b > P2_tan_b:
					self.P2_Unvisible = True

			if (P2_Area == 10) :
				P2_tan_c = abs(self.Pursuer2_y -35) / abs(self.Pursuer2_x -15.1)
				if E_tan_c > P2_tan_c:
					self.P2_Unvisible = True

			if (P2_Area == 4):
				self.P2_Unvisible = True

################# P3
			if (P3_Area == 5) or (P3_Area == 6):
				P3_tan_a = abs(self.Pursuer3_y -59) / abs(self.Pursuer3_x -15.1)
				if E_tan_a > P3_tan_a:
					self.P3_Unvisible = True

			if (P3_Area == 2) or (P3_Area == 3):
				P3_tan_b = abs(self.Pursuer3_y -26) / abs(self.Pursuer3_x -15.1)
				if E_tan_b > P3_tan_b:
					self.P3_Unvisible = True

			if (P3_Area == 10) :
				P3_tan_c = abs(self.Pursuer3_y -35) / abs(self.Pursuer3_x -15.1)
				if E_tan_c > P3_tan_c:
					self.P3_Unvisible = True

			if (P3_Area == 4):
				self.P3_Unvisible = True









