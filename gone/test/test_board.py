import pytest
from collections import deque
from gone.board import Board
from gone.search_position import SearchPosition
from gone.tile_types import TileTypes
from utils import _generate_basic_test_board, _numbers_to_tile_types

# Structured Basis, Data Flow
def test_init_stores_input_board():
    input_board, _ = _generate_basic_test_board()

    board = Board(input_board)

    assert board._board is input_board

# Structured Basis, Data Flow, Boundary, Compound Boundary, Bad Data
TEST_INVALID_POSITIONS = [
    SearchPosition(3, 0, 0),
    SearchPosition(-1, 0, 0),
    SearchPosition(0, 3, 0),
    SearchPosition(0, -1, 0),
    SearchPosition(-1, -1, 0),
    SearchPosition(3, 3, 0),
    SearchPosition(-100, -100, -100)
]
@pytest.mark.parametrize(
    'test_position', TEST_INVALID_POSITIONS
)
def test_position_is_valid_returns_false_when_invalid(test_position):
    input_board, board = _generate_basic_test_board()

    assert not board._position_is_valid(test_position)

# Boundary, Compound Boundary
TEST_VALID_POSITIONS = [
    SearchPosition(0, 0, 0),
    SearchPosition(0, 2, 0),
    SearchPosition(2, 0, 0),
    SearchPosition(2, 2, 0),
    SearchPosition(1, 1, 0)
]
@pytest.mark.parametrize(
    'test_position', TEST_VALID_POSITIONS
)
def test_position_is_valid_returns_true_when_valid(test_position):
    input_board, board = _generate_basic_test_board()

    assert board._position_is_valid(test_position)

# Bad Data
def test_position_is_valid_on_bad_data():
    input_board, board = _generate_basic_test_board()

    with pytest.raises(AttributeError):
        board._position_is_valid(None)

# Structured Basis, Data Flow, Boundary
@pytest.mark.parametrize(
    'test_position', TEST_VALID_POSITIONS
)
def test_tile_at_returns_tile_type(test_position):
    input_board, board = _generate_basic_test_board()

    assert board.tile_at(test_position) == input_board[test_position.x][test_position.y]

# Structured Basis, Boundary, Bad Data
@pytest.mark.parametrize(
    'test_position', TEST_INVALID_POSITIONS
)
def test_tile_at_returns_empty_on_invalid_position(test_position):
    input_board, board = _generate_basic_test_board()

    assert board.tile_at(test_position) == TileTypes.EMPTY

# Bad Data
def test_tile_at_on_bad_data():
    input_board, board = _generate_basic_test_board()

    with pytest.raises(AttributeError):
        board.tile_at(None)

# Structured Basis, Data Flow
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

# Structured Basis, Bad Data
def test_flip_tile_errors_on_empty_tiles():
    input_board, board = _generate_basic_test_board()
    test_position = SearchPosition(2, 0, 0)

    assert board.tile_at(test_position) == TileTypes.EMPTY

    with pytest.raises(AssertionError):
        board.flip_tile(test_position)

def test_flip_tile_errors_on_invalid_tiles():
    input_board, board = _generate_basic_test_board()
    test_position = SearchPosition(-1, -1, 0)

    assert board.tile_at(test_position) == TileTypes.EMPTY

    with pytest.raises(AssertionError):
        board.flip_tile(test_position)

# Structured Basis, Boundary, Compound Boundary
def test_tile_position_lists_returns_deque():
    board = Board([[]])

    white_tiles, black_tiles = board.tile_position_lists()

    assert type(white_tiles) is deque
    assert type(black_tiles) is deque

# Structured Basis, Data Flow, Boundary
def test_tile_position_lists_on_empty_board():
    board = Board([])

    white_tiles, black_tiles = board.tile_position_lists()

    assert not white_tiles
    assert not black_tiles

# Structured Basis, Data Flow, Boundary, Compound Boundary
def test_tile_position_lists_on_1x1_board():
    board = Board([[TileTypes.EMPTY]])

    white_tiles, black_tiles = board.tile_position_lists()

    assert not white_tiles
    assert not black_tiles

# Structured Basis, Data Flow, Bad Data
def test_tile_position_lists_on_thin_board():
    board = Board([[], [], [], []])

    white_tiles, black_tiles = board.tile_position_lists()

    assert not white_tiles
    assert not black_tiles

# Structured Basis, Compound Boundary
def test_tile_position_lists_on_basic_board():
    input_board, board = _generate_basic_test_board()

    white_tiles, black_tiles = board.tile_position_lists()

    assert len(white_tiles) == 3
    assert len(black_tiles) == 3
    
    for tile in white_tiles:
        assert board.tile_at(tile) == TileTypes.WHITE

    for tile in black_tiles:
        assert board.tile_at(tile) == TileTypes.BLACK

# Bad Data
def test_tile_position_lists_on_bad_data():
    board = Board([None])

    with pytest.raises(TypeError):
        board.tile_position_lists()

# Bad Data
def test_tile_position_lists_on_bad_data():
    board = Board(None)

    with pytest.raises(TypeError):
        board.tile_position_lists()