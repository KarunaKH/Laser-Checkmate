# Laser-Checkmate
Laser Checkmate is an adversarial board game in which two players take turns to place laser emitters in a square grid, to cover maximum blocks in their laser's range.

GOAL: Its Simple! The more blocks in your range, the more points you get, and YOU WIN!

RULES:
1. Each laser's beam penetrates in each direction, UP, DOWN, LEFT, RIGHT,and All four diagonals.
2. The range of the Lasers get blocked by walls(edges of the grid) and Towers(occupying random place in the grid).
3. You can place lasers only in an empty block.
4. Your laser's range can intersect with other laser's range, and you do get points for that!
5. The game terminates when there are no valid moves left.

TRICK: The laser has range of upto 3 blocks only!

POINTS: You get 1 point for each laser's beam. 2 points for the laser itself.

VALID MOVE: A player places the laser in the block that contains no laser emitter, wall or tower and that is not covered by any laser(from either player).

INPUT:
Line 1: Size of the square grid(N).
Line 2 to end: an N* N grid with 0s, 1s, 2s and 3s.
0 - Empty Block. 
1 - Player 1's laser emitter.
2 - Player 2's laser emitter.
3 - Towers
-1 - To represent the range of the laser emitters.

OUTPUT: A single move, the position where you will place your laser, in (x,y) co-ordinates format.



