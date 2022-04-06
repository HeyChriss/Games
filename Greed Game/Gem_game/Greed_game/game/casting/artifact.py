from game.casting.actor import Actor


class Artifact(Actor):
    '''
    Calculates the score for a gem or a rock.

    Attributes: 
     set_score is to detemine a point for a gem, minus a point for a rock.
     remove_artifact is to remove the artifact when the robot touches it.
    '''

    def __init__(self):
        super().__init__() 
        self._score = 0
        


    def set_score(self):
        """
        Tell director to add or minus 1 based on artifact type
        return 
        """
        if self._text == '*':
            self._score += 1
        elif self._text  == 'O':
            self._score -=1
        return self._score

    def remove_artifact(self):
        """
        Tell the director to remove the artifact when 'touched'.
        """
        pass
