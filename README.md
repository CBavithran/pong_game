# Pong Game

A simple Pong Game implemented using Python's `turtle` module. This game involves two paddles and a ball, where players compete to score points by preventing the ball from going out of bounds.

---

## Features
- Two-player functionality
- Ball bounces off walls and paddles
- Scoreboard to keep track of points
- Gradually increasing difficulty as ball speed increases with time

---

## How to Run
1. **Ensure Python is installed**: This game is written in Python. You need Python 3.x installed on your system.
2. **Install Dependencies**: The game uses the built-in `turtle` module, which comes pre-installed with Python.
3. **Run the Game**:
   - Copy all the code into a single folder, saving each class (Paddle, Ball, Score_board) as separate `.py` files:
     - `main.py` for the game logic
     - `paddle.py` for the paddle class
     - `ball.py` for the ball class
     - `score_board.py` for the scoreboard class
   - Execute the `main.py` script:
     ```bash
     python main.py
     ```

---

## Controls
### Right Paddle (Player 1)
- **Up Arrow (`↑`)**: Move paddle up
- **Down Arrow (`↓`)**: Move paddle down

### Left Paddle (Player 2)
- **W Key (`w`)**: Move paddle up
- **S Key (`s`)**: Move paddle down

---

## Game Rules
1. Players use their respective paddles to prevent the ball from passing their side.
2. The ball bounces off walls and paddles.
3. A player scores a point when the ball passes the opponent's paddle.

---

## Code Structure
- **`main.py`**: The main game loop and logic.
- **`paddle.py`**: Defines the `Paddle` class for controlling the paddles.
- **`ball.py`**: Defines the `Ball` class for ball movement and collision detection.
- **`score_board.py`**: Defines the `Score_board` class to manage and display the game score.

---
