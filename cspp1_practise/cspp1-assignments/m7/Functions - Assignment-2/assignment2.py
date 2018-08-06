'''
Author : Praveen
Date : 06-08-2018
'''
def paying_debt_off_in_a_year(balance, annual_interest_rate):
    '''This function compute the lowest monthly payment '''
    monthly_interest_rate = annual_interest_rate/12
    monthly_payment = 0
    newbalance = balance
    while newbalance >= 0:
        monthly_payment += 10
        newbalance = balance  
        month = 1
        while month <= 12 and newbalance > 0:
            newbalance -= monthly_payment
            newbalance += (monthly_interest_rate * newbalance)
            month += 1
    ans = "Lowest Payment: " + str(monthly_payment)
    print(ans)
def main():
    '''This is Main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    paying_debt_off_in_a_year(data[0], data[1])
if __name__== "__main__":
    main()
