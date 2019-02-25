let *B* be a 2-d array representing the pieces on the board
let *L* be an empty list
let *max_rounds* = 0

**for** all *tile* in *B*
    **if** *tile* contains a white piece
        add *tile* coordinates to *L* with rounds = 0

**while** *L* is not empty
    let *t* be the first element in *L*
    remove *t* from *L*
    process *t* according to **PROCESS_TILE(*t*, *L*, *B*)** below
    set *max_rounds* = max(*max_rounds*, *t*.rounds)

let *any_black* = false
**for** all *tile* in *B*
    **if** *tile* contains a black piece
        *any_black* = true
        exit loop

return *max_rounds*, *any_black*



**PROCESS_TILE(*t*, *L*, *B*)**
    Let *A* contain the tiles north, east, south, and west of *t*

    **for** all *u* in *A*
        **if** *u* contains a black piece
            update B to replace the piece at *u* with a white piece
            set *u*.rounds = *t*.rounds + 1
            add *u* to end of *L* 

    return *t*.rounds
