import gym
from gym import spaces
import numpy as np


def b(boolean):
    return 1 if boolean else 0


class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self, graph, nb_cops):
        super(CustomEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        self.reset(graph, nb_cops)

    def step(self, action):
        if self.first_turn:
            self.graph.set_cr(action, self.cops_turn)
        else:
          pos_tuples = np.nonzero(self.graph._attr)

        self.cops_turn = not self.cops_turn
        if not self.cops_turn and self.first_turn:
            self.first_turn = False

    def reset(self, graph=None, nb_cops=None):
        if graph is None:
            self.graph = graph
        else:
            self.graph = graph

        if nb_cops is None:
            self.nb_cops = nb_cops
        else:
            self.nb_cops = nb_cops

        # Initially, cops & robbers can choose position, so space is basically all the graph
        self.action_space = spaces.Box(0, self.graph.nb_nodes, shape=(self.nb_cops,), dtype=int)
        self.observation_space = spaces.Discrete(self.graph.nb_nodes)
        self.cops_turn = True
        self.first_turn = True

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        ...
