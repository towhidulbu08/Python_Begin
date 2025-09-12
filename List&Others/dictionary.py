
marks={'physics':12,'che':45,'math':56}
marks['che']=98
marks['english']=100
del marks['english']
# print(marks['che'])
# print(marks)
# marks_keys=marks.keys()
# marks_values=marks.values()
marks_items=marks.items()
# marks.clear()
print(marks_items)
# print(marks_values)
# print(marks_keys)






tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127



number=list(tel)
#print(number)#?['jack','sape','guido']

result='guido' in tel
notresult='jack'not in tel
# print(result)
# print(notresult)
