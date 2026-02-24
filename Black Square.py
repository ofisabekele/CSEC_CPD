a1, a2, a3, a4 = map(int, input().split())
s = input()

total = 0

for c in s:
    if c == "1":
        total += a1
    elif c == "2":
        total += a2
    elif c == "3":
        total += a3
    elif c == "4":
        total += a4

print(total)
