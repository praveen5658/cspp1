'''
Author : Praveen
Date : 04-08-2018
'''
def main():
    '''
    This function prints value according to the given conditions
    '''
    nu_m = int(input())
    for i in range(1, nu_m+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

if __name__ == "__main__":
    main()
