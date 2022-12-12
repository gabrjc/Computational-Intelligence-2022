# Computational-Intelligence-2022

## Lab3

#### Made in cooperation with Jacopo Taramasso, S292634


# Task3.1: An agent using fixed rules based on *nim-sum* (i.e., an *expert system*)

After many trials...
It has resulted in some cases how strongly the outcome depends on the first move: for the harder strategies the first move is determinant for the winning of the match because it descriminate the possibilty to leave the board in a safe state. For the dumbest strategy instead, the first move gives only an advantage to the player while for the dumbest strategies the first move gives only an advantage. Randomizing the first move we obtained a fairer match, the strategy does the rest.

## Differents strategy have been tested on 1000 matches played with nim boardes of size 10 per row, these are the outcomes:
    Expert vs optimal => 0.47
    Expert vs random => 0.0
    Expert vs evolve_strategy(p=0.5) => 0.0
    Optimal vs optimal => 0.49
    Optimal vs evolve_strategy(p=0.5) => 1.0
    Pure_random vs evolve_strategy(p=0.1) => 0.47
    Pure_random vs evolve_strategy(p=0.5) => 0.48
    Pure_random vs evolve_strategy(p=0.9) => 0.48


# Task3.2: An agent using evolved rules

A genetic algorithm is applied to the problem, the genome is composed of a list of tuples of policy to follow in order to select the column and the number of elements to remove.

There is also a global variable that allows you to choose whether to apply the "last_condition" policy, i.e. if only one column remains, the algorithm takes it all, thus winning the match.

The performance of the algorithm varies according to the parameters: increasing the number of generations, the offset or the population does not always lead to an improvement in performance.

In general the algorithm is better than both pure_random and the professor's strategy, with a further increase if the "last condition" policy is used.

Unfortunately the algorithm fails to win against the optimal strategy based on nim-sum but this was expected.

### possible future improvements <hr style="border:0.5px solid gray">

To improve the algorithm it is possible to add other policies both for the selection of the column and the number of elements.<br/>
These improvements would be effective if you get a list of policies such as to obtain a version parallel to the nim-sum that allows you to always obtain safe states.



# Task3.3: An agent using minmax

The minmax algorithm has been applied to the problem, the value of each node depends on the nimsum of the child nodes. 
A +1 is then awarded for each safe state in the node's descendants,
the choice of move is therefore made so that the opponent has the least number of safe states in the future.

The evaluations were carried out on a few games due to the large amount of computation involved.
Minmax always beats pure random and professor strategy. it loses to nimsum-based optimal strategy.


### Possible future improvements<hr />
It would be necessary to add some pruning to make the computation lighter and to have the possibility to evaluate deeper trees



# Task3.4: An agent using Reinforcement Learning
The idea of the first strategy has been taken from [wikipedia](https://en.wikipedia.org/wiki/Q-learning) and from this [repo](https://github.com/jakob-manning/nim-bot), using Q-Learning, a model-free reinforcement learning algorithm. 
For any finite Markov decision process (FMDP), Q-learning finds an optimal policy in the sense of maximizing the expected value of the total reward over any and all successive steps, starting from the current state.
Q-learning can identify an optimal action-selection policy for any given FMDP

A dictionary Q is iniazilized to maps the tuple (state, action) to q-values (numbers); the q-learning model updates itself receiving the old state, the action referred to that state, the new resulting state and the reward linked to the action taken. 
Nim game is trained against itself for a given number of matches to return the reinforced agent we wanted.

The Q-value used (taken from wikipedia):
<br>Q (state,action) = previous Q value + alpha_learning_rate * (new value estimate - olq Q value)
( with new value estimate that is the current reward + the future reward estimation )

The second strategy is taken indeed from the Maze project given from the professors, Nim games has been adapted to work with the Maze functions. In particular we had to convert the rows to tuples <code>(tuple(state._rows)</code>, and adapt the exploitation of the cook function from the previous tasks. 



### Possible future improvements <hr />
Surely the most evident problem is the lackness of a big number of training trials, the two models have been resulted very sensitive to changing the hyperparameter like alpha and random_factor. Increasing the NIM_SIZE value, computational time explodes!



