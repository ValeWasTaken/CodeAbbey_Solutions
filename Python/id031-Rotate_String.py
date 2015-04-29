def rotateString(amount):
    answer = []
    for string in range(amount):
        data = raw_input().split()
        rotateNum,string = int(data[0]),data[1]
        answer.append(string[rotateNum:]+string[:rotateNum])
    print(' '.join(answer))
rotateString(input())
