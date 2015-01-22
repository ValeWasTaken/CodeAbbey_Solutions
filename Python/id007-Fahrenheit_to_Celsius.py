def convert(variables):
    answer = []
    for x in range(int(variables[0])):
        num = float(variables[x+1])
        num = int(round(float((num) - 32) * (5.0/9.0)))
        answer.append(str(num))
    print(' '.join(answer))
convert(raw_input().split())
