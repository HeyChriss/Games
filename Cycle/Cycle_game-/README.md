# CSE210-03


# Getting Started
---

* Python 3.8.0
* Raylib Python CFFI 3.7

---

# Team contributors

```
Daniel Harris har21072@byui.edu
Weylin Douglas  weylin76@msn.com
Christian Mijangos  mij1700@byui.edu
Christi Johnson   joh21088@byui.edu
```

# Cycle game 

The best rides are the ones where you
bite off much more than you can chew,
and live through it.

- Doug Bradbury -

Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

Cycle is played according to the following rules.

Players can move up, down, left and right...
Player one moves using the W, S, A and D keys.
Player two moves using the I, K, J and L keys.
Each player's trail grows as they move.
Players try to maneuver so the opponent collides with their trail.
If a player collides with their opponent's trail...
A "game over" message is displayed in the middle of the screen.
The cycles turn white.
Players keep moving and turning but don't run into each other.

# Getting Started

---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 snake 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

# Project Structure

The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cycle               (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game screen size)
+-- README.md           (general info)
```
