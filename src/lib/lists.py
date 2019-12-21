integer_list = [1,2,3]
hetrogeneous_list = ["string" , 0.1 ,True ]
list_of_lists = [integer_list , hetrogeneous_list , [] , {}]

integer_list_length = len(integer_list)
hetrogeneous_list_length = len(hetrogeneous_list)
list_of_lists_length = len(list_of_lists)

print(integer_list_length)
print(hetrogeneous_list_length)
print(list_of_lists_length)

#Indexing the list
rangeList = [0,1,2,3,4,5,6,7,8,9,10]
print(rangeList)

#Getting the value of list items using indexing
zero = rangeList[0]
print(zero)

one = rangeList[1]
print(one)

ten = rangeList[-1]
print(ten)

nine = rangeList[-2]
print(nine)

#Slicing the list
first_three = rangeList[:3]
print(first_three)

last_three = rangeList[6:]
print(last_three)

#Append items to the list
rangeList.append(11)
print(rangeList)

rangeList.append(12)
print(rangeList)

#Append items from the end of  the list
rangeList.pop()
print(rangeList)

rangeList.pop()
print(rangeList)

#Assigning the list values using index
rangeList[0] = -1
setZeroIndex = rangeList[0]
print(setZeroIndex)
print(rangeList)

#Removing the list value by specifying its index
rangeList.pop(0)
print(rangeList)

#New lists to understand sort and reverse
num_list = [5,3,6,8,2,9,4,1]
words_list = ['cat' , 'dog' , 'apple' , 'bat' , 'egg' , 'fish']

#Sort list according to numeric order
num_list.sort()
print("Sorted Num List")
print(num_list)

#Reverse the items in the list
num_list.reverse()
print(num_list)

#Sort list according to alphabetic order
words_list.sort()
sorted_words_list = words_list
print(sorted_words_list)

#Reverse the items in the list
sorted_words_list.reverse()
print(sorted_words_list)

#concatenation of lists
mixed_list = num_list + sorted_words_list
print(mixed_list)
