class Round(object):
    def __init__(self, word, player_drawing, player) -> None:
        """init object

        Args:
            word (str): str
            player_drawing (Drawing): Player
            players(list): Player[]

        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guesses = []
        self.skips = 0
        self.player_scores = {player:0 for player in player_drawing}

    def guess(self, player, wrd):
        """for guess by player

        Args:
            player (Player): Player
            wrd (String): Guess Word

        Returns:
            bool: If player got correct answer
        """
        return wrd == self.word

    

    