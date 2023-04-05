# Rock-Paper-Scissors-with-Q-learning
This is the first version of a Python implementation of the classic game of Rock-Paper-Scissors using the Q-learning algorithm. The Q-learning algorithm is a reinforcement learning technique that learns an optimal policy for an agent by estimating the expected rewards for each state-action pair.

# What it does
This program allows the user to train an agent to play Rock-Paper-Scissors against a randomly choosing opponent using the Q-learning algorithm. After training, the agent can play the game against a human player.

# How it works
The program starts by initializing the Q-table, which is a dictionary that stores the Q-values for each state-action pair. The Q-values represent the expected reward for each action in each state, which the agent uses to choose the best action.

During training, the agent updates the Q-table based on the rewards obtained from each action taken in each state. The exploration rate controls the balance between exploration and exploitation, i.e., whether to take a random action or the action with the highest Q-value.

After training, the agent can play the game against a human player. The agent chooses its action based on the Q-values in the Q-table, and the human player chooses their action via input. The game continues until one player wins or the game is tied. The agent updates the Q-table after each game, and the exploration rate may be decayed over time to reduce exploration.

# Usage
To use this program, simply run the RockPaperScissors.py file in a Python environment.

Copy code
```
$ python RockPaperScissors.py
```
The program will start by training the agent for a set number of episodes. After training, the program will prompt the user to play the game against the agent. To choose an action, enter a number corresponding to Rock (0), Paper (1), or Scissors (2).

# Future Updates
This is the first version of the program, and it still needs to undergo major updates.
- More updates soon
