"""
FizzBuzz with list comprehension and ternary operator

List Copmprehension syntax:
[expr for item in iterable]                 # basic
[expr for item in iterable if condition]    # with filter
[expr2 for item2 in iter2 for item1 in iter1]  # nested

Ternary Operator Syntax:

result = a if cond1 else b if cond2 else c

"""

""" Trad style
def fizzBuzz(n: int):

    answer = []

    for i in range(1,(n+1)):
        print(i)
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(i)
    return answer

"""
# With Ternary operator:
"""
def fizzBuzz(n: int):

    answer = []
    
    for i in range(1,n+1):
        answer.append("FizzBuzz" if  (i % 3 == 0 and i % 5 == 0) else "Fizz" if (i % 3 == 0) else "Buzz" if (i % 5 == 0) else i)
    
    return answer        
"""

# With List Comprehension and Ternary operator:
"""
def fizzBuzz(n: int):
    answer = [
        (
            "FizzBuzz"
            if (i % 3 == 0 and i % 5 == 0)
            else "Fizz" if (i % 3 == 0) else "Buzz" if (i % 5 == 0) else f"{i}"
        )git 
        for i in range(1, n + 1)
    ]
    return answer
"""


def fizzBuzz(n: int):
    base = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]
    q, r = divmod(n, 15)
    return base * q + base[:r]


print(fizzBuzz(3))
