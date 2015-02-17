def playRPS(games):
    answer = []
    for game in range(games):
        matches = raw_input().split()
        player1,player2 = 0,0
        for match in matches:
            if match == 'RR' or match == 'PP' or match == 'SS':
                0
            elif match == 'RS' or match == 'PR' or match == 'SP':
                player1 += 1
            else:
                player2 += 1
        if player1 > player2:
            answer.append("1")
        else:
            answer.append("2")
    print(' '.join(answer))
playRPS(input())
