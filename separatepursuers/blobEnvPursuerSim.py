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
from deep_Q_pursuer import DeepQ
from deep_Q_pursuer import DeepQ_1
from repulsivePursuer import Repulsive


REPLAY_MEMORY_SIZE = 50_000  # How many last steps to keep for model training
MIN_OBSERVATION = 40_000  # Minimum number of steps in a memory to start training
MINIBATCH_SIZE = 128  # How many steps (samples) to use for training


EPISODES = 1_000_000

# Exploration settings
epsilon_evader = 0
epsilon = 0
min_epsilon = 0.05
check_epsilon = 0
EPS_DECAY = 0.00002
EPS_renew_time = 14
EPS_counter = 0


SIZE = 84
MOVE_PENALTY = 1
ENEMY_PENALTY = 300
PLAYER_N = 1  # player key in dict
ENEMY_N = 2  # enemy key in dict
PLAYER_N_Trained = 3  # player key in dict
d = {1: (255, 175, 0),
       2: (0, 0, 255),
       3: (0, 255, 0)}


replay_buffer = ReplayBuffer(REPLAY_MEMORY_SIZE)
deep_q = DeepQ()
deep_q_evader = DeepQ_1()

observation_num = 0


deep_q_evader.trained_model("targetmodel_v5")
deep_q.trained_model("targetmodel_pursuer_1")

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



		if P_Invisible == False :

			E_x_State[evader.x] = 1
			E_y_State[evader.y] = 1

		
		P_x_State[pursuer.x] = 1
		P_y_State[pursuer.y] = 1


		P1_x_State[pursuer1.x] = 1
		P1_y_State[pursuer1.y] = 1



		P2_x_State[pursuer2.x] = 1
		P2_y_State[pursuer2.y] = 1



		P3_x_State[pursuer3.x] = 1
		P3_y_State[pursuer3.y] = 1



		obs_E = np.append(E_x_State, E_y_State, axis=0)
		obs_P = np.append(P_x_State, P_y_State, axis=0)
		obs_P1 = np.append(P1_x_State, P1_y_State, axis=0)
		obs_P2 = np.append(P2_x_State, P2_y_State, axis=0)
		obs_P3 = np.append(P3_x_State, P3_y_State, axis=0)

		obs_1 = np.append(obs_E, obs_P, axis=0)
		obs_2 = np.append(obs_P1, obs_P2, axis=0)
		obs_3 = np.append(obs_1, obs_2, axis=0)

		observation_evader = np.append(obs_3, obs_P3, axis=0)
		observation_evader = np.transpose(observation_evader)



		obs_E = np.append(E_x_State, E_y_State, axis=0)
		obs_P = np.append(P_x_State, P_y_State, axis=0)
		observation = np.append(obs_E, obs_P, axis=0)
		observation = np.transpose(observation)
		

		repulsiveForce = Repulsive(evader.x, evader.y, pursuer.x, pursuer.y, pursuer1.x, pursuer1.y, pursuer2.x, pursuer2.y, pursuer3.x, pursuer3.y, P_Invisible, P1_Invisible, P2_Invisible, P3_Invisible)
		Best_Possible_Action = repulsiveForce.Best_Action
		Best_Obs_Action = repulsiveForce.Best_obs_Action
		Ex_F_Obs_Total = repulsiveForce.F_Obs_Total

### Action Selection

		predict_movement_evader, predict_q_value_evader = deep_q_evader.predict_movement(observation_evader, epsilon_evader)

		predict_movement, predict_q_value = deep_q.predict_movement(observation, epsilon)

		pursuers_actions = ChasingPursuers(evader.x, evader.y, pursuer.x, pursuer.y, pursuer1.x, pursuer1.y, pursuer2.x, pursuer2.y, pursuer3.x, pursuer3.y)
		Action_P1 = pursuers_actions.action_pursuer1
		Action_P2 = pursuers_actions.action_pursuer2
		Action_P3 = pursuers_actions.action_pursuer3
###### Action 

		done = False

		evader.action_e(predict_movement_evader)
		pursuer.action_p(predict_movement)
		pursuer1.action_p(Action_P1)
		pursuer2.action_p(Action_P2)
		pursuer3.action_p(Action_P3)

		if ((abs(evader.x-pursuer.x) < 2) and (abs(evader.y-pursuer.y) < 2)):

			reward = ENEMY_PENALTY
			done = True

		if ((abs(pursuer.x-pursuer1.x) < 2) and (abs(pursuer.y-pursuer1.y) < 2)) or ((abs(pursuer.x-pursuer2.x) < 2) and  (abs(pursuer.y-pursuer2.y) < 2)) or ((abs(pursuer.x-pursuer3.x) < 2) and (abs(pursuer.y-pursuer3.y) < 2)) or abs(pursuer.x-SIZE) < 2 or abs(pursuer.y-SIZE) < 2 or (pursuer.x < 1) or (pursuer.y < 1) or ((25 <= pursuer.y <= 35) and (14 <= pursuer.x <= 40)) or ((49 <= pursuer.y <= 59) and (14 <= pursuer.x <= 40)) or ((25 <= pursuer.y <= 59) and (30 <= pursuer.x <= 40)):

			reward = -ENEMY_PENALTY
			done = True

		if ((abs(evader.x-pursuer.x) < 2) and (abs(evader.y-pursuer.y) < 2)) or ((abs(evader.x-pursuer1.x) < 2) and (abs(evader.y-pursuer1.y) < 2)) or ((abs(evader.x-pursuer2.x) < 2) and  (abs(evader.y-pursuer2.y) < 2)) or ((abs(evader.x-pursuer3.x) < 2) and (abs(evader.y-pursuer3.y) < 2)) or abs(evader.x-SIZE) < 2 or abs(evader.y-SIZE) < 2 or (evader.x < 1) or (evader.y < 1) or ((25 <= evader.y <= 35) and (14 <= evader.x <= 40)) or ((49 <= evader.y <= 59) and (14 <= evader.x <= 40)) or ((25 <= evader.y <= 59) and (30 <= evader.x <= 40)):

			done = True

		evader.action_e(predict_movement_evader)
		pursuer.action_p(predict_movement)
		pursuer1.action_p(Action_P1)
		pursuer2.action_p(Action_P2)
		pursuer3.action_p(Action_P3)



		if ((abs(evader.x-pursuer.x) < 2) and (abs(evader.y-pursuer.y) < 2)):

			reward = ENEMY_PENALTY
			done = True

		if ((abs(pursuer.x-pursuer1.x) < 2) and (abs(pursuer.y-pursuer1.y) < 2)) or ((abs(pursuer.x-pursuer2.x) < 2) and  (abs(pursuer.y-pursuer2.y) < 2)) or ((abs(pursuer.x-pursuer3.x) < 2) and (abs(pursuer.y-pursuer3.y) < 2)) or abs(pursuer.x-SIZE) < 2 or abs(pursuer.y-SIZE) < 2 or (pursuer.x < 1) or (pursuer.y < 1) or ((25 <= pursuer.y <= 35) and (14 <= pursuer.x <= 40)) or ((49 <= pursuer.y <= 59) and (14 <= pursuer.x <= 40)) or ((25 <= pursuer.y <= 59) and (30 <= pursuer.x <= 40)):

			reward = -ENEMY_PENALTY
			done = True

		if ((abs(evader.x-pursuer.x) < 2) and (abs(evader.y-pursuer.y) < 2)) or ((abs(evader.x-pursuer1.x) < 2) and (abs(evader.y-pursuer1.y) < 2)) or ((abs(evader.x-pursuer2.x) < 2) and  (abs(evader.y-pursuer2.y) < 2)) or ((abs(evader.x-pursuer3.x) < 2) and (abs(evader.y-pursuer3.y) < 2)) or abs(evader.x-SIZE) < 2 or abs(evader.y-SIZE) < 2 or (evader.x < 1) or (evader.y < 1) or ((25 <= evader.y <= 35) and (14 <= evader.x <= 40)) or ((49 <= evader.y <= 59) and (14 <= evader.x <= 40)) or ((25 <= evader.y <= 59) and (30 <= evader.x <= 40)):

			done = True



		evader.action_e(predict_movement_evader)


		if ((abs(evader.x-pursuer.x) < 2) and (abs(evader.y-pursuer.y) < 2)) or ((abs(evader.x-pursuer1.x) < 2) and (abs(evader.y-pursuer1.y) < 2)) or ((abs(evader.x-pursuer2.x) < 2) and  (abs(evader.y-pursuer2.y) < 2)) or ((abs(evader.x-pursuer3.x) < 2) and (abs(evader.y-pursuer3.y) < 2)) or abs(evader.x-SIZE) < 2 or abs(evader.y-SIZE) < 2 or (evader.x < 1) or (evader.y < 1) or ((25 <= evader.y <= 35) and (14 <= evader.x <= 40)) or ((49 <= evader.y <= 59) and (14 <= evader.x <= 40)) or ((25 <= evader.y <= 59) and (30 <= evader.x <= 40)):

			done = True




		env = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)
		env = cv2.rectangle(env,(26,15),(34,39),(255,255,255),-1)
		env = cv2.rectangle(env,(34,31),(50,39),(255,255,255),-1)
		env = cv2.rectangle(env,(50,15),(58,39),(255,255,255),-1)
		env[evader.x][evader.y] = d[ENEMY_N]  
		env[pursuer.x][pursuer.y] = d[PLAYER_N_Trained]
		env[pursuer1.x][pursuer1.y] = d[PLAYER_N]
		env[pursuer2.x][pursuer2.y] = d[PLAYER_N]
		env[pursuer3.x][pursuer3.y] = d[PLAYER_N]
		img = Image.fromarray(env, 'RGB') 
		img = img.resize((1000, 600)) 
		cv2.imshow("image", np.array(img))
		cv2.waitKey(100)

		observation_num += 1

		if done:
			break

