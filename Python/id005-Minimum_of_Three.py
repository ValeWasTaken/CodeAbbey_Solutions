# Python 3.4
def min_of_three():
    runs = int(input())
    answer = []
    
    for run in range(runs):
        answer.append(str(min([int(x) for x in input().split()])))
        
    print(' '.join(answer))

min_of_three()
