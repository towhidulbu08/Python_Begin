numbers=[12,45,65,23,89,78,11] # list

nums={12,45,56,12,89} # set
numbers_tuple=12,45,56,12,89 # tuple
marks={'physics':12,'che':45,'math':56} # dictionary



# total=sum(numbers)
total=0

for num in numbers:
  total+=num
#   # print(num)
# print(total)

for i,num in enumerate(numbers):
  print(i,num)

for num in nums:
  total+=num
# print(total)


for num in numbers_tuple:
  total+=num  
# print(total)


sum_of_num=0

for key in marks:
  val=marks[key]
  sum_of_num+=val
  # print(val)
# print(sum_of_num)

# for subject ,mark in marks.items():
#   print(subject,mark)

for alph in "Tamim":
  print(alph)