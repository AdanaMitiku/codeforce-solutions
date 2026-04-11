a=input()
b=input()
e=""
for i in range(len(a)):
    if a[i]==b[i]:
        e+="0"
    else:
        e+="1"
print(e)
