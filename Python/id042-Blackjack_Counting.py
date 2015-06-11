# Python 2.7

def blackjack_counter(games):
    answer = []
    values = {
        '2':2,    '3':3,    '4':4,
        '5':5,    '6':6,    '7':7,
        '8':8,    '9':9,
        'T':10,   'J':10,   'Q':10,
        'K':10,   'A':11
        }
    
    for game in range(games):
        cards = [x for x in raw_input().split()]
        total, ace_count = 0, 0
        
        for card in cards:
            total += values[card]
            if card == 'A':
                ace_count += 1
                
        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1

        if total > 21:
            answer.append('Bust')
        else:
            answer.append(str(total))

    print(' '.join(answer))
blackjack_counter(input())
