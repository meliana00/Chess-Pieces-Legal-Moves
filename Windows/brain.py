from itertools import product

alpha_num_map = {v:k for k,v in enumerate('ABCDEFGH', start=1)}

def possible_moves(piece, position):
    if piece == 'pawn':
        return pawn_moves(position)

    elif piece == 'knight':
        return knight_moves(position)

    elif piece == 'bishop':
        return bishop_moves(position)

    elif piece == 'rook':
        return rook_moves(position)

    elif piece == 'queen':
        return queen_moves(position)

    elif piece == 'king':
        return king_moves(position)

def pawn_moves(pos):
    if ord(pos[0]) < 72:
        position = chr(ord(pos[0]) + 1) + pos[1]  
    
    else:
        position = 'INVALID' 

    return position.split()

def knight_moves(pos):
    position = []

    position.append(chr(ord(pos[0])+2) + chr(ord(pos[1])+1))
    position.append(chr(ord(pos[0])-2) + chr(ord(pos[1])+1))
    position.append(chr(ord(pos[0])+2) + chr(ord(pos[1])-1))
    position.append(chr(ord(pos[0])-2) + chr(ord(pos[1])-1))
    position.append(chr(ord(pos[0])-1) + chr(ord(pos[1])+2))
    position.append(chr(ord(pos[0])+1) + chr(ord(pos[1])-2))
    position.append(chr(ord(pos[0])-1) + chr(ord(pos[1])-2))
    position.append(chr(ord(pos[0])+1) + chr(ord(pos[1])+2))

    for i in range(len(position)):
        if ord(position[i][0]) < 65 or ord(position[i][0]) > 72:
            position[i] = 'INVALID'

        if ord(position[i][1]) < 49 or ord(position[i][1]) > 56:
            position[i] = 'INVALID'

    return position

def bishop_moves(pos):
    col = int(pos[1])
    row = int(alpha_num_map[pos[0]])

    bottom_right = min(abs(row-1), 8-col)
    top_right = min(8-row, 8-col)
    top_left = min(8-row, abs(col-1))
    bottom_left = min(abs(row-1), abs(col-1))

    position = []
    alpha_pos = pos[0]
    num_pos = int(pos[1])

    for i in range(bottom_right):
        position.append(chr(ord(alpha_pos)-1) + str(num_pos + 1))
        alpha_pos = chr(ord(alpha_pos)-1)
        num_pos += 1

    alpha_pos = pos[0]
    num_pos = int(pos[1])

    for j in range(top_right):
        position.append(chr(ord(alpha_pos)+1) + str(num_pos + 1))
        alpha_pos = chr(ord(alpha_pos)+1)
        num_pos += 1
    
    alpha_pos = pos[0]
    num_pos = int(pos[1])

    for k in range(top_left):
        position.append(chr(ord(alpha_pos)+1) + str(num_pos - 1))
        alpha_pos = chr(ord(alpha_pos)+1)
        num_pos -= 1
    
    alpha_pos = pos[0]
    num_pos = int(pos[1])

    for l in range(bottom_left):
        position.append(chr(ord(alpha_pos)-1) + str(num_pos - 1))
        alpha_pos = chr(ord(alpha_pos)-1)
        num_pos -= 1

    return position

def rook_moves(pos):
    x_position = []
    y_position = []

    x_position = list(product(pos[0], ['1', '2', '3', '4', '5', '6', '7', '8']))
    y_position = list(product(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], str(pos[1]), ))

    position = list(set(x_position + y_position))
    res_list = list(sorted(set(["".join(x) for x in position])))

    del res_list[res_list.index(pos)]

    return res_list

def queen_moves(pos):
    rook = rook_moves(pos)
    bishop = bishop_moves(pos)

    position = rook + bishop
    
    return position

def king_moves(pos):
    x_limit = int(pos[1])
    y_limit = pos[0]
    x_position = []
    y_position = []

    result = []

    for i in range(3):
        if x_limit-1 < 9 and x_limit > 0:
            x_position.append(str(x_limit-1))
        x_limit += 1

    for j in range(3):
        if ord(y_limit)-1 >= ord('A') and ord(y_limit)-1 <= ord('H'):  
            y_position.append(chr(ord(y_limit)-1))
        y_limit = chr(ord(y_limit)+1)

    result = list(product(y_position, x_position))
    list_res = ["".join(x) for x in result]

    del list_res[list_res.index(pos)]
 
    return list_res

