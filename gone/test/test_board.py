import pytest
from gone.board import Board
from gone.search_position import SearchPosition
from gone.tile_types import TileTypes

def _generate_basic_test_board():
    board = [
        [TileTypes.WHITE, TileTypes.WHITE, TileTypes.WHITE],
        [TileTypes.BLACK, TileTypes.BLACK, TileTypes.BLACK],
        [TileTypes.EMPTY, TileTypes.EMPTY, TileTypes.EMPTY]
    ]
    return board, Board(board)

def test_init_stores_input_board():
    input_board, _ = _generate_basic_test_board()

    board = Board(input_board)

    assert board._board is input_board

TEST_MOVEMENTS = [
    { "x": 1, "y": 0 },
    { "x": -1, "y": 0 },
    { "x": 0, "y": 1 },
    { "x": 0, "y": -1 }
]
@pytest.mark.parametrize(
    'test_movement', TEST_MOVEMENTS
)
def test_tile_at_returns_empty_when_invalid(test_movement):
    input_board, board = _generate_basic_test_board()

    test_position = SearchPosition(test_movement["x"] * len(input_board), test_movement["y"] * len(input_board[0]), 0)

    assert board.tile_at(test_position) == TileTypes.EMPTY

TEST_TILE_AT_POSITIONS = [
    SearchPosition(0, 0, 0),
    SearchPosition(1, 0, 0),
    SearchPosition(2, 0, 0)
]
@pytest.mark.parametrize(
    'test_position', TEST_TILE_AT_POSITIONS
)
def test_tile_at_returns_tile_type(test_position):
    input_board, board = _generate_basic_test_board()

    assert board.tile_at(test_position) == input_board[test_position.x][test_position.y]

def test_flip_tile_flips_black_to_white():
    input_board, board = _generate_basic_test_board()
    test_position = SearchPosition(1, 0, 0)

    assert board.tile_at(test_position) == TileTypes.BLACK

    board.flip_tile(test_position)

    assert board.tile_at(test_position) == TileTypes.WHITE

def test_flip_tile_ignores_white_tiles():
    input_board, board = _generate_basic_test_board()
    test_position = SearchPosition(0, 0, 0)

    assert board.tile_at(test_position) == TileTypes.WHITE

    board.flip_tile(test_position)

    assert board.tile_at(test_position) == TileTypes.WHITE

def test_flip_tile_ignores_empty_tiles():
    input_board, board = _generate_basic_test_board()
    test_position = SearchPosition(2, 0, 0)

    assert board.tile_at(test_position) == TileTypes.EMPTY

    board.flip_tile(test_position)

    assert board.tile_at(test_position) == TileTypes.EMPTY

def test_flip_tile_ignores_invalid_tiles():
    input_board, board = _generate_basic_test_board()
    test_position = SearchPosition(-1, -1, 0)

    assert board.tile_at(test_position) == TileTypes.EMPTY

    board.flip_tile(test_position)

    assert board.tile_at(test_position) == TileTypes.EMPTY