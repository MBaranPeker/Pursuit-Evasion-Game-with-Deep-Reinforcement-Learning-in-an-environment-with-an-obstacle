import random
import numpy as np

SIZE = 84


class Blob:

	def __init__(self):

		self.x = np.random.randint(41, 82)
		self.y = np.random.randint(1, 82)

		while True:
			if (((14 <= self.x <= 40)  and (25 <= self.y <= 35)) or ((14 <= self.x <= 40)  and (49 <= self.y <= 59)) or ((30 <= self.x <= 40) and (14 <= self.y <= 59))):

				self.x = np.random.randint(41, 82)
				self.y = np.random.randint(1, 82)
				
			else:
				break


## REPRESENT LOCATION OF ANY BLOB WE WANT
	def __str__(self):
		return f"{self.x}, {self.y}"

## SUBSTRACT a BLOB FROM ANOTHER BLOB
	def __sub__(self,other):
		return(self.x - other.x, self.y - other.y)

## ACTION evader 
	def action_e(self, choice):

		if choice == 0:               ## move right
			self.move_e(x=0, y=0)
		if choice == 1:               ## move left
			self.move_e(x=-1, y=0)
		if choice == 2:               ## move 
			self.move_e(x=0, y=1)
		if choice == 3:               ## move right
			self.move_e(x=0, y=-1)
		if choice == 4:               ## move right
			self.move_e(x=1, y=0)

	def move_e(self, x, y):

		self.x += x

		self.y += y


## THIS PART KEEPS AGENTS INSIDE THE BOUNDRIES

		if self.x < 1:
			self.x = 1
		elif self.x > (SIZE-2):
			self.x = SIZE -2

		if self.y < 1:
			self.y = 1
		elif self.y > SIZE -2:
			self.y = SIZE -2



class Blob1() :

	def __init__(self, Ev_X, Ev_Y):

		self.x = np.random.randint(41, 82)
		self.y = np.random.randint(1, 82)

		while True:
			if (((14 <= self.x <= 40)  and (25 <= self.y <= 35)) or ((14 <= self.x <= 40)  and (49 <= self.y <= 59)) or ((30 <= self.x <= 40)  and (14 <= self.y <= 59)) or ((self.x == Ev_X) and (self.y == Ev_Y))):

				self.x = np.random.randint(41, 82)
				self.y = np.random.randint(1, 82)
				
			else:
				break

## REPRESENT LOCATION OF ANY BLOB WE WANT


## ACTION pursuer

	def action_p(self, choice):

		if choice == 0:               ## move right
			self.move_p(x=0, y=0)
		if choice == 1:               ## move left
			self.move_p(x=-1, y=0)
		if choice == 2:               ## move 
			self.move_p(x=0, y=1)
		if choice == 3:               ## move right
			self.move_p(x=0, y=-1)
		if choice == 4:               ## move right
			self.move_p(x=1, y=0)

	def move_p(self, x, y):

		self.x += x

		self.y += y




## THIS PART KEEPS AGENTS INSIDE THE BOUNDRIES

		if self.x < 1:
			self.x = 1
		elif self.x > (SIZE-2):
			self.x = SIZE -2

		if self.y < 1:
			self.y = 1
		elif self.y > SIZE -2:
			self.y = SIZE -2




class Blob2:

	def __init__(self, Ev_X, Ev_Y, P_X, P_Y):

		self.x = np.random.randint(41, 82)
		self.y = np.random.randint(1, 82)

		
		while True:
			if (((14 <= self.x <= 40)  and (25 <= self.y <= 35)) or ((14 <= self.x <= 40)  and (49 <= self.y <= 59)) or ((30 <= self.x <= 40)  and (14 <= self.y <= 59)) or ((self.x == Ev_X) and (self.y == Ev_Y)) or ((self.x == P_X) and (self.y == P_Y))):

				self.x = np.random.randint(41, 82)
				self.y = np.random.randint(1, 82)
				
			else:
				break


## REPRESENT LOCATION OF ANY BLOB WE WANT


## ACTION pursuer

	def action_p(self, choice):

		if choice == 0:               ## move right
			self.move_p(x=0, y=0)
		if choice == 1:               ## move left
			self.move_p(x=-1, y=0)
		if choice == 2:               ## move 
			self.move_p(x=0, y=1)
		if choice == 3:               ## move right
			self.move_p(x=0, y=-1)
		if choice == 4:               ## move right
			self.move_p(x=1, y=0)


	def move_p(self, x, y):

		self.x += x

		self.y += y




## THIS PART KEEPS AGENTS INSIDE THE BOUNDRIES

		if self.x < 1:
			self.x = 1
		elif self.x > (SIZE-2):
			self.x = SIZE -2

		if self.y < 1:
			self.y = 1
		elif self.y > SIZE -2:
			self.y = SIZE -2



		if ((30 >= self.y >= 25) and (39>=self.x>=15)) :
			self.y = 24
		if ((59 >= self.y >= 54) and (39>=self.x>=15)) :
			self.y = 60
		if ((35 >= self.y > 30) and (31>=self.x>=15)) :
			self.y = 36
		if ((54 > self.y >= 49) and (31>=self.x>=15)) :
			self.y = 48

		if ((17 >= self.x >= 14) and (34>=self.y>=26)) :
			self.x = 13
		if ((17 >= self.x >= 14) and (58>=self.y>=50)) :
			self.x = 13
		if ((35 > self.x >= 30) and (50>=self.y>=34)) :
			self.x = 29
		if ((40 >= self.x >= 35) and (58>=self.y>=26)) :
			self.x = 41


class Blob3:

	def __init__(self, Ev_X, Ev_Y, P_X, P_Y, P1_X, P1_Y):

		self.x = np.random.randint(41, 82)
		self.y = np.random.randint(1, 82)

		
		while True:
			if (((14 <= self.x <= 40)  and (25 <= self.y <= 35)) or ((14 <= self.x <= 40)  and (49 <= self.y <= 59)) or ((30 <= self.x <= 40)  and (14 <= self.y <= 59)) or ((self.x == Ev_X) and (self.y == Ev_Y)) or ((self.x == P_X) and (self.y == P_Y)) or ((self.x == P1_X) and (self.y == P1_Y))):

				self.x = np.random.randint(41, 82)
				self.y = np.random.randint(1, 82)
				
			else:
				break

## REPRESENT LOCATION OF ANY BLOB WE WANT


## ACTION pursuer

	def action_p(self, choice):

		if choice == 0:               ## move right
			self.move_p(x=0, y=0)
		if choice == 1:               ## move left
			self.move_p(x=-1, y=0)
		if choice == 2:               ## move 
			self.move_p(x=0, y=1)
		if choice == 3:               ## move right
			self.move_p(x=0, y=-1)
		if choice == 4:               ## move right
			self.move_p(x=1, y=0)




	def move_p(self, x, y):

		self.x += x

		self.y += y




## THIS PART KEEPS AGENTS INSIDE THE BOUNDRIES

		if self.x < 1:
			self.x = 1
		elif self.x > (SIZE-2):
			self.x = SIZE -2

		if self.y < 1:
			self.y = 1
		elif self.y > SIZE -2:
			self.y = SIZE -2


		if ((30 >= self.y >= 25) and (39>=self.x>=15)) :
			self.y = 24
		if ((59 >= self.y >= 54) and (39>=self.x>=15)) :
			self.y = 60
		if ((35 >= self.y > 30) and (31>=self.x>=15)) :
			self.y = 36
		if ((54 > self.y >= 49) and (31>=self.x>=15)) :
			self.y = 48

		if ((17 >= self.x >= 14) and (34>=self.y>=26)) :
			self.x = 13
		if ((17 >= self.x >= 14) and (58>=self.y>=50)) :
			self.x = 13
		if ((35 > self.x >= 30) and (50>=self.y>=34)) :
			self.x = 29
		if ((40 >= self.x >= 35) and (58>=self.y>=26)) :
			self.x = 41


class Blob4:

	def __init__(self, Ev_X, Ev_Y, P_X, P_Y, P1_X, P1_Y, P2_X, P2_Y):

		self.x = np.random.randint(41, 82)
		self.y = np.random.randint(1, 82)

		
		while True:
			if (((14 <= self.x <= 40)  and (25 <= self.y <= 35)) or ((14 <= self.x <= 40)  and (49 <= self.y <= 59)) or ((30 <= self.x <= 40)  and (14 <= self.y <= 59)) or ((self.x == Ev_X) and (self.y == Ev_Y)) or ((self.x == P_X) and (self.y == P_Y)) or ((self.x == P1_X) and (self.y == P1_Y)) or ((self.x == P2_X) and (self.y == P2_Y))):

				self.x = np.random.randint(41, 82)
				self.y = np.random.randint(1, 82)
				
			else:
				break


## REPRESENT LOCATION OF ANY BLOB WE WANT


## ACTION pursuer

	def action_p(self, choice):

		if choice == 0:               ## move right
			self.move_p(x=0, y=0)
		if choice == 1:               ## move left
			self.move_p(x=-1, y=0)
		if choice == 2:               ## move 
			self.move_p(x=0, y=1)
		if choice == 3:               ## move right
			self.move_p(x=0, y=-1)
		if choice == 4:               ## move right
			self.move_p(x=1, y=0)



	def move_p(self, x, y):

		self.x += x

		self.y += y



## THIS PART KEEPS AGENTS INSIDE THE BOUNDRIES

		if self.x < 1:
			self.x = 1
		elif self.x > (SIZE-2):
			self.x = SIZE -2

		if self.y < 1:
			self.y = 1
		elif self.y > SIZE -2:
			self.y = SIZE -2



		if ((30 >= self.y >= 25) and (39>=self.x>=15)) :
			self.y = 24
		if ((59 >= self.y >= 54) and (39>=self.x>=15)) :
			self.y = 60
		if ((35 >= self.y > 30) and (31>=self.x>=15)) :
			self.y = 36
		if ((54 > self.y >= 49) and (31>=self.x>=15)) :
			self.y = 48

		if ((17 >= self.x >= 14) and (34>=self.y>=26)) :
			self.x = 13
		if ((17 >= self.x >= 14) and (58>=self.y>=50)) :
			self.x = 13
		if ((35 > self.x >= 30) and (50>=self.y>=34)) :
			self.x = 29
		if ((40 >= self.x >= 35) and (58>=self.y>=26)) :
			self.x = 41















