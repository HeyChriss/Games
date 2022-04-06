# from game.word_generator import Word_Generator
import time
from time import sleep
import random
from game.terminal_service import TerminalService
# from game.draw_image import Jumper

name = input("Enter Your Name: ")
print(f"Hello {name.title()}")
print("Get ready!!") 
print ("")
time.sleep(1)
print ("Let's play Jumpman!")
time.sleep(0.5)

class Game_element:
    """ Class controls the elements of the jumpman game.

    Attributes:
        terminal_service: For getting and displaying information on the terminal.
        jumper: The game's jumper image
        get_word: The list of words to choose from for the serect word.
        player_guess: The letter the player guesses.
        # chances: Number of wrong guess the player has.
        # guessed (boolen): Checks to see if the player has guessed the serect word.
        word to guess: The serect word displayed as underscores.
        word: Is the serect word.
    """


    def __init__(self):
        self._terminal_service = TerminalService()
        self._player_guess = ''
        self._word_to_guess = ''
        self._word = ''
        self._wrong_guess = False

    def get_word(self):  
        """ A list of words to be randomly chosen for the serect word.

        Args:
            self (Director): an instance of Director.
        
        """
        # random word from candidates  
        candidates = [
            'cloud', 'hydrogen', 'laugh', 'smile', 'toothbrush', 'class', 'game', 'sunshine', 'galaxy', 'telephone'
            'puzzle', 'assignment', 'vacation', 'awkward', 'blizzard', 'fuchsia', 'jovial', 'mnemonic', 'transplant',
            'waltz', 'stretch', 'zombie', 'pineapple', 'beach', 'cello', 'ticket', 'sprinkler', 'lighthouse',
            'suitcase', 'coconut', 'shark', 'sunflower', 'password', 'landscape', 'drawback', 'gasoline',
            'shampoo', 'chess', 'picnic', 'applause', 'nightmare', 'loveseat', 'charger', 'cabin'
        ]
        return random.choice(candidates)



    def jumpman_word(self):
        """ Gets the random word and prints underscore for length of word

            Args:
                self (Director): an instance of Director.

            Return:
                underscores for each letter for length of the secert word that will be displayed as t
            """
        self._word = self.get_word()
        self._word_to_guess = '_' * len(self._word)
        return self._word_to_guess



    def check_guess(self):
        """ Checks for correct letters, keeps track of number of guesses
            Args - self
            Return - the number of chances for the player, correct letters
            """

        self._player_guess in self._word
        # This to take the word that is to be guessed and to split it into single letters.
        word_as_list = list(self._word_to_guess)
        indices = [i for i, letter in enumerate(self._word) if letter == self._player_guess]
        for index in indices:
            word_as_list[index] = self._player_guess
        # This is to bring the single letters back into the word.
        self._word_to_guess = "".join(word_as_list)

    def wrong_guess(self):
        """ Check wrong letters
        Args:
            self (Director): an instance of Director.
        """
        if self._player_guess not in self._word: 
            return True




    def display_word(self):
        """ Displays the word the player is guessing with a space 
        between each letter.

        Args:
            self (Director): an instance of Director.
        """
        for i in self._word_to_guess:
            self._terminal_service.write_single_line(i + " ")
        
        

    def word_complete(self):
        """ Checks to see of the players guesses match the word

        Args:
            self (Director): an instance of Director.
        Returns: 
            True if both words match
        """
        if self._word_to_guess == self._word:
            return True


    def get_guess(self, letter):
        """Gets the letter guess from the player
        
        Args:
            self (Director): an instance of Director.
            letter: letter from the player
        
        """
        self._player_guess = letter   
