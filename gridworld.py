import numpy as np

from environment import GridworldEnvironment
from simulator import GridworldSimulator
from mdp import MDP

grid = np.array([
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 'D', 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 'S', 0, 1],
])
Pe = 0.3
initial_state = (0, 2)

gridworld_environment = GridworldEnvironment(grid, Pe)

gridworld_mdp = MDP(gridworld_environment)
gridworld_policy = gridworld_mdp.value_iteration(0.01, 0.5)
# gridworld_policy = gridworld_mdp.policy_iteration(0.01, 0.5)

gridworld_simulator = GridworldSimulator(gridworld_environment, initial_state)
gridworld_simulator.run_policy(gridworld_policy)