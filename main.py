# Lab05avst.py
# This is a program that determines palindromes
# Evin Lodder 11/9/22
# Function <isPal> returns true if <str> is a "palindrome"
# and false otherwise.
def isPal(string: str) -> bool:
    return string == "".join(reversed(string))
#
# Function <isLetter> returns true if <char> is a letter
# in the ['A'..'Z'] range and false otherwise.
def isLetter(char: str) -> bool:
    return char.lower() in "abcdefghijklmnopqrstuvwxyz"
#
# Function <purge> returns <str> with all non-apha-numeric
# characters removed.
def purge(string: str) -> str:
    numbers: str = "0123456789"
    # If character isn't number or isn't letter it isn't included
    return ''.join(c for c in str if c.lower() in numbers or isLetter(c))
#
# Function <isAlmostPal> returns true if str is an "almost palindrome"
# and false otherwise.
def isAlmostPal(string: str) -> bool:
    # Return true if purged lowered is palindrome, XOR so it isn't almost palindrome if it literally is palindrome
    return isPal(purge(string).lower()) != isPal(string)
#
###############################
# Start of main execution loop
if __name__ == "__main__":
    notFinished= True
    while(notFinished):
        str =  input("Enter String: ")
        print()
        #
        print("Entered String:          ",str)
        print("Palindrome?:             ",isPal(str))
        print("Almost Palindrome?: ",isAlmostPal(str))
        print()
        repeat = input("Do you wish to repeat this program [Y/N]? ")
        notFinished = repeat.lower() == "y"
        print()
    #
    print("FINISHED")
