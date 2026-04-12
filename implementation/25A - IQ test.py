n = int(input())
a = list(map(int, input().split()))

even = [i for i in a if i % 2 == 0]
odd = [i for i in a if i % 2 != 0]

if len(even) == 1:
    print(a.index(even[0]) + 1)
else:
    print(a.index(odd[0]) + 1)
