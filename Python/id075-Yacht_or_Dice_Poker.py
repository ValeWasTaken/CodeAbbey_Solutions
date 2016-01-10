import collections

def dice_poker():
    rolls = int(input())
    answer = []
    
    for roll in range(rolls):
        roll = input().split()
        values = sorted([x for x in collections.Counter(roll).values()])

        if sorted(roll) == ['2', '3', '4', '5', '6']:
            answer.append('big-straight')
        elif sorted(roll) == ['1', '2', '3', '4', '5']:
            answer.append('small-straight')
        elif values == [2, 3]:
            answer.append('full-house')
        elif values == [1, 2, 2]:
            answer.append('two-pairs')
        elif values == [5]:
            answer.append('yacht')
        elif values == [1, 4]:
            answer.append('four')
        elif values == [1, 1, 3]:
            answer.append('three')
        elif values == [1, 1, 1, 2]:
            answer.append('pair')
        else:
            answer.append('none')
        
    print(' '.join(answer))
dice_poker()
