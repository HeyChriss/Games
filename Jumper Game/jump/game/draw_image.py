from game.terminal_service import TerminalService

class Jumper:
    def __init__(self):
        """This is the constructor method and we are building the image here and set it as a list"""
        self._terminal_service = TerminalService()
        self._jumper = [
            '    ___    ',
            '   /___\   ',
            '   \   /   ',
            '    \ /    ',
            '     o     ',
            '    /|\    ',
            '    / \    ',
            '',           
            '^^^^^^^^^^^'
        ]

    def draw_jumper(self):
        for i in self._jumper:
            self._terminal_service.write_text(i)


    def remove_parachute_piece(self):
        self._jumper.pop(0)
        

    def parachute_gone(self):
        self._jumper[0] = '     X     '
        

    def has_parachute(self):
        return len(self._jumper) >= 6
        
