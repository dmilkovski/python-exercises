#!/usr/bin/env python

board = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

player_a_symbol = ''
player_b_symbol = ''

current_move = 'A'
step_count = 0 

winning_states = list(map(lambda position_array : int(''.join(position_array), 2), [
    [
        '1', '0', '0',
        '1', '0', '0',
        '1', '0', '0',
    ],
    [
        '0', '1', '0',
        '0', '1', '0',
        '0', '1', '0',
    ],
    [
        '0', '0', '1',
        '0', '0', '1',
        '0', '0', '1',
    ],
    [
        '1', '0', '0',
        '0', '1', '0',
        '0', '0', '1',
    ],
    [
        '0', '0', '1',
        '0', '1', '0',
        '1', '0', '0',
    ],
    [
        '1', '1', '1',
        '0', '0', '0',
        '0', '0', '0',
    ],
    [
        '0', '0', '0',
        '1', '1', '1',
        '0', '0', '0',
    ],
    [
        '0', '0', '0',
        '0', '0', '0',
        '1', '1', '1',
    ],
])
)

state_player_a = list(map(lambda x : 0 , range(0, 9)))
state_player_b = list(map(lambda x : 0 , range(0, 9)))

def print_board(): 
    for x in range(0, len(board)):
        symbol = board[x]
        if x != 0 and x % 3 == 0 :
            print(f'\n--+---+---+')
            
        if state_player_a[x] != 0:
            symbol = player_a_symbol
        elif state_player_b[x] != 0:
            symbol = player_b_symbol
            
        print(f'{symbol} | ', end='')

def check_position(position) :
    return state_player_a[position - 1] != 1 and state_player_b[position - 1] != 1

def has_winner(player) :
    player_position = int(''.join([str(x) for x in player]), 2)
    # check diagonals
    for win_position in winning_states :
        if bin(win_position & player_position) == bin(win_position) :
            return True
        
    return False

def select_player(player) :
    userinput = ''
    while True :
        userinput = input(f'Select {player} symbol (X/O): ')
        if userinput.upper() == 'X' or userinput.upper() == 'O' :
            return userinput.upper()
        
        print(f'Please select symbol ("X" or "O") for ${player}: ')

def player_step() :
    userinput = ''
    while True :
        print_board()
        userinput = input(f'\n[Player{current_move.upper()}] please select position for ({get_player_symbol(current_move.upper())}): ')
        if(userinput.isnumeric()) :
            userinput = int(userinput)
            if userinput >= 1 and userinput <= 9 and check_position(userinput) :
                return userinput - 1

def get_player_symbol(player) :
    if player == 'A' :
        return player_a_symbol
    
    return player_b_symbol 

while not has_winner(state_player_a) and not has_winner(state_player_b) :
    if not player_a_symbol : 
        player_a_symbol = select_player('PlayerA')
        if player_a_symbol == 'X': player_b_symbol = 'O'
        else : player_b_symbol = 'X'
        
        print(f'PlayerA will play with symbol: {player_a_symbol}')
        print(f'PlayerB will play with symbol: {player_b_symbol}')
    
    if step_count >= 9 :
        print('KO no one wins')
        break
    
    if current_move == 'A' :
        state_player_a[player_step()] = 1
        current_move = 'B'
    else :
        state_player_b[player_step()] = 1
        current_move = 'A'
    
    step_count = step_count + 1 
    