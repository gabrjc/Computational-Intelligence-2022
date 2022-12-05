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

## possible future improvements

To improve the algorithm it is possible to add other policies both for the selection of the column and the number of elements.

These improvements would be effective if you get a list of policies such as to obtain a version parallel to the nim-sum that allows you to always obtain safe states.
