import collections
list = [11,45,8,11,23,45,23,45,89]
print('Original list ', str(list))
occur = collections.Counter(list)
print('Printing count of each item ', str(occur))
