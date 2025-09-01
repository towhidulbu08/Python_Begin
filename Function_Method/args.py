def add(a,b):
  total=a+b
  print(f'a: {a} and b: {b}')
  return total
# result=add(12,14)
# result=add(b=12,a=14)


def multiply (a,d,b=23,c=30):
  result=a*b
  return result

output=multiply(45,2)
# print(output)

def multiply2(*numbers):
  result=1
  for num in numbers:
    result =result*num
  return result

final_result=multiply2(12,2,3,5,-6)
print(final_result)



def add(a,b,*numbers):
  print(a,b)
  print(numbers)

add(3,4,5,6,7,8,9,10)