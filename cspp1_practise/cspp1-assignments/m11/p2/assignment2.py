'''
Author : Praveen
Date : 10-08-2018
'''

def updatehand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    for lo_op in word:
        if lo_op in hand:
            hand[lo_op] -= 1
    return hand

def main():
    '''This is main function'''
    nu_m = input()
    adict = {}
    for lo_op in range(int(nu_m)):
        data = input()
        sp_lit = data.split()
        adict[sp_lit[0]] = int(sp_lit[1])
        lo_op += 1
    data1 = input()
    print(updatehand(adict, data1))


if __name__ == "__main__":
    main()
