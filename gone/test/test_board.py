import pytest
from gone.board import Board
from gone.search_position import SearchPosition
from gone.tile_types import TileTypes

def _generate_basic_test_board():
    board = [
        [1,1,1],
        [2,2,2],
        [3,3,3]
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

TEST_POSITIONS = [
    SearchPosition(0, 0, 0),
    SearchPosition(1, 0, 0),
    SearchPosition(2, 0, 0)
]
@pytest.mark.parametrize(
    'test_position', TEST_POSITIONS
)
def test_tile_at_returns_tile_type(test_position):
    input_board, board = _generate_basic_test_board()

    assert board.tile_at(test_position) == input_board[test_position.x][test_position.y]

