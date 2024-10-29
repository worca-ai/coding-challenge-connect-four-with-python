# Coding Challenge - Connect Four with Python

## Instructions:
- The challenge should take about two hours to complete.
- Please use Python 3.11 or later.
- Give careful thought to your code organization and algorithms, and treat it similar to how
you would write production code. We value good engineering practices and efficiency, as
well as correctness.
- The code must be functional, and we appreciate you adding some code in addition to the
core logic to make it easier for us to run and test.

## Requirements
You are creating the game Connect Four. There are two players, and each of the players takes
turns trying to get four of their game pieces in a row. For this interview, your job is to implement
the core functionalities to support two-player Connect Four matchups. The code should be
functioning, and you should follow good engineering practices.

1. Write a functional subset of the code for the game board, game pieces, and player state.
Your code should include a function to print out the board in ASCII. For example, here is a
plausible printout after two turns--one from player 'x' and one from player 'o'.
```
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* x o * * * *
```
Note that although the classic version of Connect Four has 7 columns and 6 rows, our
game might be played on a board of an arbitrary size.

2. Write functions that enable each player to place a new piece onto the board, and that
check whether one of the players has won the game.
You do not need to worry about collecting input from the players. You may assume that the
arguments to all functions/methods have been gathered from the appropriate input device.
