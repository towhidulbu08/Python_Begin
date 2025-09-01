def calculate(a,*p,**z):
  print(a)
  print(p)
  print(z)
  for key,value in z.items():
    print(key,value)

# calculate("tamim",6,name="sakib",b=4)


def  show(a,b,c,*args,**kargs):
  print(a)
  print(args)
  for key,value in kargs.items():
    print(key,value)




