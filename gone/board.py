Board is a class representing a game board with its tiles. Its internal _board
property stores the current 2-D array representation of the board. The TYPE_AT
method takes a SearchPosition and returns the TileType stored at the
SearchPosition's coordinates. The FLIP_TILE method takes a SearchPosition and
if the board contains a black tile at the SearchPosition's coordinates,
replaces it with a white tile. The TO_SORTED_LINKED_LISTS method returns two
doubly linked lists, white_tiles and black_tiles, which contain all of the 
white and black tiles in the board, respectively.

Class Board
    _board = a 2-D array containing TileTypes to represent the game board.

    Constructor(2d_array_board)
        Store the 2-D input array in _board

    TILE_AT(search_position)
        Return the TileType in _board at (search_position.x, search_position.y)

    FLIP_TILE(search_position)
        If _board contains a black tile at search_position, change it to white

    TO_SORTED_LINKED_LISTS()
        Let White_Tiles and Black_Tiles be empty doubly linked lists of
            SearchPositions

        For each (x, y) position in _board
            Let search_position be a new SearchPosition with (x=x, y=y, rounds=0)
            If TILE_AT(search_position) is TileTypes.WHITE
                Add search_position to the end of White_Tiles
            Else if TILE_AT(search_position) is TileTypes.BLACK
                Add search_position to the end of Black_Tiles

        Return White_Tiles, Black_Tiles