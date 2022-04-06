# CSE210-03

---

Team contributors

```
Daniel Harris har21072@byui.edu
Weylin Douglas  weylin76@msn.com
Christian Mijangos  mij1700@byui.edu
Christi Johnson   joh21088@byui.edu
```

# Jumper

Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of
secret word - one at time.

If the player guess a correct letter in the puzzle, the letter is revealed.
If the guess is incorrect, a line is cut on the player's parachute.
The game ends when the puzzle is solved or the player has no more parachute.

# Getting Started

---

Use Python 3.8x or newer, installed and running on your machine. Open a terminal and
browse to the project's root folder. Start the program by running the following
command:

```
python.exe jump
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and
open the project folder. Select the main module inside the game folder and click the
"run" icon.

# Project Structure

The project files and folders are organized as follows:

```
root                     (project root folder)
+-- jump                 (source code for game)
   +-- director          (director class)
   +-- draw_image        (source code for game)
   +-- game_elements     (source code for game)
   +-- terminal_service  (read/write terminal)
   +-- __main__.py       (program entry point)
+-- README.md            (general info)
```
