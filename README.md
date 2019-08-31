# Laser-Checkmate
Laser Checkmate is an adversarial board game in which two players take turns to place laser emitters in a square grid, to cover maximum blocks in their laser's range.

# GOAL: 
Its Simple! The more blocks in your range, the more points you get, and YOU WIN!

# RULES:
1. Each laser's beam penetrates in each direction, UP, DOWN, LEFT, RIGHT,and All four diagonals.
2. The range of the Lasers get blocked by walls(edges of the grid) and Towers(occupying random place in the grid).
3. You can place lasers only in an empty block.
4. Your laser's range can intersect with other laser's range, and you do get points for that!
5. The game terminates when there are no valid moves left.

# TRICK:
The laser has range of upto 3 blocks only!

# POINTS:
You get 1 point for each laser's beam. 2 points for the laser itself.

# VALID-MOVE:
A player places the laser in the block that contains no laser emitter, wall or tower and that is not covered by any laser(from either player).

# INPUT:
1. Line 1: Size of the square grid(N).
2. Line 2 to end: an N* N grid with -1s to 3s.
- 0 = Empty Block. 
- 1 = Player 1's laser emitter.
- 2 = Player 2's laser emitter.
- 3 = Towers.
- -1 = To represent the range of the laser emitters.

# OUTPUT:
A single move, the position where you will place your laser, in (x,y) co-ordinates format.

# LOGIC:
ATTEMPT #1: The Simple and Elegant backtracking solution.

1. You place a laser emitter in the very first available block.
2. Rule out all the places where the opponent might place their lasers.
3. Create all the branches where the opponent can place their lasers.
4. Keep track of the scores for each player as you go down the path!
5. When you reach a state where the grid is packed and you don't have any valid moves left, Check the scores.
    If your score is greater than the opponents, go back to the root of the tree and you have your best move!
    
Why this solution will fail?
This solution works perfectly fine for smaller grids of upto 5*5.
Consider a grid of 25*25 with very tight constraints, the algorithm has to check 25! possible solutions and pick the first best one.


ATTEMPT #2: If depth of the tree causes the problem, lets cut down the tree!

1. You can select a specific number of depth for which the algorithm will create a tree.
2. At that depth, in any of the possible path, if your score is greater than the opponent's, choose that possible move.

Why this solution will fail?
What if you reach that certain depth and you select the move which seems best at the moment but ultimately makes you lose? 
What is the correct depth? If you select a small number to cut down the number of paths, you are taking a decision too soon. If you select a big number, are you really working on reducing the time to retrieve THE move?


ATTEMPT #3: Alpha-beta pruning.
This seems like a nice idea! What if I stop looking at the path, the moment I realise I am losing?

1. Apply alpha beta pruning to the main backtracking logic.

Yes! it will reduce the time significantly! So much so that even a grid of size 15* 15 with very tight constraints, will give you the best move under 60 seconds!

