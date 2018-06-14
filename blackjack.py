from random import random

card_colours = ["diamonds", "heart", "spades", "clubs"]

card_value = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

def initial_cards(deck, players):

    player1 = []
    player2 = []

    for i in range(len(players)):
        player1_initial_card = int(random() * len(deck))
        players['Player 1'].append(deck[player1_initial_card][0])
        del deck[player1_initial_card]

        player2_initial_card = int(random() * len(deck))
        players['Player 2'].append(deck[player2_initial_card][0])
        del deck[player2_initial_card]

    return deck, players


def calculate_score(cards):
    total = 0
    for card in cards:
        if total >= 11 and card == 'A':
            total += 1
        else:
            total += card_value[card]
    return total


def player_turn(deck, players, stand_count):

    for player in players:
        if player in stand_count:
            continue
        print('\n%s\'s turn: \n' % player)
        print('your current cards are: %s \n' %players[player])
        player_input = input('Do you want another card? (y)')

        if player_input == 'y':
            position = int(random() * len(deck))
            print('you got another card:', deck[position][0])
            players[player].append(deck[position][0])
            print('your current cards are: %s \n' %players[player])
            del deck[position]
        else:
            stand_count.append(player)

    return deck, players, stand_count

def main():
    deck = []
    for colour in card_colours:
        for card in card_value:
            deck.append((card, colour))

    players = {
        'Player 1': [],
        'Player 2': []
    }

    winner = None
    stand_count = []


    deck, players = initial_cards(deck, players)

    while winner == None:

        deck, players, stand_count = player_turn(deck, players, stand_count)

        player1_score = calculate_score(players['Player 1'])
        player2_score = calculate_score(players['Player 2'])

        if player1_score > 21:
            winner = 'Player 2'
            print('Player 1 lost! Winner is %s' % winner)
        elif player2_score > 21:
            winner = 'Player 1'
            print('Player 2 lost! Winner is %s' % winner)

        if 'Player 1' in stand_count and 'Player 2' in stand_count:
            if player1_score > player2_score:
                winner = 'Player 1'
                print('%s is the winner!' % winner)
            elif player2_score > player1_score:
                winner = 'Player 2'
                print('%s is the winner!' % winner)
            else:
                print('It\'s a draw!')
                winner = 'nobody'

    print('Player 1\'s score:', player1_score)
    print('Player 2\'s score:', player2_score)


if __name__ == "__main__":
    main()
