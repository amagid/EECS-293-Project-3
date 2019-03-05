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
        # While self._white_tiles is not empty
        while self._white_tiles:
            # Let tile be the first element in _white_tiles
            # Remove tile from _white_tiles
            tile = self._white_tiles.popleft()

            self._add_neighbors_to_next_round(tile)

            self._max_rounds = max(self._max_rounds, tile.rounds)

        return self._max_rounds

        
    def _add_neighbors_to_next_round(self, tile):
        # Let neighbors contain the valid SearchPositions adjacent to tile
        neighbors = []
        if tile.x > 0:
            neighbors.append(SearchPosition(tile.x - 1, tile.y, tile.round + 1))
        if tile.x < len(self._board) - 1:
            neighbors.append(SearchPosition(tile.x + 1, tile.y, tile.round + 1))
        if tile.y > 0:
            neighbors.append(SearchPosition(tile.x, tile.y - 1, tile.round + 1))
        if tile.y < len(self._board[0]) - 1:
            neighbors.append(SearchPosition(tile.x, tile.y + 1, tile.round + 1))

        for neighbor_position in neighbors:
            if self._board.tile_at(neighbor_position) == TileTypes.BLACK:
                self._board.flip_tile(neighbor_position)
                # Add neighbor_position to end of _white_tiles 
                self._white_tiles.append(neighbor_position)


    def _max_rounds(self):
        pass
        # Return _max_rounds


    def _any_black_remaining(self):
        pass
        # For each position in _black_tiles
            # If _board.TILE_AT(position) is TileTypes.BLACK
                # Return true

        # Return false