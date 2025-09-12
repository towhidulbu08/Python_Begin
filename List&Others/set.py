numbers=[12,45,56,12,89]
# print(numbers)

#set:don't allow duplication
nums={12,45,56,12,89}
# print(nums)
#? create set from list:
numbers_set=set(numbers)
print(numbers_set)

numbers_set.add(77)
numbers_set.add(45)
numbers_set.remove(12)
print(len(numbers_set))

