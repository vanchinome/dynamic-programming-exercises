"""     
"""

import time

def fibonacci(n):
    """
    Calculates the n-fibonacci number using brute force and recursion
    """
    if n <=2: return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memoied(n, memo = {}):
    """
    Calculates the n-fibonacci number using brute force and recursion but
    uses memoization to reduce time complexity and making it run faster
    for bigger values
    """
    if n in memo: return memo[n]
    if n <=2: return 1
    memo[n] = fibonacci_memoied(n - 1, memo) + fibonacci_memoied(n - 2, memo)
    return memo[n]

print("Normal fibonacci run:")

start_time = time.time()

print("Fibonaci 1: ",fibonacci(1))
print("Fibonaci 2: ",fibonacci(2))
print("Fibonaci 6: ",fibonacci(6))
print("Fibonaci 37: ",fibonacci(37))

print("Run took", time.time() - start_time, "seconds")

start_time = time.time()

print("Fibonaci 1: ",fibonacci_memoied(1))
print("Fibonaci 2: ",fibonacci_memoied(2))
print("Fibonaci 6: ",fibonacci_memoied(6))
print("Fibonaci 37: ",fibonacci_memoied(37))

print("Run took", time.time() - start_time, "seconds")