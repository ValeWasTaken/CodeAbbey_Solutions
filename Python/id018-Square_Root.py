def sqRoot(numbers):
    answer = []
    for number in range(numbers):
        data = raw_input().split()
        value,runs = int(data[0]),int(data[1])
        root = 1.00

        if root == 0:
            print(1)
        else:
            for x in range(runs):
                division = value / root
                abs(root - division)
                root = (root + division) / 2
            answer.append(str(root))
    print(' '.join(answer))
sqRoot(input())
