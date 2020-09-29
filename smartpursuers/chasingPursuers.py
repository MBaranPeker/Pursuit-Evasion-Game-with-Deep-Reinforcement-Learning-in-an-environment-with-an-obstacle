import numpy as np
import time
import random
from tqdm import tqdm
import os



class ChasingPursuers:

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

		self.action_pursuer = 5
		self.action_pursuer1 = 5
		self.action_pursuer2 = 5
		self.action_pursuer3 = 5


		self.chasing()


	def chasing(self):

# P		
		if abs(self.Evader_x - self.Pursuer_x) == abs(self.Evader_y - self.Pursuer_y ):

			if (self.Evader_x > self.Pursuer_x) and (self.Evader_y > self.Pursuer_y ):
				action_random_list = [2,4]
				self.action_pursuer = random.choice(action_random_list)
			elif (self.Evader_x > self.Pursuer_x) and (self.Evader_y < self.Pursuer_y ):
				action_random_list_1 = [3,4]
				self.action_pursuer = random.choice(action_random_list_1)
			elif (self.Evader_x < self.Pursuer_x) and (self.Evader_y < self.Pursuer_y ):
				action_random_list_2 = [1,3]
				self.action_pursuer = random.choice(action_random_list_2)
			else:
				action_random_list_3 = [1,2]
				self.action_pursuer = random.choice(action_random_list_3)


		elif abs(self.Evader_x-self.Pursuer_x) > abs(self.Evader_y-self.Pursuer_y ):

			if (self.Evader_x > self.Pursuer_x):
				self.action_pursuer = 4
			else:
				self.action_pursuer = 1
		elif abs(self.Evader_x-self.Pursuer_x) < abs(self.Evader_y-self.Pursuer_y ):

			if (self.Evader_y > self.Pursuer_y ):
				self.action_pursuer = 2
			else:
				self.action_pursuer = 3

# P1
		if abs(self.Evader_x-self.Pursuer1_x) == abs(self.Evader_y-self.Pursuer1_y ):

			if (self.Evader_x > self.Pursuer1_x) and (self.Evader_y > self.Pursuer1_y ):
				action_random_list = [2,4]
				self.action_pursuer1 = random.choice(action_random_list)
			elif (self.Evader_x > self.Pursuer1_x) and (self.Evader_y < self.Pursuer1_y ):
				action_random_list_1 = [3,4]
				self.action_pursuer1 = random.choice(action_random_list_1)
			elif (self.Evader_x < self.Pursuer1_x) and (self.Evader_y < self.Pursuer1_y ):
				action_random_list_2 = [1,3]
				self.action_pursuer1 = random.choice(action_random_list_2)
			else:
				action_random_list_3 = [1,2]
				self.action_pursuer1 = random.choice(action_random_list_3)

		elif abs(self.Evader_x-self.Pursuer1_x) > abs(self.Evader_y-self.Pursuer1_y ):

			if (self.Evader_x > self.Pursuer1_x):
				self.action_pursuer1 = 4
			else:
				self.action_pursuer1 = 1
		elif abs(self.Evader_x-self.Pursuer1_x) < abs(self.Evader_y-self.Pursuer1_y ):

			if (self.Evader_y > self.Pursuer1_y ):
				self.action_pursuer1 = 2
			else:
				self.action_pursuer1 = 3

# P2
		if abs(self.Evader_x-self.Pursuer2_x) == abs(self.Evader_y-self.Pursuer2_y ):

			if (self.Evader_x > self.Pursuer2_x) and (self.Evader_y > self.Pursuer2_y ):
				action_random_list = [2,4]
				self.action_pursuer2 = random.choice(action_random_list)
			elif (self.Evader_x > self.Pursuer2_x) and (self.Evader_y < self.Pursuer2_y ):
				action_random_list_1 = [3,4]
				self.action_pursuer2 = random.choice(action_random_list_1)
			elif (self.Evader_x < self.Pursuer2_x) and (self.Evader_y < self.Pursuer2_y ):
				action_random_list_2 = [1,3]
				self.action_pursuer2 = random.choice(action_random_list_2)
			else:
				action_random_list_3 = [1,2]
				self.action_pursuer2 = random.choice(action_random_list_3)

		elif abs(self.Evader_x-self.Pursuer2_x) > abs(self.Evader_y-self.Pursuer2_y ):

			if (self.Evader_x > self.Pursuer2_x):
				self.action_pursuer2 = 4
			else:
				self.action_pursuer2 = 1
		elif abs(self.Evader_x-self.Pursuer2_x) < abs(self.Evader_y-self.Pursuer2_y ):

			if (self.Evader_y > self.Pursuer2_y ):
				self.action_pursuer2 = 2
			else:
				self.action_pursuer2 = 3

# P3
		if abs(self.Evader_x-self.Pursuer3_x) == abs(self.Evader_y-self.Pursuer3_y ):

			if (self.Evader_x > self.Pursuer3_x) and (self.Evader_y > self.Pursuer3_y ):
				action_random_list = [2,4]
				self.action_pursuer3 = random.choice(action_random_list)
			elif (self.Evader_x > self.Pursuer3_x) and (self.Evader_y < self.Pursuer3_y ):
				action_random_list_1 = [3,4]
				self.action_pursuer3 = random.choice(action_random_list_1)
			elif (self.Evader_x < self.Pursuer3_x) and (self.Evader_y < self.Pursuer3_y ):
				action_random_list_2 = [1,3]
				self.action_pursuer3 = random.choice(action_random_list_2)
			else:
				action_random_list_3 = [1,2]
				self.action_pursuer3 = random.choice(action_random_list_3)

		elif abs(self.Evader_x-self.Pursuer3_x) > abs(self.Evader_y-self.Pursuer3_y ):

			if (self.Evader_x > self.Pursuer3_x):
				self.action_pursuer3 = 4
			else:
				self.action_pursuer3 = 1
		elif abs(self.Evader_x-self.Pursuer3_x) < abs(self.Evader_y-self.Pursuer3_y ):

			if (self.Evader_y > self.Pursuer3_y ):
				self.action_pursuer3 = 2
			else:
				self.action_pursuer3 = 3































