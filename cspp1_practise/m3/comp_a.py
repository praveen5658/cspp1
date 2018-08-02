'''
@author Praveen
@date 02-08-2018
'''

VARA = "hello"
VARB = "world"
if(isinstance(VARA) == str or isinstance(VARB) == str):
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
