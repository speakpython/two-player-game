#https://speakpython.codes/two-player-game/2023/03/01/tic-tac-toe-human-vs-human.html#possible-winning-patterns

wining_pattern = [
    
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
    
]


#https://speakpython.codes/two-player-game/2023/03/01/tic-tac-toe-human-vs-human.html#grid-box-pattern

def game_grid(value):  
    print("\n")  
    print("\t____________________")  
    print("\t|      |      |     |")  
    print("\t|    {} |  {}   |  {}  |".format(value[0], value[1], value[2]))  
    print('\t|______|______|_____|')  
    print("\t|      |      |     |") 
    print("\t|   {}  |  {}   |  {}  |".format(value[3], value[4], value[5]))  
    print('\t|______|______|_____|')  
    print("\t|      |      |     |")  
    print("\t|  {}   |  {}   |  {}  |".format(value[6], value[7], value[8]))  
    print('\t|______|______|_____|')
    print("\n") 


#https://speakpython.codes/two-player-game/2023/03/01/tic-tac-toe-human-vs-human.html#game-initialisation

default_values = [' ' for i in range(9)] #create a list of 9 single spaces 
players_moves = { 
    'X_moves': [], # record palyer X's taken moves
    'O_moves': []  # record palyer O's taken moves
}
players = ['X', 'O'] # signifies total number of players
taken_move = [] # records all the moves taken by both the players


#https://speakpython.codes/two-player-game/2023/03/01/tic-tac-toe-human-vs-human.html#decide-winner

def check_wining(moves):
    for i in wining_pattern:
        if all(j in moves for j in i):
            return True 
    return False 


#https://speakpython.codes/two-player-game/2023/03/01/tic-tac-toe-human-vs-human.html#driver-code--brain

def main():
    step = 0
    game_grid(default_values)
    while step < 9:
        
        if step > 7:
            print('Match tied!')
            break
            
        player = players[step % 2]
        
        try:
            move = int(input(player + " : "))
            if move < 10 and move not in taken_move:
                taken_move.append(move)
                players_moves[player + '_moves'].append(move)
                default_values[move - 1] = player
                game_grid(default_values)
                step += 1
                if check_wining(players_moves[player + '_moves']):
                    print(player, 'Won!')
                    break
                continue

            print('Invalid move, try again!\n')

        except ValueError:
            print('Invalid move, try again!\n')

#https://speakpython.codes/two-player-game/2023/03/01/tic-tac-toe-human-vs-human.html#example-testing

main()