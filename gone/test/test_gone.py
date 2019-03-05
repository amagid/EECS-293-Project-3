from gone.gone import Gone
from gone.board import Board
from utils import _generate_basic_test_board

def test_gone_empty_board():
    input_board = [[]]

    results = Gone(input_board)

    assert results.max_rounds() == 0
    assert not results.any_black_remaining()

def test_gone_basic_board():
    input_board, _ = _generate_basic_test_board()

    results = Gone(input_board)

    assert results.max_rounds() == 1
    assert not results.any_black_remaining()