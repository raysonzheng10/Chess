# Chess
#### Video Demo : https://youtu.be/3DtHWmpQeo0
#### Description:
Implementation of Chess with Pygame (CS50X Final Project)

#### Usage
In order to play, you must first have installed pygame via pip install. Afterwards, you simply run the code and the chessboard will appear in a 800x800 pixel display. There isn't support for undoing moves or saving/loading previous games. To play again, you have to exit and run the code again, which will create a new board with all the pieces in their starting positions.


#### Gameplay
This code works as a fully functional chessboard, with support for castling, limited promotions, pins, checks, and checkmates. Some notable features missing are underpromotion and en passante. Pawn promotions work but are limited to queen promotions. When a pawn reaches the back rank, it automatically becomes a queen. 

The game also does not support draws. There is no option to opt for a draw and the game is unable to detect when a stalemate has occured (whether via insufficient materials, no moves left to play, or repeated moves). 

 Asides from the already mentioned issues, the code plays like a normal game of chess.


#### Technologies Used
- Python
- Pygame
- All images and SFX imported