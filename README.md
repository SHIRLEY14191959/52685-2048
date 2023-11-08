# 2048 Game
A simple implementation of the 2048 game using the Pygame library.

## Overview
This game consists of a 4x4 grid where players combine tiles by sliding them to the left, right, up, or down. The goal is to combine tiles until you create a tile with the number 2048.

## Setup
Dependencies: This game requires pygame. If you haven't installed it, you can do so with:

bash
Copy code
```
pip install pygame
```
Clone or download this repository and run the provided script.

## How to Play
Start the Game: Execute the python script.
Controls: Use the arrow keys (↑, ↓, ←, →) to move the tiles.
Objective: Try to combine tiles with the same numbers. Every time you make a move, a new tile (either a 2 or a 4) appears on the board. Keep combining them to reach the 2048 tile!
Features
Colors: Tiles are color-coded based on their number, which helps to quickly identify the higher valued tiles.
Game Over Check: The game checks if there are any valid moves left. If not, it signifies the end of the game.
Game Logic
The core logic of the game revolves around the move() function, which takes care of the sliding and merging of the tiles based on the direction given (left, right, up, or down). Post every move, the game generates a new tile in a random empty spot on the grid.

## Future Enhancements
While the core gameplay is implemented, there's always room for improvement:

### Implement a scoring system.
Show a "Game Over" message when no moves are left.
Add animations for smoother tile movements.
Implement a start menu and an end screen.

## Feedback & Contributions
Your feedback is always welcome! If you have suggestions or find bugs, please report them. Contributions to improve or add new features to the game are also appreciated.

Happy gaming! 🎮