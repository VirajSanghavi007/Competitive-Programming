s = str(input())
leng = len(s)
hello = ['e', 'l', 'l', 'o']
lst = []
x = 0

h = s.find('h')

for i in range(h, leng):
    if hello == []:
        break
    elif s[i] == hello[x]:
        hello.remove(hello[x])

if(hello == []):
    print("YES")
else:
    print("NO")