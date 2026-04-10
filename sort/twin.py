n=int(input())
a=list(map(int,input().split()))
b=a[0]
c=1
for i in range(1,n):
    while b<=sum(a)//2:
        c+=1
        b+=a[i]

print(c)


