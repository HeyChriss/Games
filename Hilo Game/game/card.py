import random
from game import director



class Card:
    def __init__(self):
        #add the variables and store them in a list
        self.current_cards = []
        self.score = 300

    def give_cards(self):
        #ramdom numbers
        card1 = random.randint(1, 13)
        card2 = random.randint(1, 13)
        self.current_cards = [card1, card2]
        print(f'The Card Is: {self.current_cards[0]}')
        self.answer = input('Higher or lower?(h/l) ')
        print(f'Next Card was: {self.current_cards[1]}')

    def points(self):
        # Calculate the points 
        if self.answer.lower() == 'h' and self.current_cards[0] < self.current_cards[1]:
            self.score += 100
        elif self.answer.lower() == 'l' and self.current_cards[0] > self.current_cards[1]:
            self.score += 100
        elif self.answer.lower() == 'h' and self.current_cards[0] > self.current_cards[1]:
            self.score -= 75
        elif self.answer.lower() == 'l' and self.current_cards[0] < self.current_cards[1]:
            self.score -= 75
        return self.score

    def deal(self):
        #Do the player wants to keep playing?
        if self.score > 0:
            return True
        else:
            return False
