# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

def last(n):
    return n[-1]

def sort(tuples):
    return sorted(tuples, key = last)

my_list = ([2,3], [4,6], [1,5], [8,2], [7,1])
print("my_list:")
print(my_list)
print("Sorted:")
print(sort(my_list))