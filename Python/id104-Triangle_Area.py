from math import sqrt

def triangleArea(amount):
    answer = []
    for triangle in range(amount):
        vertices = raw_input().split()
        x1,y1,x2,y2,x3,y3 = vertices
        x1,y1,x2,y2,x3,y3 = int(x1),int(y1),int(x2),int(y2),int(x3),int(y3)
        #A = x1,y1
        #B = x2,y2
        #C = x3,y3
        
        distanceAB = sqrt((x2 - x1)**2 + (y2-y1)**2) # Distance between A and B
        distanceAC = sqrt((x3 - x1)**2 + (y3-y1)**2) # Distance between A and C
        distanceBC = sqrt((x3 - x2)**2 + (y3-y2)**2) # Distance between B and C
        a,b,c = distanceAB,distanceAC,distanceBC

        s = (a + b + c) / 2 # s  = Semiperimeter
        
        # Heron's Formula
        area = sqrt(s*((s-a)*(s-b)*(s-c)))
        answer.append(str(area))
    print(' '.join(answer))
triangleArea(input())
