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

# Gem game 

Greed is a game in which the player seeks to gather as many falling gems as possible.
The game continues as long as the player wants more!

Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
The player (#) can move left or right along the bottom of the screen.
If the player touches a gem they earn a point.
If the player touches a rock they lose a point.
Gems and rocks are removed when the player touches them.
The game continues until the player closes the window.

# Getting Started

---

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 Greed Game
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

# Project Structure

The project files and folders are organized as follows:

```
root                                (project root folder)
+-- game                            (source code for game)
   +-- casting                      (Casting for the game)
        +-- actor.py                (Actor class)
        +-- artifact.py             (Artifact Class)
        +-- cast.py                 (director class)
   +-- directing                    (Directing folder)
        +-- director.py             (director class)
   +-- services                     (Services folder)
        +-- keyboard_service.py     (Keyboard service class)
        +-- video_service.py        (video service class)
   +-- shared                       (Shared folder)
        +-- color.py                (color class)
        +-- point.py                (point class)
   +-- __main__.py                  (program entry point)
+-- README.md                       (general info)
```


