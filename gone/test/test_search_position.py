from gone.search_position import SearchPosition

# Helper method to check if two SearchPositions have the same coordinates
def _are_same_position(position1, position2):
    return position1.x == position2.x and position1.y == position2.y

# Structured Basis, Data Flow
def test_init_assigns_x_y_round():
    x = 10
    y = 20
    round = 30
    search_position = SearchPosition(x, y, round)

    assert search_position.x == x
    assert search_position.y == y
    assert search_position.round == round

# Structured Basis, Data Flow
def test_neighbors_returns_all_neighbors():
    search_position = SearchPosition(1, 1, 0)
    expected_positions = [
        SearchPosition(0, 1, 1),
        SearchPosition(2, 1, 1),
        SearchPosition(1, 0, 1),
        SearchPosition(1, 2, 1)
    ]

    neighbors = search_position.neighbors()

    assert len(neighbors) == 4

    for neighbor in neighbors:
        found = False
        for position in expected_positions:
            if _are_same_position(position, neighbor):
                found = True

        assert found

def test_neighbors_returns_invalid_neighbors_too():
    search_position = SearchPosition(-2, -2, 0)
    expected_positions = [
        SearchPosition(-3, -2, 0),
        SearchPosition(-1, -2, 0),
        SearchPosition(-2, -3, 0),
        SearchPosition(-2, -1, 0)
    ]

    neighbors = search_position.neighbors()

    assert len(neighbors) == 4

    for neighbor in neighbors:
        found = False
        for position in expected_positions:
            if _are_same_position(position, neighbor):
                found = True

        assert found

# Boundary
def test_increment_round_on_0():
    search_position = SearchPosition(0, 0, 0)
    
    search_position.increment_round()

    assert search_position.round == 1

# Structured Basis, Data Flow, Boundary
def test_increment_round_on_mid_number():
    search_position = SearchPosition(0, 0, 5)
    
    search_position.increment_round()

    assert search_position.round == 6