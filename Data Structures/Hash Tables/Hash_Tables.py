"""

Hash Tables store items in key_value pairs

USES--------
python dictionaries {} 

A hash table has empty slots or 'buckets': When we add a new element, the value will be mapped to a key with a 'hash function' 

Hash function: every time a hash function is applied, the same value is returned for the same input.

'Hashing' a key is  O(1)

Collisions: when we try to assign a value to a key which already has one. Collisions must be resolved
Methods:
 mydict.items() # return a list of key:value pairs in tuples
 mydict.get() # retrieve a value 
 def mydict # deletes a dictionary
 del mydict['key'] # deletes a key:value
 mydict.clear() # empties a dictionary

Loop through a dict:
for key, value in mydict.items():
 print(f"\nkey: {key}")
 print(f"value: {value}")

# loop through keys:
for key in mydict:
 print(key)

# loop through values:
 for value in mydict.values():
  print(value)
"""
