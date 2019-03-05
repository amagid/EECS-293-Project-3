# The Gone class exposes methods necessary to process an input game board and
# return the required number of rounds and whether or not any black pieces remain
# at the end.

from collections import deque
from gone.board import Board
from gone.search_position import SearchPosition
from gone.tile_types import TileTypes

class Gone():

    def __init__(self, array_board):
        # an instance of the Board class generated from the input array
        self._board = Board(array_board)
        # a deque of SearchPositions (all white tiles)
        self._white_tiles = None
        # a deque of SearchPositions (all black tiles)
        self._black_tiles = None
        # the maximum number of rounds required to reach a black tile
        self._max_rounds = 0

        self._initialize_game()

    def _initialize_game(self):
        self._white_tiles, self._black_tiles = self._board.to_sorted_linked_lists()

        self._simulate_game()

        return self._max_rounds(), self._any_black_remaining()


    def _simulate_game(self):
        pass
        # While _white_tiles is not empty
            # Let tile be the first element in _white_tiles
            # Remove tile from _white_tiles

            # ADD_NEIGHBORS_TO_NEXT_ROUND(tile)

            # Set _max_rounds = max(_max_rounds, tile.rounds)

        # Return _max_rounds

        
    def _add_neighbors_to_next_round(self, tile):
        pass
        # Let neighbors contain the valid SearchPositions adjacent to tile

        # For each neighbor_position in neighbors
            # If _board.TILE_AT(neighbor_position) is TileTypes.BLACK
                # _board.FLIP_TILE(neighbor_position)
                # Set neighbor_position.rounds = tile.rounds + 1
                # Add neighbor_position to end of _white_tiles 


    def _max_rounds(self):
        pass
        # Return _max_rounds


    def _any_black_remaining(self):
        pass
        # For each position in _black_tiles
            # If _board.TILE_AT(position) is TileTypes.BLACK
                # Return true

        # Return false