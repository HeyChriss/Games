import random
import constants
from game.shared.color import Color
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.shared.point import Point


class Food(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        self.set_text("")
        self.set_color(constants.YELLOW)
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the food is worth."""
        self._points = random.randint(1, 8)
        x = random.randint(20, constants.MAX_X - 20)
        y = random.randint(20, constants.MAX_Y - 20)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        
        self.set_position(position)
        self.set_text('&')


    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
        
        
    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points
