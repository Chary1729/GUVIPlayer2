
num=int(input())
inp=input()
lists={'a','e','i','o','u'}
if(len(inp)==num):
  for i in lists:
    if i in inp:
      inp=inp.replace(i,'')
      inp=inp[::-1]
#       print('working')
    else:
      inp=inp[::-1]
#       print('not working')
  print(inp)
  
  
  
  
