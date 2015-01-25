def collatzSequence(tests):
    data = raw_input().split()
    answer = []
    
    for test in range(tests):
        count = 0
        value = int(data[test])
        
        while value != 1:
            if value % 2 == 0:
                value /= 2
            else:
                value = 3 * value + 1
            count += 1
        answer.append(str(count))
    print(' '.join(answer))
collatzSequence(input())
