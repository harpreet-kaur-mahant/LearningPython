# Sets: unordered collections of unique objects

my_set = set()
print(my_set)
print(type(my_set))

my_set.add(1)
print(my_set)

my_set.add(2)
print(my_set)

my_set.add(2)
print(my_set)

my_list = [3,3,3,3,4,4,4,2,2,2,1,1,1,1,5,5,5,6,7,9,8,10]
print(my_list)
print(set(my_list))