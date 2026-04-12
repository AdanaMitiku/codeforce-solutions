n = int(input())

x = list(map(int, input().split()))[1:]
y = list(map(int, input().split()))[1:]

z = x + y
b = set(z)

c = set(range(1, n + 1))

if b == c:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
