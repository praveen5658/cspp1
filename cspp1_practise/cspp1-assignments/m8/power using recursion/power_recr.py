'''
Author : Praveen
Date : 07-08-2018
'''
def recur_power(base, exp):
    '''
    FUnction for computing Power using recursion
    '''
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * recur_power(base, exp-1)
def main():
    '''This is main function '''
    data = input()
    data = data.split()
    print(recur_power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
