import gym
import numpy as np

from screencapture.py import capture_screen, preprocess_image, game_window
class MapleStoryEnv(gym.Env):
    def __init__(self):
        super(MapleStoryEnv, self).__init__()

        self.action_space = gym.spaces.Discrete(4)  # Define your action space (e.g., 4 actions)
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(84, 84), dtype=np.float32)  # Define the observation space (e.g., 84x84 preprocessed images)

    def step(self, action):
        # Simulate taking the action in the game (e.g., using PyAutoGUI)
        # Get the new game state, reward, and done status
        # (Replace this comment with your code to interact with the game and get the new state, reward, and done status)
        new_game_screen = capture_screen(game_window)
        new_state = preprocess_image(new_game_screen)
        new_state = np.zeros((84, 84))  # Replace with the actual new state (preprocessed image)
        reward = calculate_reward(previous_state, self.current_state)  # Replace with the actual reward
        done = False  # Replace with the actual done status

        return new_state, reward, done, {}

    def reset(self):
        # Reset the game to its initial state
        # (Replace this comment with your code to reset the game)
        game_screen = capture_screen(game_window)
        initial_state = preprocess_image(game_screen)
        initial_state = np.zeros((84, 84))  # Replace with the actual initial state (preprocessed image)
        return initial_state
    
    def render(self, mode='human'):
        pass  # You can implement a rendering method if needed

    def close(self):
        pass  # You can implement a close method if needed


def calculate_reward(previous_state, current_state):
    # Weights for different reward components
    exp_weight = 1.0
    hp_potion_weight = 0.5
    mp_potion_weight = 0.5
    death_penalty_weight = -10.0

    # Experience gain
    previous_exp = previous_state['experience']
    current_exp = current_state['experience']
    exp_reward = (current_exp - previous_exp) * exp_weight

    # HP/MP potion management
    previous_hp_potions = previous_state['hp_potions']
    current_hp_potions = current_state['hp_potions']
    hp_potion_reward = (previous_hp_potions - current_hp_potions) * hp_potion_weight

    previous_mp_potions = previous_state['mp_potions']
    current_mp_potions = current_state['mp_potions']
    mp_potion_reward = (previous_mp_potions - current_mp_potions) * mp_potion_weight

    # Death penalty
    previous_lives = previous_state['lives']
    current_lives = current_state['lives']
    death_penalty = (previous_lives - current_lives) * death_penalty_weight

    # Total reward
    total_reward = exp_reward + hp_potion_reward + mp_potion_reward + death_penalty

    return total_reward
