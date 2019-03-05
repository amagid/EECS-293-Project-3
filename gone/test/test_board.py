from gone.board import Board

def test_init_stores_input_board():
    input_board = [
        [1,1,1],
        [2,2,2],
        [3,3,3]
    ]

    board = Board(input_board)

    assert board._board is input_board