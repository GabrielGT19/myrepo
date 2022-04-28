"""Intro"""


print('Welcome to TikTakToe!')

player_1 = input('What is the name of Player One? ')
player_2 = input('What is the name of Player Two? ')

print(f'{player_1} you will be X')
print(f'{player_2} you will be O')

player_1 = 'X'
player_2 = 'O'


print('Let the games begin!')


"""Game"""

def main():
    players = get_players
    table = tiktaktoe_table()
    print_table(table)






def get_players():
    player_1 == player_1
    player_2 == player_2



def tiktaktoe_table():
    table = []
    for space in range(9):
        table.append(space + 1)
    return table


def print_table(table):
    print()
    print()
    print(f'{table[0]}|{table[1]}|{table[2]}')
    print('-+-+-')
    print(f'{table[3]}|{table[4]}|{table[5]}')
    print('-+-+-')
    print(f'{table[6]}|{table[7]}|{table[8]}')
    print()
    print()

def winner(table):
    return (table[0] == table[1] == table[2] or
            table[3] == table[4] == table[5] or
            table[6] == table[7] == table[8] or
            table[0] == table[3] == table[6] or
            table[1] == table[4] == table[7] or
            table[2] == table[5] == table[8] or
            table[0] == table[4] == table[8] or
            table[2] == table[4] == table[6])


if __name__ == "__main__":
    main()