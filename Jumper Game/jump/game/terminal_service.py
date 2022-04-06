class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def read_letters(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
         
        return input(prompt)

    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """

        print(text)
    
    def write_draw(self, drawing):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(drawing)

    def write_single_line(self, text):
        """Displays the given text on the screen but doesn't do a new 
        line after each letter. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text, end="")
