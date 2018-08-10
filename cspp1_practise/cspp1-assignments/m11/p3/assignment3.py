'''
Author : Praveen
Date : 10-08-2018
'''

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    count = 0
    le_n = len(word)
    for lo_op in word:
        if lo_op in hand:
            count += 1
    return bool(count == le_n && word in wordList)



def main():
    word=input()
    nu_m=int(input())
    adict={}
    for ite_r in range(nu_m):
        data=input()
        spl_it=data.split()
        adict[spl_it[0]]=int(spl_it[1])
        ite_r += 1
    l_2=input().split()
    print(isValidWord(word,adict,l_2))
        


if __name__ == "__main__":
    main()
