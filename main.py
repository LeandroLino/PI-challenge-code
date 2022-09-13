from pythonds.basic.deque import Deque
import math
import time

def is_palindrome(aString):
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

def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    xx = 0
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2
        xx+=1


def find_palindromes_in_pi(palindromeSize):
    palindrome = ''
    pi = make_pi()
    while True:
        n = str(next(pi))
        if(len(palindrome)==palindromeSize):
            palindrome = palindrome[1:]
            palindrome = palindrome + n
        elif(len(palindrome)<palindromeSize):   
            palindrome = palindrome + n

        if(is_palindrome(palindrome)
        and len(palindrome) == palindromeSize 
        and is_prime(palindrome)
        ):  
            print(f'First Palindrome with {palindromeSize} digits:', palindrome)
            break

if __name__ == "__main__":
    inicio = time.time()
    find_palindromes_in_pi(21)
    fim = time.time()
    print(fim - inicio)
