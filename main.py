from PI import PI #File with 1M of digits
from pythonds.basic.deque import Deque

def is_palindromes(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

def find_palindromes_in_pi(palindromeSize):
    palindrome = ''
    for n in PI[2:]:
        if(len(palindrome)==palindromeSize):
            palindrome = palindrome[1:]
            palindrome = palindrome + n
        elif(len(palindrome)<palindromeSize):
            palindrome = palindrome + n

        if(is_palindromes(palindrome) and len(palindrome) == palindromeSize):
            print(f'First Palindrome with {palindromeSize} digits:', palindrome)
            break

if __name__ == "__main__":
    find_palindromes_in_pi(9)
