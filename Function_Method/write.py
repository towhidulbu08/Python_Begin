with open("message.txt",'a') as fileWrite:
  fileWrite.write("Again from hello")


with open("message.txt",'r') as fileRead:
  text=fileRead.read()
  print(text)