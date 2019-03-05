from gone.board import Board

def _generate_basic_test_board():
    return [
        [1,1,1],
        [2,2,2],
        [3,3,3]
    ]

def test_init_stores_input_board():
    input_board = _generate_basic_test_board()

    board = Board(input_board)

    assert board._board is input_board