# Board is a class representing a game board with its tiles. Its internal _board
# property stores the current 2-D array representation of the board. The TYPE_AT
# method takes a SearchPosition and returns the TileType stored at the
# SearchPosition's coordinates. The FLIP_TILE method takes a SearchPosition and
# if the board contains a black tile at the SearchPosition's coordinates,
# replaces it with a white tile. The TO_SORTED_LINKED_LISTS method returns two
# doubly linked lists, white_tiles and black_tiles, which contain all of the 
# white and black tiles in the board, respectively.

from gone.search_position import SearchPosition
from gone.tile_types import TileTypes
from collections import deque

class Board():

    # Store the 2-D input array in _board
    def __init__(self, board):
        self._board = board

    # Return the TileType in _board at (search_position.x, search_position.y)
    # If search_position is invalid, return TileTypes.EMPTY
    def tile_at(self, search_position):
        if search_position.x in range(0, len(self._board)) and search_position.y in range(0, len(self._board[0])):
            return self._board[search_position.x][search_position.y]
        else:
            return TileTypes.EMPTY

    # If _board contains a black tile at search_position, change it to white
    def flip_tile(self, search_position):
        if self._board[search_position.x][search_position.y] == TileTypes.BLACK:
            self._board[search_position.x][search_position.y] = TileTypes.WHITE

    def to_sorted_linked_lists(self):
        # Let White_Tiles and Black_Tiles be empty doubly linked lists of
        # SearchPositions

        # TODO: Replace with dictionary to replace below if-elif with lookup
        white_tiles = deque()
        black_tiles = deque()

        # For each (x, y) position in _board, add to respective list
        for x in range(0, len(self._board)):
            for y in range(0, len(self.board[x])):

                search_position = SearchPosition(x, y, 0)

                if self.tile_at(search_position) == TileTypes.WHITE:
                    white_tiles.append(search_position)

                elif self.tile_at(search_position) == TileTypes.BLACK:
                    black_tiles.append(search_position)

        return white_tiles, black_tiles