def findRange(numbers):
    answer = []
    minNum, maxNum = 0,0
    numbers = numbers.split()
    for x in numbers:
        if int(x) < int(minNum):
            minNum = x
        if int(x) > int(maxNum):
            maxNum = x
    print(str(maxNum) + " " + str(minNum))
findRange(raw_input())
