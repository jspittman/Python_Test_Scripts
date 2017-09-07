import functools
from functools import reduce # this is for reduce


tup_1 = 1, 2, "me"
tup_2 = tup_1
tup_3 = tup_2
print(tup_1 is tup_2 is tup_3)

#######


"""
l = [1,2,3]
q = sum_list(l)
print(q)
"""

# THIS IS COOL!
list_1 = [1,2,3,4]
list_2_iter = filter(lambda x: x % 2 == 0, list_1)
list_2 = list(list_2_iter)
print(list_1)
print(list_2)

#bug in this code
'''
list_3_item = map(lambda x: x *2, list_1)
list_3 = list(list_3_iter)
print(list_3)
'''


# reduce -- where is the new list created?
list_10 = [1,2,3,4]
reduce(lambda x, y: x + y, list_10)
print (list_10)

big_list = list(range(1000))
reduce(lambda x, y: x +y, big_list)

dna = ["aaa","bbb","ccc"]


### awesome ###
a_count = reduce(lambda a, x: a +x.count("a"), dna, 0)
print (a_count)

