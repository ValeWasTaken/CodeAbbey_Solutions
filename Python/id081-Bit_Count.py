def bitCount():
    codeAbbeyWaste = input() # Required by CodeAbbey
    numbers = input().split()
    answer = []
    for num in numbers:
        data = int(num) % 0x100000000
        bits = format(data, 'b')
        answer.append(str(bits.count('1')))
    print(' '.join(answer))
bitCount()
