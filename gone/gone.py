# The Gone class exposes methods necessary to process an input game board and
# return the required number of rounds and whether or not any black pieces remain
# at the end.

from collections import deque
from gone.board import Board
from gone.search_position import SearchPosition
from gone.tile_types import TileTypes

class Gone():
    # an instance of the Board class generated from the input array
    _board = None
    # _white_tiles = a deque of SearchPositions (all white tiles)
    _white_tiles = None
    # _black_tiles = a deque of SearchPositions (all black tiles)
    _black_tiles = None
    # _max_rounds = the maximum number of rounds required to reach a black tile
    _max_rounds = 0


    # PROCESS_GAME(2d_array_board)
        # Generate a new Board instance from 2d_array_board and store in _board
        # _white_tiles, _black_tiles = _board.TO_SORTED_LINKED_LISTS()

        # SIMULATE_GAME()

        # Return MAX_ROUNDS(), ANY_BLACK_REMAINING()


    # SIMULATE_GAME()
        # While _white_tiles is not empty
            # Let tile be the first element in _white_tiles
            # Remove tile from _white_tiles

            # ADD_NEIGHBORS_TO_NEXT_ROUND(tile)

            # Set _max_rounds = max(_max_rounds, tile.rounds)

        # Return _max_rounds

        
    # ADD_NEIGHBORS_TO_NEXT_ROUND(tile)
        # Let neighbors contain the valid SearchPositions adjacent to tile

        # For each neighbor_position in neighbors
            # If _board.TILE_AT(neighbor_position) is TileTypes.BLACK
                # _board.FLIP_TILE(neighbor_position)
                # Set neighbor_position.rounds = tile.rounds + 1
                # Add neighbor_position to end of _white_tiles 


    # MAX_ROUNDS()
        # Return _max_rounds


    # ANY_BLACK_REMAINING()
        # For each position in _black_tiles
            # If _board.TILE_AT(position) is TileTypes.BLACK
                # Return true

        # Return false