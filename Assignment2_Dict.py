# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

dict_ascii = dict()
for i in range(97,123):
    dict_ascii[chr(i)] = i
    key = dict_ascii.keys()
    value = dict_ascii.values()
    print("ASCII Dict:", dict_ascii)
    n = str(input('enter the key ->'))
    print("key:", n)
    print("value:", dict_ascii[n])