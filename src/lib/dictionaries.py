# learning about dictionaries
# Unordered mappings of storing objects
# List:
# 1. stores objects in an ordered sequence
# 2. Ordered
# 3. Can be sorted, ondexed, sliced
# 4. []
# 5. Objects retrieved by exact index location


# Dictionaries:
# 1. Stores objects in the key:value pair
# 2. Unordered
# 3. Cannot be sorted
# 4. {}
# 5. Objects retrieved by the exact key
# 6. Dictionaries are not immutable

# Tuples
# Similar to lists , bbut they are immutable
# ()


my_dict = {"key1" : "Value1" , "Key2" : "Value2" }
print(my_dict['key1'])

grocery_prices = {"Milk" : 5.99 , "Apples" : 2.99 , "Oranges" : 1.99 }
print(grocery_prices['Milk'])

mixed_dict = {"k1" : 2.10 , "k2" : [1,2,3,4] , "k3" : { "SubDictKey1" : "Subvalue1" , "SubDictKey2" : 100 } }
print(mixed_dict["k1"])
print(mixed_dict["k2"])
print(mixed_dict["k3"])

print(mixed_dict["k2"][0])
print(mixed_dict["k2"][1])
print(mixed_dict["k2"][2])
print(mixed_dict["k2"][3])
print(mixed_dict["k2"][-1])
print(mixed_dict["k2"][-2])
print(mixed_dict["k2"][-3])
print(mixed_dict["k2"][-4])
print(mixed_dict["k2"][0])


print(mixed_dict["k3"]["SubDictKey1"])
print(mixed_dict["k3"]["SubDictKey2"])

d = {"k1": 1 , "k2" : 2}
print(d)

d["k3"] = 3
print(d)

d["k1"] = "Updated Value"
print(d)

print(d.keys())
print(d.values())
print(d.items())
