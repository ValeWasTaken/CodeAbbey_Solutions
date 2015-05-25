# Python 2.7

def double_dice_roll(rolls):
    dice_sides = 6
    answer = []
    for roll in range(rolls):
        die_1, die_2 = [int(x) for x in raw_input().split()]
        value_1 = (die_1 % dice_sides) + 1
        value_2 = (die_2 % dice_sides) + 1
        total_roll = value_1 + value_2
        answer.append(str(total_roll))
    print(' '.join(answer))
double_dice_roll(input())
