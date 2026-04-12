n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    print(a if b == c else c if a == b else b)
