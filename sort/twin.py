n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

b = 0        
c = 0         
total = sum(a) 

for i in range(n):
    b += a[i]  
    c += 1
    if b > total // 2:  
        break

print(c)
