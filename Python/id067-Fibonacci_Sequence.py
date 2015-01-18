def fibonacci_search(amount):
        answer = []
        for x in range(amount):
                fibNum = input()
                a,b,c,count = 0,1,0,0
                while(c <= fibNum and fibNum != 0):
                        c = a + b
                        a = b
                        b = c
                        count += 1
                answer.append(str(count))
        print(' '.join(answer))
fibonacci_search(input())
