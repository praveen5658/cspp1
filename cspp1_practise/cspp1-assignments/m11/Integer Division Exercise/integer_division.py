'''
Author : Praveen
Date : 10-08-2018
'''

def integer_division(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

def main():
    data = input()
    data1 = data.split()
    print(integer_division(int(data1[0]), int(data1[1])))


if __name__ == "__main__":
    main()
