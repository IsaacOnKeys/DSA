"""
first, you start with your array of numbers:
myArray = [31,2,30,1,100,0]

then you plug each into this formula, the resulting integer is the index of the "bucket" which it should go into.
num = current value
max =  largest value in the array
n = len(myArray)
normalized = num / (max + 1)
bucketNo = int(n*normalized)

Then Bucket Sort uses "insertion" sort



"""
