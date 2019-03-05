# TileTypes is an Enum representing the value contained in a tile on the board.
# Every cell in the 2-D board array must always contain exactly one TileType.

from enum import Enum

class TileTypes(Enum):
    WHITE = 1
    BLACK = 2
    EMPTY = 3