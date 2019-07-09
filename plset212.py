N,K=map(int,input().split())
inp=[int(x) for x in input().split()]
for i in range(0,K):
    inp=[inp[-1]]+inp[:-1]
print(*inp)
