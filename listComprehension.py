# List comprehension is a concise and powerful technique that can work on list elements

a = [ 2,3,4,6,7,8,9, 11]

# Create a new list built from selected elements of x (those whose value is >7). 
# For each element, thats found, make a new list with double the value of that element

b = [ x*2 for x in a if x > 7]

print b
