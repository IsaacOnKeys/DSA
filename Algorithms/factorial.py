import time
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

start = time.time()
myfact = factorial(999)
end = time.time()

totaltime = end - start

print(f"the answer is: {myfact}\n  \
    it took {totaltime}" )
