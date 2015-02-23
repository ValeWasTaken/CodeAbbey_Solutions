def foolsDay(problems):
    answer = []
    for problem in range(problems):
        total = 0
        numbers = raw_input().split()
        for num in numbers:
            total += int(num)*int(num)
        answer.append(str(total))
    print(' '.join(answer))
foolsDay(input())
