num=int(input())
arr=[int(x) for x in input().split()]
if(len(arr)==num):
  for i in arr:
    if(arr.count(i)<=1):
      count=arr.count(i)
      temp=i
  print(temp)
