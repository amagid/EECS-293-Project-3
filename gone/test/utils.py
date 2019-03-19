from gone.tile_types import TileTypes
from gone.board import Board
from gone.gone import Gone

def _generate_basic_test_board():
    board = _numbers_to_tile_types([
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
    ])
    return board, Board(board)

def _numbers_to_tile_types(board):
    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            board[x][y] = TileTypes(board[x][y])

    return board

def _generate_unprocessed_gone():
    gone = Gone([[]])

    gone._board = None
    gone._white_tiles = None
    gone._black_tiles = None
    gone._max_rounds = 0

    return gone