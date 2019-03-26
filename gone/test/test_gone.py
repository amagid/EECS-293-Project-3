import pytest
from gone.gone import Gone
from gone.board import Board
from utils import _generate_basic_test_board, _numbers_to_tile_types, _generate_unprocessed_gone

# Structured Basis, Data Flow
def test_gone_empty_board():
    input_board = [[]]

    results = Gone(input_board)

    assert results.max_rounds() == 0
    assert not results.any_black_remaining()

# Structured Basis, Data Flow
def test_gone_basic_board():
    input_board, _ = _generate_basic_test_board()

    results = Gone(input_board)

    assert results.max_rounds() == 1
    assert not results.any_black_remaining()

# Structured Basis
def test_gone_some_black_remaining():
    input_board = _numbers_to_tile_types([
        [1, 1, 1],
        [3, 3, 3],
        [2, 2, 2]
    ])

    results = Gone(input_board)

    assert results.max_rounds() == 0
    assert results.any_black_remaining()

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

# Structured Basis
def test_gone_various_boards(test_case):
    input_board, expected_rounds, expected_black_left = test_case
    board = _numbers_to_tile_types(input_board)

    results = Gone(board)

    assert results.max_rounds() == expected_rounds
    assert results.any_black_remaining() == expected_black_left

