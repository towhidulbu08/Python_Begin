largest=max(45,89,54,116,-12)
nums={12,45,56,12,89}
numbers=[12,45,56,89,78,11]


big_nums=max(nums)
# print(big_nums)
num_reversed=reversed(numbers)
# print(list(num_reversed))


sorted_numbers=sorted(numbers,reverse=True)


# print(sorted_numbers)




actors=[
  {'name':"Taimur","age":34},
  {'name':'Alamgir','age':38},
  {
    'name':"Babur",'age':56
  },
  {
    'name':"Isha Kha",'age':78
  }
]




# sorted_actors=sorted(actors,key=lambda actor:actor['age'],reverse=True)
sorted_actors=sorted(actors,key=lambda actor:actor['name'],reverse=True)
# print(sorted_actors)


friends=["Rafiq","Jamal","Salam","Kalam","Balam","Abir"]


# sorted_friends=sorted(friends)
sorted_friends=sorted(friends,reverse=True)
print(sorted_friends)

