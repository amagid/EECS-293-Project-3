# SearchPosition is a class representing a set of (x,y) coordinates on the board
# plus a round number. The round number represents the round at which this
# SearchPosition was found.

class SearchPosition():

    # Initialize the SearchPosition with (x, y) coords & round number
    def __init__(self, x, y, round):
        self.x = x
        self.y = y
        self.round = round