
from game.casting.actor import Actor



class Score(Actor):
    """
    A record of points. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, position):
        super().__init__()
        self._points = 0
        self._position = position
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

    def get_points(self):
        """Gets the total points the player has.
        
        Returns:
            points (int): The total points a player has.
        """
        return self._points
