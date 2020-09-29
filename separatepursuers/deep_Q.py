import gym
import numpy as np
import random
import keras
import cv2
from replay_buffer import ReplayBuffer
from keras.models import load_model, Sequential
from keras.layers.convolutional import Convolution2D
from keras.optimizers import Adam
from keras.layers.core import Activation, Dropout, Flatten, Dense, Reshape
from keras.layers.embeddings import Embedding


import tensorflow as tf
import keras.backend.tensorflow_backend as backend

# List of hyper-parameters and constants
DECAY_RATE = 0.99
BUFFER_SIZE = 40_000
MINIBATCH_SIZE = 128
TOT_FRAME = 3_000_000
EPSILON_DECAY = 1_000_000
MIN_OBSERVATION = 5_000
FINAL_EPSILON = 0.05
INITIAL_EPSILON = 0.1
NUM_ACTIONS = 5
TAU = 0.01
# Number of frames to throw into network
NUM_FRAMES = 3


config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)



with tf.device('/gpu:0'):
	class DeepQ(object):
		"""Constructs the desired deep q learning network"""
		def __init__(self):
			self.construct_q_network()


		def construct_q_network(self):
        # Uses the network architecture found in DeepMind paper


			self.model = Sequential()
			self.model.add(Dense(1400, input_shape=(840,), activation='relu'))
			self.model.add(Dense(1400, activation='relu'))
			self.model.add(Dense(1400, activation='relu'))
			self.model.add(Dense(1400, activation='relu'))
			self.model.add(Dense(1400, activation='relu'))
			self.model.add(Dense(1400, activation='relu'))
			self.model.add(Dense(1400, activation='relu'))
			self.model.add(Dense(NUM_ACTIONS, activation='linear'))
			self.model.compile(loss='mse', optimizer=Adam(lr=0.00001))

        # Creates a target network as described in DeepMind paper

			self.target_model = Sequential()
			self.target_model.add(Dense(1400, input_shape=(840,), activation='relu'))
			self.target_model.add(Dense(1400, activation='relu'))
			self.target_model.add(Dense(1400, activation='relu'))
			self.target_model.add(Dense(1400, activation='relu'))
			self.target_model.add(Dense(1400, activation='relu'))
			self.target_model.add(Dense(1400, activation='relu'))
			self.target_model.add(Dense(1400, activation='relu'))
			self.target_model.add(Dense(NUM_ACTIONS, activation='linear'))
			self.target_model.compile(loss='mse', optimizer=Adam(lr=0.00001))
			self.target_model.set_weights(self.model.get_weights())

		def predict_movement(self, observation, epsilon):
			"""Predict movement of game controler where is epsilon
        probability randomly move."""
			q_actions = self.model.predict(observation)
			opt_policy = np.argmax(q_actions)
			rand_val = np.random.random()
			if rand_val < epsilon:
 				opt_policy = np.random.randint(0, NUM_ACTIONS)
 				#print(opt_policy)

			return opt_policy, q_actions[0, opt_policy]

		def train(self, s_batch, a_batch, r_batch, d_batch, s2_batch, observation_num):
			"""Trains network to fit given parameters"""
			batch_size = s_batch.shape[0]
			targets = np.zeros((batch_size, NUM_ACTIONS))

			for i in range(batch_size):
				targets = self.model.predict(s_batch[i])
				fut_action = self.target_model.predict(s2_batch[i])
				targets = np.transpose(targets)
				targets[a_batch[i]] = r_batch[i]
				
				if d_batch[i] == False:
					targets[a_batch[i]] += DECAY_RATE * np.max(fut_action)
 	
				targets = np.transpose(targets)

				loss = self.model.train_on_batch(s_batch[i], targets)
				

        # Print the loss every 10 iterations.
			if observation_num  == -1:
				print("We had a loss equal to ", loss)

		def save_network(self, path):
        # Saves model at specified path 
			self.model.save(path)
			print("Successfully saved network.")

		def save_target_network(self, path):
        # Saves model at specified path 
			self.target_model.save(path)
			print("Successfully saved network.")

		def load_network(self, path):
			self.model = load_model(path)
			print("Succesfully loaded network.")

		def target_train(self):
			model_weights = self.model.get_weights()
			target_model_weights = self.target_model.get_weights()
			for i in range(len(model_weights)):
				target_model_weights[i] = TAU * model_weights[i] + (1 - TAU) * target_model_weights[i]
			self.target_model.set_weights(target_model_weights)



		def trained_model(self, path):

			self.model_1 = load_model(path)
			print("Succesfully loaded network.")

			model_1_weights = self.model_1.get_weights()
			for i in range(len(model_1_weights)):
				model_1_weights[i] = model_1_weights[i]
			self.model.set_weights(model_1_weights)

		def trained_model_1(self, path):

			self.model_1 = load_model(path)
			print("Succesfully loaded network.")

			model_1_weights = self.model_1.get_weights()
			for i in range(len(model_1_weights)):
				model_1_weights[i] = model_1_weights[i]
			self.target_model.set_weights(model_1_weights)
