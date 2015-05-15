# Python 3.4
def mortgage_calculator():
    data = input().split()
    p = loan_amount = int(data[0])
    i = interest_rate = (int(data[1]) / 100.0) / 12
    n = months_until_complete = int(data[2])

    monthly_payment = p*(i*(1+i)**n)/((1+i)**n-1)
    print(round(monthly_payment))
mortgage_calculator()
