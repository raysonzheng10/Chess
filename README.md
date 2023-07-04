# Chess
#### Video Demo : https://youtu.be/eVCar5PABAY
#### Description:
This was created as my final project for Harvard's CS50 course. It's a recreation of chess, created in python using the pygame library. The game runs on pygame's display with a clock speed of 30 to detect player clicks. The game's board is represented and processed through a _Board_ class, that stores the board as a 8x8 matrix with each square being an instance of a separate _Tile_ class. The _Board_ and _Tile_ are located in board.py.

The _Tile_ class contains information on what piece is on it, with each piece having its own class (all of these classes are in movement.py). I changed these classes and functions a lot, and this is what I settled on in the end.

The largest obstacles that I faced usually stemmed from how the classes were structured. I had to rewrite a lot of code because I wasn't able to make certain classes work together and how I would go about processing the movements in the 8x8 matrix and how that would translate properly onto the board that was displayed.

I'd initially wanted to create a AI bot to play against after implementing chess but that's something for me to tackle in the future. I've learned a lot about python's object-oriented coding and also how I can use that to my advantage.

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