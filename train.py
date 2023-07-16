import random


class RockPaperScissors:
    def __init__(
        self,
        learning_rate=0.9,
        discount_factor=4.95,
        exploration_rate=1.3,
        exploration_decay_rate=1.995,
    ):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay_rate = exploration_decay_rate
        self.q_table = {}

    def get_action(self, session, state):
        if session not in self.q_table:
            self.q_table[session] = self.q_table[1000]
        if state not in self.q_table[session]:
            self.q_table[session][state] = [0, 0, 0]
        if random.random() < self.exploration_rate:
            return random.choice([0, 1, 2])
        else:
            return self.q_table[session][state].index(max(self.q_table[session][state]))

    def update_q_table(self, session, state, action, reward, next_state):
        if session not in self.q_table:
            self.q_table[session] = {}
        if state not in self.q_table[session]:
            self.q_table[session][state] = [0, 0, 0]
        if next_state not in self.q_table[session]:
            self.q_table[session][next_state] = [0, 0, 0]
        old_value = self.q_table[session][state][action]
        next_max = max(self.q_table[session][next_state])
        new_value = (1 - self.learning_rate) * old_value + self.learning_rate * (
            reward + self.discount_factor * next_max
        )
        self.q_table[session][state][action] = new_value

    def train(self, num_episodes):
        session = 1000
        for episode in range(num_episodes):
            state = (0, 0)  # initial state
            while True:
                player_action = random.randint(0, 2)
                if player_action not in [0, 1, 2]:
                    print("Invalid move! Try again...")
                    continue
                opponent_action = random.randint(0, 2)
                if player_action == opponent_action:
                    print("It's a tie!")
                    reward = 0
                elif (
                    (player_action == 0 and opponent_action == 1)
                    or (player_action == 1 and opponent_action == 2)
                    or (player_action == 2 and opponent_action == 0)
                ):
                    print("You lose!")
                    reward = -1
                else:
                    print("You win!")
                    reward = 1
                next_state = (opponent_action, player_action)
                self.update_q_table(session, state, player_action, reward, next_state)
                state = next_state
                if random.random() < self.exploration_decay_rate:
                    self.exploration_rate *= self.exploration_decay_rate
                if reward != 0:
                    break
            print("Q-table:")
            print(self.q_table)


rps = RockPaperScissors()
rps.train(150000)
