"""
Memoization:store the values for recent function calls so future calls do not have to repeat the work. 
"""

#implementing memoization with a fibonacci algorithm

fibonacci_cache={}

def fibonacci(n):
# If value is cached, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
         
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value =  fibonacci(n-1) + fibonacci(n-2)

# cache the value and return it
    fibonacci_cache[n] = value
    return

print(fibonacci(6))
