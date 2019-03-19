# SearchPosition is a class representing a set of (x,y) coordinates on the board
# plus a round number. The round number represents the round at which this
# SearchPosition was found.

class SearchPosition():

    # Initialize the SearchPosition with (x, y) coords & round number
    def __init__(self, x, y, round):
        self.x = x
        self.y = y
        self.round = round

    def neighbors(self):
        neighbors = []

        neighbors.append(SearchPosition(self.x - 1, self.y, self.round))
        neighbors.append(SearchPosition(self.x + 1, self.y, self.round))
        neighbors.append(SearchPosition(self.x, self.y - 1, self.round))
        neighbors.append(SearchPosition(self.x, self.y + 1, self.round))
        
        return neighbors

    def increment_round(self):
        self.round += 1