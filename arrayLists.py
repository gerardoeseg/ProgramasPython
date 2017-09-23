# Showing de basic data types and variables on Python
# Types of lists, lists on Python are variables that store arrays, inside
# each position can have a different data type
# Extracted from: https://goo.gl/vnT6hp

# Ordered collection / arrays or vectors
l = [2, "three", True, ["uno", 10]]
print l

# Access to a specific elements
l2 = l[1]
print l2

# Access to a nested list
l3 = l[3][0]
print l3

# A new value of a list element
l[1] = 4
print l
l[1] = "tres"

# Get a specific element range
l3 = l[0:3]
print l3

# Get a range of specific elements
l4 = l[0:3:2]
print l4

l5 = l[1::2]
print l5
