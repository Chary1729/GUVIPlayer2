m=input()
def countchar(some):
  count=0
  for i in some:
    if(some.count(i)>count):
      count=some.count(i)
      temp=i
      
  print(temp)
      
countchar(m)
