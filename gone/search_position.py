SearchPosition is a class representing a set of (x,y) coordinates on the board
plus a round number. The round number represents the round at which this
SearchPosition was found.

Class SearchPosition
    x = the X coordinate of this position
    y = the Y coordinate of this position
    round = the "round" of BFS at which this position was reached

    Constructor(X, Y, Round)
        Store X, Y, and Round in the respective fields in this SearchPosition