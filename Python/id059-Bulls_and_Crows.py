# Python 2.7

def bulls_and_crows():
    answer = []
    # Note: numbers_to_compared is wasted to meet the CodeAbbey requirement.
    secret_number, numbers_to_compare = [x for x in raw_input().split()]
    numbers = [x for x in raw_input().split()]

    for number in numbers:
        number_match = place_match = count = 0
        for num in number[::]:
            if num == secret_number[count]:
                place_match += 1
            if num in secret_number and num != secret_number[count]:
                number_match += 1
            count += 1
        answer.append('{0}-{1}'.format(place_match, number_match))
    print(' '.join(answer))
bulls_and_crows()
