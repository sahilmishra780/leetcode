## Notes from Neetcode Python crash course: https://www.youtube.com/watch?v=0K_eZGS5NsU

# Same variable can be assigned to different types
n = 0
n = 'abc';

# Multiple variable assignments
m, n, o = 0, "abc", False

# Increment
n = n + 1
n += 1

# Null
n = 4
n = None # every type is nullable

# if statements (needs indentation, no parentheses)
n = 1
if n > 2:
  n -= 1:
elif n == 2:
  n *= 2
else:
  n += 2

# Logical conditions
n = True and False # &&
n = True or False # ||

# While loops
n = 0
while n < 5:
  print(n)
  n += 1

# for loops
for i in range(5):
  print(i) # 0 to 4
for i in range(2,6):
  print(i) # 2 to 5
for i in range(5,1,-1):
  print(i) # 5 to 2

# Division
print(5 / 2) # 2.5, Float division by default
print(5 // 2) # 2, rounds down
# careful most language round to 0, but python just rounds down so negative numbers will round away from 0
print(-3 // 2) # -2
# to round towards 0
print(int(-3 / 2))

# Modulus
print(10%3) # standard 1
print(-10%3) # non-standard, -2, tricky behavior when using % on negative numbers, use math.fmod
import math
print(math.fmod(10, 3)) # standard -1

# Math helpers
import math
print(math.floor(/2)) # round down
print(math.ceil(/2)) # round up
print(math.sqrt(2))
print(math.pow(2, 3)) # 8

# INT_MAX, INT_MIN
float("inf")
float("-inf")

# Python never overflows
import math
print(math.pow(2,200))

# Arrays (lists in python)
arr = [1, 2, 3]
print(arr)

# Arrays are dynamic arrays, so can be used as a stack
arr.append(4)
arr.append(5)
print(arr)
arr.pop()
print(arr)

# Array supports insertion but O(n)
arr.insert(1,7) # insert 7 at pos 1 and shift everthing to right

# Supports indexing
print(arr[0])
arr[0] = -1

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# index -1 of array is last value, -2 is second last item and so on and so forth
arr = [1, 2, 3]
print(arr[-1])

# Array slicing
arr = [1, 2, 3, 4]
print(arr[1:3]) # slice arr from pos 1 to 2 (3 is not included like range)

# Unpacking
a, b, c = [1, 2, 3]

# Loop through arrays
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
  print(nums[i])

# Without index
for n in nums:
  print(n)

# With index and value, enumerate
for i, n in enumerate(nums):
  print(i, n)

# Loop through multiple arrays simultaneously with zipping and unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
# zip(nums1, nums2) basically results in [(1,2), (3,4), (5,6)]
for n1, n2 in zip(nums1, nums2):
  print(n1, n2)

# Reverse
nums = [1, 2, 3]
nums.reverse()

# Sort
arr = [5, 4, 7, 3, 8]
arr.sort() # asc
arr.sort(reverse = True) # desc
arr = ["bob", "alice", "jane", "doe"]
arr.sort() # sorted in lexical order
arr.sort(key=lambda x: len(x))

# List comprehension
arr = [i for in range(5)] # 0, 1, 2, 3, 4
arr = [2*i for in range(5)] # 0, 2, 4, 6, 8

# 2-D lists (4x4(
arr  = [[0] * 4 for i in range(4)]
# don't do this arr = [[0] * 4]* 4, the [0]*4 is duplicated as 4 rows but each row object is the same. so modifying 1 row will result in modifying all rows

# String
a = "abc"

# String slicing
print(s[0:2])

# Strings are immutable i.e. cannot reassign characters 
# s[1] = d # not possible

# Updating a string creates a new string
s += "def"

## Any modification to a string is considered an O(n) time operation

# Valid numeric strings can be converted
print(int("123"))

# Numers can be converted to strings
print(str(123))

# Ascii value of a char
print(ord("a"))

# Joining strings
strings = ["ab", "cd", "ef"]
print("".join(strings)), empty string delimiter
print("#".join(strings)), "#" delimiter

# Queues (double ended qs by default i.e. deques)
from collections import deque
q = deque()
q.append(1)
q.append(2) # append to right i.e. end
print(q)
q.popleft() # constant time, for list this O(n)
q.appendleft(1) # constant time, for list this O(n)
q.pop() # pop from right i.e. end

# Hashset or simply set, add, remove, find in const time, ensures no duplicates
mySet = set()
mySet.add(1)
mySet.add(2)
print(len(mySet)) # num of elements in set
print(1 in mySet) # true if 1 is in mySet, search is via "in" operator
mySet.remove(2) # remove in constant time

# Hardcoded set
mySet = {1, 2, 3};
# List to set
print(set([1, 2, 3])

# Set to comprehension
mySet = { i for i in range(5)}

# Hashmap or simply map or dict
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
# obv no duplicate keys
print(len(myMap)) # Len of dict gives number of keys in dict

myMap["alice"] = 80 # update value at key alice
print("alice" in myMap) # check if key "alice" exists in myMap
val = myMap.pop("alice") # removes key, value with key "alice", returns value with key "alice"
del myMap["bob"] # removes key, value with key "bob", no return value

# Hardcoded dict
myMap = {"alice": 88, "bob": 77}

# Dict comprehensions
myMap = {i: 2*i for i in range(3) } # for adjacency list

# looping through maps

# via keys
for key in myMap:
  print(key, myMap[key])

# via values
for val in myMap.values():
  print(val)

# via keys and values
for key, val in myMap.items():
  print(key, val)

# Tuples, like arrays but immutable
tup = (1, 2, 3)
print(tup(1))

# Use tuples as keys of a hashmap or a hashset (like coordinates)
myMap = {(1,2): 5} # map of coordinates and distance**2 # tuples are hashable keys
mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

# Lists can't be keys for hashsets or hashmaps

# Heaps
import heapq

# under the hood are arrays and are minheap by default
minHeap = []
heapq.heappush(minHeap, 3) # log N operation
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 1)
print(minHeap[0]) # min value i.e 1

while len(minHeap):
  print(heapq.heappop(minHeap)) # print curr min and pop it, popping is log N operation

# For maxheaps multiply -1 while writing and then multiply -1 while reading
maxHeap = [] # for 1, 2, 3
heapq.heappush(maxHeap, -1)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -3)
print(-1 * maxHeap[0]) # max value i.e 3

while len(maxHeap):
  print(heapq.heappop(-1 * maxHeap)) # print curr max and pop it

# Heapify a list in O(n)
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
  print(heapq.heappop(arr)) # prints values in ascending order from min to max

# Functions

def myFunc(n, m):
  return n * m;
print(myFunc(1, 2))

# Nested functions -> have access to outer variables
def outer(a, b):
  c = "c"
  def inner():
    return a + b + c;
  return inner()
print(outer("a", "b")


# Nested functions allow modifying objects but not reassign values unless using the nonlocal keyword
def double(arr, val):
  def helper():
    # Modifying array works
    for i, n in enumerate(arr):
      arr[i] *= 2
    
    # will only modify val in the helper scope
    # val += 2
    
    # this will modify val outside helper scope
    nonlocal val
    val *= 2
   helper()
   print(arr, val)

nums= [1, 2]
val = 3
double(nums, val)

# Classes
class MyClass:
   # Constructor
   def __init__(self, nums): # self is this keyword
      # Create member variables
      self.nums = nums
      self.size = len(nums)
   
   def getLength(self):
     return self.size
   
   def getDoubleLength(self):
    return 2 * self.getLenght()

   def __privateFunction(self):
    return 0;

class Person:
    def __init__(self, name="John Doe", age=30):
        self.name = name
        self.age = age

# Default constructor
p1 = Person()
print(p1.name, p1.age)  # Output: John Doe 30

# Parameterized constructor
p2 = Person("Alice", 25)
print(p2.name, p2.age)  # Output: Alice 25

    

  

  

