# def square(x):
#   return x*x


square=lambda x:x*x


result=square(6)
# print(result)


add=lambda x,y:x+y


output=add(5,6)


# print(output)




numbers=[12,45,65,23,89,78,11]




def double_it(x):
  return x*2


double_it2=lambda x:x*2


# doubled_numbers=map(double_it,numbers)
doubled_numbers=map(lambda x:x*2,numbers)
squared_numbers=map(lambda x:x*x,numbers)


# print(numbers)
# print(list(squared_numbers))




bigger_numbers=filter(lambda f:f%2==0,numbers)
# print(numbers)
# print(list(bigger_numbers))




actors=[
  {'name':'sakib','age':29},{"name":"mama",'age':56},
  {'name':'ahil','age':24},{"name":"miyaji",'age':45},
  {'name':'salman','age':34},{"name":"saikot",'age':27},
  ]


senior_person=filter(lambda person:person["age"]>38,actors)


junior_person=filter(lambda person:person["age"]<35,actors)


print(list(junior_person))


print(list(senior_person))











