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

        if self.x > 0:
            neighbors.append(SearchPosition(self.x - 1, self.y, self.round + 1))
        if self.x < len(self._board) - 1:
            neighbors.append(SearchPosition(self.x + 1, self.y, self.round + 1))
        if self.y > 0:
            neighbors.append(SearchPosition(self.x, self.y - 1, self.round + 1))
        if self.y < len(self._board[0]) - 1:
            neighbors.append(SearchPosition(self.x, self.y + 1, self.round + 1))
        
        return neighbors