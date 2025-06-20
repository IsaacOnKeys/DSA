"""
- Recursive function is a function calling itself,
- An alternative to loops in most situations
------------------------------------------------
  How recursion works:
 computer uses a stack (the call stack) to keep track of the functions. It calls the first interation of the Recursive function, then starts the next before it can finish. Because it didn't finish, it gets added to the call stack, as do aall the subsequent function iterations. After n=1 finishes (in other words the base-case condition is met as n = 1), it passes the result of that function call to the next on on the stak, specifically, n = 2. All the unfinished function calls that are stacked up now multiple by each other in first-in-first-out order (because it's a STACK).
 So, factorial_recursion above:
  factorial_recursion(5) returns  
    5th call: factorial_recursion(1)
    4th call: factorial_recursion(2)
    3rd call: factorial_recursion(3)
    2nd call: factorial_recursion(4)
    1st call: factorial_recursion(5)
    which then get multiplied in this order: 1*2*3*4*5
-----------------
### Examples ###

1. Factorial Calculation:
 n! = n * (n-1)!

2. Fibonacci sequence:
 fib(n) = fib(n - 1) + fib(n - 2) , with and , being the position in the sequence.

3. Towers of Hanoi:
 Transfer all the disks from one of the three rods to another, following these rules:

  -  You can only move one disk at a time.
  -  You can only take the upper disk from one of the stacks and place it on top of another stack.
  - You cannot put a larger disk on top of a smaller one.

----------------------

Dynamic Programming:

- Optimization technique. mainly applied to recursion.
- Can reduce the complexity of recursive algoithms
- Used for any problem that can be divided into smaller sub-problems that overlap
- MEMOIZATION: The solutions of the sub-problems are saved, avoiding the need for recalculation later.
-

------------------------------
Pros & Cons of Recursion
Con: does not scale up like iteration. Requires more memory
Con: in many languages iterative solutions are way faster
Con: sometimes more abstract or harder to understand than iterative solutions
Pro: in some cases, extramely fast and easy to code. 
Pro: Extremely practical for tree traversals and binary search.

"""

### Factorial Calculation ###
def factorial_while_loop(n: int) -> int:
 #initialize the result variable to 1:
  result = 1
  while n > 1:
   result = n * result
   print(f'n = {n}', f'result = {result}')
   n -= 1
  return result

print(factorial_while_loop(10))



# factorial recursion formula: n! = n * (n-1)!
""" 4! = 4*3*2*1
    4 * 3! =
    4 * 3 * 2! =
    4 * 3 * 2 * 1
"""
def factorial_recursion(n:int) ->int:
 #set base-case to avoid an infinite loop
 #catch statement:
 if n < 0:
  return -1
  # starts here:
 elif n <=  1 :
  return 1
 else:
  #this return statement iw what gets added to the stack, the first time it is added, partially finished as 5 * 
  return n * factorial_recursion(n - 1)
"""
CALL STACK:
return 1
2 * (factorial_recursion(2 - 1) = 1) = return 2
3 * (factorial_recursion(3 - 1) = 2) = return 6
4 * (factorial_recursion(4 - 1) = 6) = 24 
"""

### Fibonacci Sequence ###
def fibonacci(n):
  # Define the base case
  if n <= 1:
    return n
  else:
    # Call recursively to fibonacci
    return n + fibonacci(n -1)
    
print(fibonacci(6))

## ???? Check to see if the value exists in cache ????##
cache = [None]*(100)

def fibonacci(n): 
    if n <= 1:
        return n
    
    # Check if the value exists
    if not cache[n]:
        # Save the result in cache
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return cache[n]
    

print(fibonacci(6))

## Tower Of Hanoi ##
def hanoi(num_disks, from_rod, to_rod, aux_rod):
  # Correct the base case
  if num_disks >= 1:
    # Correct the calls to the hanoi function
    hanoi(num_disks -1, from_rod, aux_rod, to_rod )
    print("Moving disk", num_disks, "from rod", from_rod,"to rod",to_rod)
    hanoi(num_disks -1, aux_rod, to_rod, from_rod)   

num_disks = 4
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'

hanoi(num_disks, source_rod, target_rod, auxiliar_rod)
 