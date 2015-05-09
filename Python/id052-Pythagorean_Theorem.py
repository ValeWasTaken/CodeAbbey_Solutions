def pythagorean(triangles):
    answer = []
    for triangle in range(triangles):
        sides = input().split()
        a,b,c = sides
        a,b,c = int(a),int(b),int(c)

        if a**2 + b**2 == c**2:
            answer.append('R')
        elif a**2 + b**2 > c**2:
            answer.append('A')
        elif a**2 + b**2 < c**2:
            answer.append('O')
    print(' '.join(answer))
pythagorean(int(input()))
