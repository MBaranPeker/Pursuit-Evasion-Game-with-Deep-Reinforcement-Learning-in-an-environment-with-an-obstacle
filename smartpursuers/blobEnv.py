import numpy as np
import keras.backend.tensorflow_backend as backend
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Activation, Flatten
from keras.optimizers import Adam
from keras.callbacks import TensorBoard
import tensorflow as tf
from collections import deque
import time
import random
from tqdm import tqdm
import os
from PIL import Image
import cv2
from blob import Blob
from blob import Blob1
from blob import Blob2
from blob import Blob3
from blob import Blob4
from eyesight import Eyesight
from chasingPursuers import ChasingPursuers
from replay_buffer import ReplayBuffer
from deep_Q import DeepQ
from repulsive import Repulsive


REPLAY_MEMORY_SIZE = 50_000  # How many last steps to keep for model training
MIN_OBSERVATION = 40_000  # Minimum number of steps in a memory to start training
MINIBATCH_SIZE = 128  # How many steps (samples) to use for training


EPISODES = 1_000_000

# Exploration settings
epsilon = 1.0
min_epsilon = 0.05
check_epsilon = 0
EPS_DECAY = 0.00002
EPS_renew_time = 14
EPS_counter = 0

SIZE = 84
MOVE_PENALTY = 1
ENEMY_PENALTY = 10


replay_buffer = ReplayBuffer(REPLAY_MEMORY_SIZE)
deep_q = DeepQ()

observation_num = 0


deep_q.trained_model("targetmodel_v2")

for episode in range(EPISODES):

	evader = Blob()
	Evader_x = evader.x
	Evader_y = evader.y

	pursuer = Blob1(Evader_x, Evader_y)
	Pursuer_x = pursuer.x
	Pursuer_y = pursuer.y

	pursuer1 = Blob2(Evader_x, Evader_y, Pursuer_x, Pursuer_y)
	Pursuer1_x = pursuer1.x
	Pursuer1_y = pursuer1.y

	pursuer2 = Blob3(Evader_x, Evader_y, Pursuer_x, Pursuer_y, Pursuer1_x, Pursuer1_y)
	Pursuer2_x = pursuer2.x
	Pursuer2_y = pursuer2.y

	pursuer3 = Blob4(Evader_x, Evader_y, Pursuer_x, Pursuer_y, Pursuer1_x, Pursuer1_y, Pursuer2_x, Pursuer2_y)


	episode_reward = 0 

	for episode_step in range(200):

		reward = 0
		observation_num += 1

###
		Visible = Eyesight(evader.x, evader.y, pursuer.x, pursuer.y, pursuer1.x, pursuer1.y, pursuer2.x, pursuer2.y, pursuer3.x, pursuer3.y)
		P_Invisible = Visible.P_Unvisible
		P1_Invisible = Visible.P1_Unvisible
		P2_Invisible = Visible.P2_Unvisible
		P3_Invisible = Visible.P3_Unvisible
###

		E_x_State = np.zeros((SIZE,1))
		E_y_State = np.zeros((SIZE,1))
		P_x_State = np.zeros((SIZE,1))
		P_y_State = np.zeros((SIZE,1))
		P1_x_State = np.zeros((SIZE,1))
		P1_y_State = np.zeros((SIZE,1))
		P2_x_State = np.zeros((SIZE,1))
		P2_y_State = np.zeros((SIZE,1))
		P3_x_State = np.zeros((SIZE,1))
		P3_y_State = np.zeros((SIZE,1))

		Ex_Seen = 0

		E_x_State[evader.x] = 1
		E_y_State[evader.y] = 1

		if P_Invisible == False :
			P_x_State[pursuer.x] = 1
			P_y_State[pursuer.y] = 1
			Ex_Seen += 1

		if P1_Invisible == False :
			P1_x_State[pursuer1.x] = 1
			P1_y_State[pursuer1.y] = 1
			Ex_Seen += 1


		if P2_Invisible == False :
			P2_x_State[pursuer2.x] = 1
			P2_y_State[pursuer2.y] = 1
			Ex_Seen += 1


		if P3_Invisible == False :
			P3_x_State[pursuer3.x] = 1
			P3_y_State[pursuer3.y] = 1
			Ex_Seen += 1


		obs_E = np.append(E_x_State, E_y_State, axis=0)
		obs_P = np.append(P_x_State, P_y_State, axis=0)
		obs_P1 = np.append(P1_x_State, P1_y_State, axis=0)
		obs_P2 = np.append(P2_x_State, P2_y_State, axis=0)
		obs_P3 = np.append(P3_x_State, P3_y_State, axis=0)

		obs_1 = np.append(obs_E, obs_P, axis=0)
		obs_2 = np.append(obs_P1, obs_P2, axis=0)
		obs_3 = np.append(obs_1, obs_2, axis=0)

		observation = np.append(obs_3, obs_P3, axis=0)
		observation = np.transpose(observation)
		

		repulsiveForce = Repulsive(evader.x, evader.y, pursuer.x, pursuer.y, pursuer1.x, pursuer1.y, pursuer2.x, pursuer2.y, pursuer3.x, pursuer3.y, P_Invisible, P1_Invisible, P2_Invisible, P3_Invisible)
		Best_Possible_Action = repulsiveForce.Best_Action
		Best_Obs_Action = repulsiveForce.Best_obs_Action
		Ex_F_Obs_Total = repulsiveForce.F_Obs_Total

### Action Selection

		predict_movement, predict_q_value = deep_q.predict_movement(observation, epsilon)
		pursuers_actions = ChasingPursuers(evader.x, evader.y, pursuer.x, pursuer.y, pursuer1.x, pursuer1.y, pursuer2.x, pursuer2.y, pursuer3.x, pursuer3.y)
		Action_P = pursuers_actions.action_pursuer
		Action_P1 = pursuers_actions.action_pursuer1
		Action_P2 = pursuers_actions.action_pursuer2
		Action_P3 = pursuers_actions.action_pursuer3

###### Action 
		done = False

		evader.action_e(predict_movement)
		pursuer.action_p(Action_P)
		pursuer1.action_p(Action_P1)
		pursuer2.action_p(Action_P2)
		pursuer3.action_p(Action_P3)


		if ((abs(evader.x-pursuer.x) < 2) and (abs(evader.y-pursuer.y) < 2)) or ((abs(evader.x-pursuer1.x) < 2) and (abs(evader.y-pursuer1.y) < 2)) or ((abs(evader.x-pursuer2.x) < 2) and  (abs(evader.y-pursuer2.y) < 2)) or ((abs(evader.x-pursuer3.x) < 2) and (abs(evader.y-pursuer3.y) < 2)) or abs(evader.x-SIZE) < 2 or abs(evader.y-SIZE) < 2 or (evader.x < 1) or (evader.y < 1) or ((25 <= evader.y <= 35) and (14 <= evader.x <= 40)) or ((49 <= evader.y <= 59) and (14 <= evader.x <= 40)) or ((25 <= evader.y <= 59) and (30 <= evader.x <= 40)):

			reward = -ENEMY_PENALTY
			done = True

		evader.action_e(predict_movement)
		pursuer.action_p(Action_P)
		pursuer1.action_p(Action_P1)
		pursuer2.action_p(Action_P2)
		pursuer3.action_p(Action_P3)

		if ((abs(evader.x-pursuer.x) < 2) and (abs(evader.y-pursuer.y) < 2)) or ((abs(evader.x-pursuer1.x) < 2) and (abs(evader.y-pursuer1.y) < 2)) or ((abs(evader.x-pursuer2.x) < 2) and  (abs(evader.y-pursuer2.y) < 2)) or ((abs(evader.x-pursuer3.x) < 2) and (abs(evader.y-pursuer3.y) < 2)) or abs(evader.x-SIZE) < 2 or abs(evader.y-SIZE) < 2 or (evader.x < 1) or (evader.y < 1) or ((25 <= evader.y <= 35) and (14 <= evader.x <= 40)) or ((49 <= evader.y <= 59) and (14 <= evader.x <= 40)) or ((25 <= evader.y <= 59) and (30 <= evader.x <= 40)):

			reward = -ENEMY_PENALTY
			done = True

		evader.action_e(predict_movement)

		if ((abs(evader.x-pursuer.x) < 2) and (abs(evader.y-pursuer.y) < 2)) or ((abs(evader.x-pursuer1.x) < 2) and (abs(evader.y-pursuer1.y) < 2)) or ((abs(evader.x-pursuer2.x) < 2) and  (abs(evader.y-pursuer2.y) < 2)) or ((abs(evader.x-pursuer3.x) < 2) and (abs(evader.y-pursuer3.y) < 2)) or abs(evader.x-SIZE) < 2 or abs(evader.y-SIZE) < 2 or (evader.x < 1) or (evader.y < 1) or ((25 <= evader.y <= 35) and (14 <= evader.x <= 40)) or ((49 <= evader.y <= 59) and (14 <= evader.x <= 40)) or ((25 <= evader.y <= 59) and (30 <= evader.x <= 40)):

			reward = -ENEMY_PENALTY
			done = True


###
		Visible = Eyesight(evader.x, evader.y, pursuer.x, pursuer.y, pursuer1.x, pursuer1.y, pursuer2.x, pursuer2.y, pursuer3.x, pursuer3.y)
		P_Invisible = Visible.P_Unvisible
		P1_Invisible = Visible.P1_Unvisible
		P2_Invisible = Visible.P2_Unvisible
		P3_Invisible = Visible.P3_Unvisible
###

		E_x_State = np.zeros((SIZE,1))
		E_y_State = np.zeros((SIZE,1))
		P_x_State = np.zeros((SIZE,1))
		P_y_State = np.zeros((SIZE,1))
		P1_x_State = np.zeros((SIZE,1))
		P1_y_State = np.zeros((SIZE,1))
		P2_x_State = np.zeros((SIZE,1))
		P2_y_State = np.zeros((SIZE,1))
		P3_x_State = np.zeros((SIZE,1))
		P3_y_State = np.zeros((SIZE,1))


		New_Seen = 0

		E_x_State[evader.x] = 1
		E_y_State[evader.y] = 1

		if P_Invisible == False :
			P_x_State[pursuer.x] = 1
			P_y_State[pursuer.y] = 1
			New_Seen += 1

		if P1_Invisible == False :
			P1_x_State[pursuer1.x] = 1
			P1_y_State[pursuer1.y] = 1
			New_Seen += 1

		if P2_Invisible == False :
			P2_x_State[pursuer2.x] = 1
			P2_y_State[pursuer2.y] = 1
			New_Seen += 1

		if P3_Invisible == False :
			P3_x_State[pursuer3.x] = 1
			P3_y_State[pursuer3.y] = 1
			New_Seen += 1

		obs_E = np.append(E_x_State, E_y_State, axis=0)
		obs_P = np.append(P_x_State, P_y_State, axis=0)
		obs_P1 = np.append(P1_x_State, P1_y_State, axis=0)
		obs_P2 = np.append(P2_x_State, P2_y_State, axis=0)
		obs_P3 = np.append(P3_x_State, P3_y_State, axis=0)

		obs_1 = np.append(obs_E, obs_P, axis=0)
		obs_2 = np.append(obs_P1, obs_P2, axis=0)
		obs_3 = np.append(obs_1, obs_2, axis=0)

		new_observation = np.append(obs_3, obs_P3, axis=0)
		new_observation = np.transpose(new_observation)

		repulsiveForce = Repulsive(evader.x, evader.y, pursuer.x, pursuer.y, pursuer1.x, pursuer1.y, pursuer2.x, pursuer2.y, pursuer3.x, pursuer3.y, P_Invisible, P1_Invisible, P2_Invisible, P3_Invisible)

		New_F_Obs_Total = repulsiveForce.F_Obs_Total


		if done == False:
			reward = MOVE_PENALTY

			if Best_Possible_Action == predict_movement :
				reward += 5

			if (New_F_Obs_Total > Ex_F_Obs_Total):
				if (Ex_F_Obs_Total > 11.40):
					reward += 10
				elif (Ex_F_Obs_Total > 5.30):
					reward += 7
				elif(Ex_F_Obs_Total > 2.70):
					reward += 4
				elif(Ex_F_Obs_Total > 0):
					reward += 2


			if (New_Seen < Ex_Seen):

				if (New_Seen == 0):
					reward += 10
#				elif (New_Seen == 1):
#					reward += seen_reward_2
#				elif (New_Seen == 2):
#					reward += seen_reward_3
#				elif (New_Seen == 3):
#					reward += seen_reward_4




		experience = (observation, predict_movement, reward, done, new_observation)
		replay_buffer.add(observation, predict_movement, reward, done, new_observation)
		episode_reward += reward

		if replay_buffer.size() > MIN_OBSERVATION:
			if observation_num % 128 == 0:
				s_batch, a_batch, r_batch, d_batch, s2_batch = replay_buffer.sample(MINIBATCH_SIZE)
				deep_q.train(s_batch, a_batch, r_batch, d_batch, s2_batch, observation_num)
				deep_q.target_train()

		if observation_num % 50_000 == 9999:
			print("Saving Network")
			deep_q.save_network("model_den2")
			deep_q.save_target_network("targetmodel_den2")
		
		if observation_num >= 40_000 :
			if epsilon > min_epsilon:
				epsilon -= EPS_DECAY
			if (EPS_renew_time > EPS_counter) and (min_epsilon >= epsilon):
				EPS_counter += 1
				epsilon = 1.0


		if observation_num % 10_000 == 0:
			print("Experience number ", observation_num)

		if done:
			break


#	if observation_num % 20_000 == 0:
#		print("We predicted a q value of ", predict_q_value)


#		if not done :
#			if New_Seen < Seen:
#				reward += ENEMY_PENALTY/10
#			if New_Seen == 0:
#				reward += ENEMY_PENALTY
#			else:
#				reward += -MOVE_PENALTY



