# Python 2.7

def find_name(amount_of_cards):
    #amount_of_cards is a wasted variable required by CodeAbbey.
    answer = []
    cards = [int(x) for x in raw_input().split()]
    suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack','Queen', 'King', 'Ace']
    for card in cards:
        suit_number = card / 13
        suit = suits[suit_number]
        
        rank_number = card % 13
        rank = ranks[rank_number]

        answer.append('{0}-of-{1}'.format(rank, suit))
    print(' '.join(answer))
find_name(input())
