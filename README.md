# Snake-Water-Gun Game

A simple text-based implementation of the classic Snake-Water-Gun (similar to Rock-Paper-Scissors) game using Python. This game allows you to play multiple rounds against the computer and keeps track of the score.

## How to Play

- **Snake (s)** beats **Water (w)**.
- **Water (w)** beats **Gun (g)**.
- **Gun (g)** beats **Snake (s)**.
- If both the player and the computer choose the same option, it's a draw.

## Features

- You can choose how many rounds you want to play.
- The program will keep track of the scores for both the player and the computer.
- After all rounds are completed, the game announces the final winner.

## Requirements

- Python 3.x installed on your system.

## Getting Started

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/A3x-parvez/snake-water-gun-game.git

2 . Run the program into your terminal:
    ```bash
     python main.py



## Example 💡 ##

```bash
Enter how many rounds you want to play: 3

Round 1 Start.

Enter s (Snake), w (Water), or g (Gun): s
You chose Snake
Computer chose Gun
You Lose!

Round 1 Complete.


Round 2 Start.

Enter s (Snake), w (Water), or g (Gun): w
You chose Water
Computer chose Snake
You Lose!

Round 2 Complete.


Round 3 Start.

Enter s (Snake), w (Water), or g (Gun): g
You chose Gun
Computer chose Water
You Win!

Round 3 Complete.

Game Over!
Final Scores:
Your score = 1
Computer score = 2
The computer won the game! Better luck next time.
