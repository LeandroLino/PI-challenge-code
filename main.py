#from PI import PI
from pythonds.basic.deque import Deque
import math

PI = ''
with open('PI_3.txt', 'r') as file:
    PI = file.read().replace('\n', '')

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

def is_prime(seqNum):
    n = int(seqNum)
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True

def find_palindromes_in_pi(palindromeSize):
    palindrome = ''
    print(len(PI))
    for n in PI[1000000:]:
        if(len(palindrome)==palindromeSize):
            palindrome = palindrome[1:]
            palindrome = palindrome + n
        elif(len(palindrome)<palindromeSize):   
            palindrome = palindrome + n

        if(is_palindromes(palindrome)
        and len(palindrome) == palindromeSize 
        and is_prime(palindrome)
        ):  
            print(f'First Palindrome with {palindromeSize} digits:', palindrome)
            break

if __name__ == "__main__":
    find_palindromes_in_pi(21)
    #pass
