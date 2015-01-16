def timeCalc(calculations):
    answer = []
    for calculation in range(calculations):
        solution = 0
        # Day | hour | minute | second
        d1,h1,m1,s1,d2,h2,m2,s2 = raw_input().split()
        d1,h1,m1,s1,d2,h2,m2,s2 = int(d1),int(h1),int(m1),int(s1),int(d2),int(h2),int(m2),int(s2)
    
        if s2 >= s1:
            s = s2 - s1
        else:
            m2 -= 1
            s2 += 60
            s = s2 - s1

        if m2 >= m1:
            m = m2 - m1
        else:
            h2 -= 1
            m2 += 60
            m = m2 - m1
        
        if h2 >= h1:
            h = h2 - h1
        else:
            d2 -= 1
            h2 += 24
            h = h2 - h1
        d = d2 - d1      
        answer.append('('+str(d)+' '+str(h)+' '+str(m)+' '+str(s)+') ')
    print(' '.join(answer))
timeCalc(input())

# Note to self: Optimize later with use of sequential arrays.
