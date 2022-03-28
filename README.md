# Number Tower Game
Welcome to Number Tower!

Number Tower is a fun math game.
Swap and stack the numbered bricks from lowest to highest.

## How to play
- You are going to build a tower using bricks numbered from 1 to 60.
- Arrange 10 bricks in your tower from lowest to highest.
- You are playing with the computer. The first player to get their 10 bricks in order wins.
- In each turn you can choose to pick up the top brick from the discard pile or to pick up the top brick from the main pile.
- Once you choose a brick, you can decide which brick in the tower to replace with the new brick.

## Sample Output
You can see how the game play goes on sample_output.txt.

Here is a digest version of the output:
```
Press any key to start!: s

Computer's tower: [36, 10, 38, 15, 6, 2, 13, 54, 35, 26]
Your tower:	      [5, 28, 57, 51, 17, 11, 25, 8, 37, 20]

COMPUTER'S TURN
The computer picked 14 from the discard pile.
The computer replaced a brick.

NOW IT'S YOUR TURN!
Your tower:	      [5, 28, 57, 51, 17, 11, 25, 8, 37, 20]
The top brick on the discard pile is 38
Type 'D' to take the discard brick, 'M' for a mystery brick, or 'H' for help: h
-----help-----
Type 'D' to use the top brick of the discard pile.
Type 'M' to check the top brick from the main pile and see if that brick is useful to you.
You can also discard the main brick and skipp the turn if the top brick is not useful to you.
--------------
Type 'D' to take the discard brick, 'M' for a mystery brick, or 'H' for help: d
Where do you want to place this brick? Type a brick number to replace in your tower: 25
You replaced 25 with 38.
Your tower:	      [5, 28, 57, 51, 17, 11, 38, 8, 37, 20]

COMPUTER'S TURN
The computer picked 25 from the discard pile.
The computer replaced a brick.

NOW IT'S YOUR TURN!
Your tower:	      [5, 28, 57, 51, 17, 11, 38, 8, 37, 20]
The top brick on the discard pile is 6
Type 'D' to take the discard brick, 'M' for a mystery brick, or 'H' for help: d
Where do you want to place this brick? Type a brick number to replace in your tower: 6
Brick not found in the tower. Try again.
Where do you want to place this brick? Type a brick number to replace in your tower: 28
You replaced 28 with 6.
Your tower:	      [5, 6, 57, 51, 17, 11, 38, 8, 37, 20]

COMPUTER'S TURN
The computer picked from the main pile.
The computer replaced a brick.

...

NOW IT'S YOUR TURN!
Your tower:	      [5, 6, 15, 26, 30, 36, 38, 8, 52, 60]
The top brick on the discard pile is 13
Type 'D' to take the discard brick, 'M' for a mystery brick, or 'H' for help: m
You picked 49 from main pile.
Do you want to use this brick? Type 'Y' or 'N' to skip turn: y
Where do you want to place this brick? Type a brick number to replace in your tower: 8
You replaced 8 with 49.
Your tower:	      [5, 6, 15, 26, 30, 36, 38, 49, 52, 60]

Congrats! You won!
Computer's tower: [3, 10, 14, 22, 25, 31, 37, 54, 51, 57]
Your tower:	      [5, 6, 15, 26, 30, 36, 38, 49, 52, 60]
There were 10 turns made in this game.

Do you want to play again? Type 'Y' to play again or 'N' to finish: 

```
