def full_name(f_name,l_name):
  name=f"{f_name} {l_name}"
  return name

name=full_name(l_name='chowdhury',f_name='khan')
# print(name)



def long_name(**kargs):
  print(kargs)

# long_name(first='Dr. ', last='Chowdhury', middle="Rahman")


def name_mixed(first,last,**name_parts):
  print(first,last,name_parts)


# name_mixed("tamim",last='islam',middle="akidah",)


def all_types (first,*args,**kargs):
  print(first)
  for word in args:
    print(word)
  print(kargs)
  for key,value in kargs.items():
    print(key,value)


all_types(1,2,3,4,5,"a",'b',name="abba",age=35)


    
