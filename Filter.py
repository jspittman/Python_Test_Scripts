
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
