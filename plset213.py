x=int(input())
sum=0
x=str(x)
for i in x:
  if(i.isdigit()==True):
    i=int(i)
    sum=sum+(i*i)
print(sum)  
