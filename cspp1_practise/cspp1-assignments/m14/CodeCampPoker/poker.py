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
    backward_sequence = 'AKQJT987654321A'
    dictionary = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8, 'J':9, 'Q':10, 'K':11, 'A':12}
    st_r = ""
    st_r1 = ""
    '''for lo_op in range(le_n):
        st_r += hand[lo_op][0]
        st_r1 += dictionary[hand[lo_op][0]]'''
    # l = list(int(st_r1)).sort()
    '''for lo_op in range(11):
        if forward_sequence[lo_op:lo_op + 5] == st_r or backward_sequence[lo_op:lo_op + 5]:
            return 1'''
    for lo_op in dictionary:
    	for lo_op1 in range(le_n):
    		if hand[lo_op1][0] == lo_op:
    			st_r += lo_op
    print(st_r)
    for lo_op in range(11):
        if forward_sequence[lo_op:lo_op + 5] == st_r or backward_sequence[lo_op:lo_op + 5]:
            return 1
    if st_r[0] == '2' and st_r[4] == 'A':
    	return 1 
    return 0

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
            return 0
    return 2
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    su_m = 0
    su_m = is_straight(hand) + is_flush(hand)
    return su_m

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
    return max(hands, key=hand_rank)

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
