lists={'a','e','i','o','u'}
num=int(input())
inp=input()
if(len(inp)==num):
  for i in inp:
    if i in lists:
      inp=inp.replace(i,'')
      inp=inp[::-1]
    else:
      inp=inp[::-1]

print(inp)
  
  
  
  
