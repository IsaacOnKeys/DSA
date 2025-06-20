""" 
Big Omega (Ω) ==  best case
Big Theta (Θ) == average runtime of an algorithm.
BIG Omicron (O)== worst case

TIME COMPLEXITY
REFERENCE:
https://www.bigocheatsheet.com/
-----------------------------------------------------
#################
##### BIG O #####
#################
OPTIMIZATION Considerations:
    # Drop constants
    # Drop Non-Dominants: if you have O(n^2, n), drop the n because it is less significant, especially as n^2 grows.
    # Different Terms for Inputs:
    If you have to different inputs for your function, you can't simplify them by dropping the constants. Instead you have to combine them:
        # O(a + b)
        def print_items(a,b): #different terms a & b cannot be easily dropped
            for i in range(a):
                print(i)
            for j in range(b):
                print(j)
        # for a nested for loop, it becomes O(a*b):
          def print_items(a,b):
            for i in range(a):
                for j in range(b):
                    print(i,j)
------------------------------------------------
CALCULATING Big O Notation:
1. remove constants: ## find example ##
2. Assign different variables for different inputs
3. Remove smaller terms (keep the term that increases faster.)

ALT calculate big O:
Break your algorithm/function into individual operations
Calculate the Big O of each operation
Add up the Big O of each operation together
Remove the constants
Find the highest order term — this will be what we consider the Big O of our algorithm/function
--------------------------------------------------
O(1) ## Constant Time ##
    even a n increases, the number of operations remains constant.
Line: straight across the bottom axis
--------------------------------------------------
O(n) ## Proportional ##
Time is equal to the length of the input.  
Line: LINEAR, creates a 45 degree straight line  
"""
# Example is a simple for loop


def print_items(n):
    for i in range(n):
        print(i)


""""
O(n), continued

- first rule: Drop constants. O(2n) simplifies to O(n).
	Constants are actual numbers, not variables.
"""
# Example is having 2 for loops in one function:


def print_items(n):
    for i in range(n):
        print(i)
        for j in range(n):
            print(j)


# evaluates to Big O(2n), and we drop the constant 2, leaving O(n)
"""
----------------------------------------------------------
O(n^2) ## Loop wothin a loop ## 
QUADRATIC: all n^x complexites are simplified as qudratic. So O(n^3), O(n^4) simplify down to O(n^2).
Line: steeply increases up the y-axis.
# example is a nested loop
	# The algorithm's runtime grows proportionally to the square of the input size. 
	# When you graph a quadratic function, it creates a parabola (like a U or an upside-down U). It has the form f(x) = ax^2 + bx + c, where a, b, and c.
	Definition 2:
	Algorithms or operations that have quadratic time are identified as having to perform a linear time operation for each value in an input, not just for the input itself.
	
"""
# Example is a nested loop


def print_more_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print_more_items(10)
"""
------------------------------------------------------
O(n^3) == cubic (Evaluate as Quadratic)
------------------------------------------------------
O(log n) == logoritmic ## Divide and Conquer ## 

- works on SORTED data.
- split data on either side, check is value is bigger or smaller, repeat.
- 2^3 = 8 the same as log2 8 = 3: this says,'2 to the what power = 8?", or "how many times do you have to divide 8 by 2 to get down to one item?". The answer is '3'.
Line. runs along, and just above the X axis. The increase as n increases is barley perceptible.

-----------------------------------------------------
O(nlog n) 
Applies to 
-----------------------------------------------------
Factorial time: O(n!)
HORRIBLE: only comes about with badly writen code.

-----------------------------------------------------
Big O of lists: 
    Since lists are a built in data structure, it's common to compare other DS's to them!

for the operations:
    my_list.append(n) & my_list.pop()
these == O(1).
for my_list.pop(3) OR my_list.insert(0,n), the index is no longer correct, so the whole array needs to be re-indexed, so it is O(n).

----------------------------------------------------
Big O comparisons:
If n == 1000
    O(1) == 1
    O(log n) == 10
    O(n) == 1,000
    O(n^2) == 1,000,000
Conclusion, O(n^2) is inefficient, so it should be simplified when possible at least to O(n).
"""
"""
---------------------------------------------------------
---------------------------------------------------------
#########################	
##### Big Omega (Ω) #####
#########################
Behavior of an algorithm in the best case
	using 'Ω' for Big Omega notation is based on the mathematical convention representing the lower bound of a function.
	In the context of time complexity analysis, the lower bound represents the minimum amount of time an algorithm takes to solve a problem for a given input size.
	
"""


"""
---------------------------------------------------
---------------------------------------------------
#########################
##### Big Theta (Θ) #####
#########################
The average runtime of an algorithm.
"""
"""
---------------------------------------------------
#########################
### SPACE COMPLEXITY: ###
#########################
according to https://www.bigocheatsheet.com/

## DATASTRUCTURE Space Complexity ##
All common data structures have the same space complexity:
O(n)
EXCEPT for a Skip List, which has the complexity of:
O(n log(n))

"""
