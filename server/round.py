"""
Round:
        word: str
        time: float
        player_drawing: Player
        player_guessed: list
        skips: int
        player_scores: list
"""
import time
from _thread import *

class Round(object):
    def __init__(self, word, player_drawing, player) -> None:
        """init object

        Args:
            word (str): str
            player_drawing (Drawing): Player Object
            players(list): Player[]

        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.player_scores = {player:0 for player in player_drawing}
        # self.start = time.time()
        start_new_thread(self.time_thread, ())

    def time_thread(self):
        """
        Runs in thread to keep track of the time
        """
        while self.time > 0:
            time.sleep(1)
            self.time -=1
        self.end_round("Time is Up")

    def guess(self, player, wrd):
        """for guess by player

        Args:
            player (Player): Player
            wrd (String): Guess Word

        Returns:
            bool: If player got correct answer
        """
        # return wrd == self.word
        correct = wrd = self.word
        if correct:
            self.player_guessed.append(player)


    def player_left(self, player):
        """removes the player from list and scores

        Args:
            player (Player): Player
        Returns:
            None

        """
        if player in self.player_scores:
            del self.player_scores[player]
        
        if player in self.player_guessed:
            self.player_guessed.remove(player)
        
        if player==self.player_drawing:
            self.end_round("Drawing Player Left")

    
    def end_round(self, msg):
        pass
        

    

    