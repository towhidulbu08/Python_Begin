""" 
01. function
02. function with default parameter
03. function with keyword argument
04. function with positional arguments
05. function with return value
06. args and kwargs
07.tuple and dictionary
08.modules(different import)
09.scopes
10.built in modules(pyautogui and opencv) and functions

11. try , except, finally
12. file write , read, append operation

 """





def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
















# def all_num_multiply(*allnum):
#   print("The numbers are:")
#   result=0
#   for num in allnum:
#     result +=num
#     # print(result)
#   print(result)

# all_num_multiply(2,5,7,12,1)
  


def find_max(*allnum):
  if not allnum:
    return None, None
  return max(allnum),min(allnum)

maxNum=find_max("d")
print(maxNum)
