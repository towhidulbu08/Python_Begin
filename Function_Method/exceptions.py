# num2=int(input("Enter a number: "))

# result=20/num2
# print(result)
# print("Done")


# text="Anis"
# print(text[4])
# print("Done")



try:
  list=[20,0,30]

  result=list[0]/list[3]

  print(result)
  print("Done")

except ZeroDivisionError:
  print("Dividing by zero is not possible")