#This file contains all of the library functions used in my project euler solutions
#Keep this file in Alphabetical Order
#Contains:
#esieve,fact,fib,is_palindrome,isprime,maxPF,nth_prime,pf,tri

import math,random

# E

def esieve(n):
    # The Sieve of Eratosthenes, O(n) space , O(log log n) time
    # Generates primes up to a limit
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

# F

def fact(n):
    # Returns the factorial of n, where factorial is n*(n-1)*(n-2)...*(1)
    if n >= 0:
        product = 1
        for i in range(n):
            product *= i+1
    else:
        raise ValueError('factorial is not defined for negative numbers')
    return product

def fib(n):
    # Returns fibonnacci(n), where fib(n) = fib(n-1)+fib(n-2)
    a,b = 0,1
    for x in range(0,n):
        a, b = b, a + b
    return a

# I

def is_palindrome(s):
    # Returns True if a string is a palindrome, False otherwise. 
    # A Palindrome is a string that is the same forwards and backwards.
    digits = list(str(s))
    return digits[::-1] == digits[:]

def isprime(n, precision=7):
    _smallprimeset = 1000000
    # http://en.wikipedia.org/wiki/Miller-Rabin_primality_test
    # Algorithm_and_running_time
    if n < 1:
        raise ValueError("Out of bounds, first argument must be > 0")
    elif n <= 3:
        return n >= 2
    elif n % 2 == 0:
        return False
        d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for repeat in range(precision):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1: continue

        for r in range(s - 1):
            x = pow(x, 2, n)
            if x == 1: return False
            if x == n - 1: break
        else: return False

    return True

# M

def maxPF(n):
    # Returns the max prime factor of a number
    maxPrime = -1
    while n%2 == 0:
        maxPrime = 2
        n /= 2
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        while n % x == 0:
            maxPrime = x
            n = n / x
    if n > 2:
        maxPrime = n    
    return int(maxPrime)    

# N

def nth_prime(n):
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                # break to stop testing more numbers, we know it's not a prime
                break
        else:
            prime_list.append(num)
        # don't check even numbers
        num += 2
    # return the last prime number generated
    return prime_list[-1]

# P

def pf(n): 
    # Returns the prime factor list of a number
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors 

# T

def tri(n):
    # Triangle numbers, O(1) time , O(1) space
    # Returns the nth triangle number
    return int(((n*(n+1))/2))


    



