'''
    Author : Praveen
    Date : 14-08-2018
'''

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    le_n = len(hand)
    forward_sequence = 'A123456789TJQKA'
    dictionary = {
        '2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8, 'J':9,
        'Q':10, 'K':11, 'A':12}
    st_r = ""
    for lo_op in dictionary:
        for lo_op1 in range(le_n):
            if hand[lo_op1][0] == lo_op:
                st_r += lo_op
    for lo_op in range(11):
        if forward_sequence[lo_op:lo_op + 5] == st_r:
            return True
    if st_r[0] == '2' and st_r[4] == 'A':
        return True
    return False

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    ch_ar = hand[0][1]
    le_n = len(hand)
    for lo_op in range(le_n):
        if hand[lo_op][1] != ch_ar:
            return False
    return True

def is_of_kind(hand):
    '''This will check the conditions of Four of a kind and three of kind'''
    dictionary = {}
    for lo_op in hand:
        if lo_op[0] in dictionary:
            dictionary[lo_op[0]] += 1
        else:
            dictionary[lo_op[0]] = 1
    if len(dictionary) != 2:
        return 0
    for lo_op in dictionary:
        if dictionary[lo_op] in (3, 4):
            return dictionary[lo_op]
def is_of_pair(hand):
    '''This will check the conditions of twp pair and one pair'''
    dictionary = {}
    co_u = 0
    for lo_op in hand:
        if lo_op[0] in dictionary:
            dictionary[lo_op[0]] += 1
        else:
            dictionary[lo_op[0]] = 1
    if len(dictionary) != 3:
        return 0
    for lo_op in dictionary:
        if dictionary[lo_op] == 2:
            co_u += 1
    return co_u
def is_full_house(hand):
    '''This will check the condition full house'''
    dictionary = {}
    for lo_op in hand:
        if lo_op[0] in dictionary:
            dictionary[lo_op[0]] += 1
        else:
            dictionary[lo_op[0]] = 1
    if len(dictionary) != 2:
        return False
    l_1 = list[dictionary.values()]
    if l_1[0] in (2, 3) and l_1[1] in (2, 3):
        return True
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    ra_nk = is_of_kind(hand)
    pair_rank = is_of_pair(hand)
    if is_straight(hand) and is_flush(hand):
        print(1)
        return 1
    if ra_nk == 4:
        print(2)
        return 2
    if is_full_house(hand):
        print(3)
        return 3
    if is_flush(hand):
        print(4)
        return 4
    if is_straight(hand):
        print(5)
        return 5
    if ra_nk == 3:
        print(6)
        return 6
    if pair_rank == 2:
        print(7)
        return 7
    if pair_rank == 1:
        print(8)
        return 8
    return 0

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return min(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
