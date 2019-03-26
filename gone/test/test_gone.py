import pytest
import math
from gone.gone import Gone
from gone.board import Board
from utils import _generate_basic_test_board, _numbers_to_tile_types, _generate_unprocessed_gone
from gone.tile_types import TileTypes

# Structured Basis, Data Flow, Boundary, Compound Boundary, Bad Data
def test_gone_empty_board():
    input_board = [[]]

    results = Gone(input_board)

    assert results.max_rounds() == 0
    assert not results.any_black_remaining()

# Bad Data
def test_gone_on_none_board():
    input_board = None

    with pytest.raises(TypeError):
        Gone(input_board)

# Bad Data
def test_gone_on_no_rows_board():
    input_board = [None]

    with pytest.raises(TypeError):
        Gone(input_board)

# Bad Data
def test_gone_on_3d_board():
    input_board = [[[]]]

    with pytest.raises(TypeError):
        Gone(input_board)

# Boundary, Compound Boundary, Good Data
def test_gone_1x1_board():
    input_board = [[TileTypes.WHITE]]

    results = Gone(input_board)

    assert results.max_rounds() == 0
    assert not results.any_black_remaining()

# Structured Basis, Data Flow, Boundary, Compound Boundary, Good Data
def test_gone_basic_board():
    input_board, _ = _generate_basic_test_board()

    results = Gone(input_board)

    assert results.max_rounds() == 1
    assert not results.any_black_remaining()

# Structured Basis, Boundary, Good Data
def test_gone_some_black_remaining():
    input_board = _numbers_to_tile_types([
        [1, 1, 1],
        [3, 3, 3],
        [2, 2, 2]
    ])

    results = Gone(input_board)

    assert results.max_rounds() == 0
    assert results.any_black_remaining()

# Structured Basis, Boundary, Compound Boundary, Good Data
TEST_BOARDS = [
    (
        [
            [1, 2, 2, 2, 2]
        ], 4, False
    ),
    (
        [
            [1, 2, 2, 2, 2, 2, 2, 2, 1]
        ], 4, False
    ),
    (
        [
            [1, 2, 2, 2, 3, 2]
        ], 3, True
    ),
    (
        [
            [2, 1, 1],
            [2, 2, 2],
            [2, 3, 3],
            [3, 3, 2]
        ], 3, True
    ),
    (
        [
            [1, 2, 2],
            [3, 3, 2],
            [2, 2, 2],
            [2, 3, 3],
            [2, 2, 2],
            [3, 3, 2],
            [2, 2, 2],
            [2, 3, 3],
            [2, 2, 2]
        ], 18, False
    )
]
@pytest.mark.parametrize(
    'test_case', TEST_BOARDS
)
def test_gone_various_boards(test_case):
    input_board, expected_rounds, expected_black_left = test_case
    board = _numbers_to_tile_types(input_board)

    results = Gone(board)

    assert results.max_rounds() == expected_rounds
    assert results.any_black_remaining() == expected_black_left

HUGE_DIMENSION = 10000
# Stress
def test_gone_long_thin_board():
    input_board = [[TileTypes.BLACK] * HUGE_DIMENSION]
    input_board[0][0] = TileTypes.WHITE

    results = Gone(input_board)

    assert results.max_rounds() == HUGE_DIMENSION - 1
    assert not results.any_black_remaining()


# Stress
def test_gone_tall_thin_board():
    input_board = []
    for i in range(0, HUGE_DIMENSION):
        input_board.append([TileTypes.BLACK])

    input_board[0][0] = TileTypes.WHITE

    results = Gone(input_board)

    assert results.max_rounds() == HUGE_DIMENSION - 1
    assert not results.any_black_remaining()

# Stress
def test_large_full_board():
    input_board = []
    for i in range(int(math.sqrt(HUGE_DIMENSION))):
        input_board.append([TileTypes.BLACK] * int(math.sqrt(HUGE_DIMENSION)))

    input_board[0][0] = TileTypes.WHITE

    results = Gone(input_board)

    assert results.max_rounds() == int(math.sqrt(HUGE_DIMENSION) - 1) * 2
    assert not results.any_black_remaining()
