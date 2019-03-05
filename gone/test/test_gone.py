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