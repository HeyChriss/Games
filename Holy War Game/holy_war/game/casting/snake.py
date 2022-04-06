import constants
from game.casting.actor import Actor
from game.shared.point import Point
import random


class Snake(Actor):
    """
    A growing reptile representing the Universities.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, color1, color2):
        super().__init__()        
        self._snake_color1 = color1
        self._snake_color2 = color2
        self._segments = []
        self._prepare_body()


    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            text_list = [47,92]
            text = chr(random.choice(text_list))
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._snake_color1 if i % 2 else self._snake_color2)
            self._segments.append(segment)
            

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = 0.0
        y = 0.0

        if self._snake_color1 == constants.BLUE:
            x = int(constants.MAX_X // 2)
            y = int(constants.MAX_Y // 10)
        else:
            x = int(constants.MAX_X // 6)
            y = int(constants.MAX_Y // 4)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            
            text_list = [47,92]
            text = "8" if i == 0 else chr(random.choice(text_list)) 
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._snake_color1 if i % 2 else self._snake_color2)
            self._segments.append(segment)