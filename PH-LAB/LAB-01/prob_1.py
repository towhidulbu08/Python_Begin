""" 
Clean the data and get a String output 'a e i o u'

 """


data="aNtEriOur\n\t>>"

new_data=data.lower()

output_data=''



for ch in new_data:
  # print(ch)
  if ch =='a' or ch=='i' or ch=='u'or ch=='e' or ch=='o':
    print(f'{ch} found')
    if len(output_data)==10:
      break
    output_data +=f"{ch}_"
print((output_data))