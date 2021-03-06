'''
Author : Praveen
Date : 10-08-2018
'''

def calculatehandlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    count = 0
    for ke_y in hand:
        if hand[ke_y] > 0:
            count += hand[ke_y]
    return count

def main():
    '''This is main function'''
    nu_m = input()
    adict = {}
    for lo_op in range(int(nu_m)):
        data = input()
        spl_it = data.split()
        adict[spl_it[0]] = int(spl_it[1])
        lo_op += 1
    print(calculatehandlen(adict))


if __name__ == "__main__":
    main()
