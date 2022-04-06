from game import card


class Director:
    def __init__(self):
        # Define Game Start, and points
        self.on = True
        self.points = 0
        self.dealer = card.Card()

    def game_start(self):
        while self.on:
            self.get_inputs()
            self.get_updates()
            self.do_outputs()

    def get_inputs(self):
        # Gets the inputs at the beginning of the round. 

        self.dealer.give_cards()

    def get_updates(self):
        # Calling the points method from the class

        self.points = self.dealer.points()
        
    def do_outputs(self):
        
        # Print out the current score.
        # If they still have points to play then ask the user if wants to keep playing 
        # If they don't have points set game_on to False and stop playing .
        print(f"Your score is: {self.points}")

        # Return value of deal function.
        deal = self.dealer.deal()

        # Check if deal is True or False.
        if deal == True:
            choice = input("Keep playing [y/n] ")
            print('')
            if choice.lower() == "y":
                self.on = True
            else:
                self.on = False
        else:
            self.on = False
            print('You lost')
