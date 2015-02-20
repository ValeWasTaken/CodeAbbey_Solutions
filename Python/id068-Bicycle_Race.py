def findMeetup(meetups):
    answer = []
    for meetup in range(meetups):
        data = raw_input().split()
        distance,speedA,speedB = int(data[0]),int(data[1]),int(data[2])
        ETA = (distance / float(speedA + speedB))
        solution = ETA * speedA
        answer.append(str(solution))
    print(' '.join(answer))
findMeetup(input())
