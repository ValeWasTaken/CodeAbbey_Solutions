from math import sqrt

def triangleArea(amount):
    answer = []
    for triangle in range(amount):
        x1,y1,x2,y2,x3,y3 = [int(x) for x in raw_input().split()]
        #A = x1,y1      B = x2,y2       C = x3,y3
        a = sqrt((x2 - x1)**2 + (y2-y1)**2) # Distance between A and B
        b = sqrt((x3 - x1)**2 + (y3-y1)**2) # Distance between A and C
        c = sqrt((x3 - x2)**2 + (y3-y2)**2) # Distance between B and C
        s = (a + b + c) / 2 # s  = Semiperimeter
        area = sqrt(s*((s-a)*(s-b)*(s-c))) # Heron's Formula
        answer.append(str(area))
    print(' '.join(answer))
triangleArea(input())
