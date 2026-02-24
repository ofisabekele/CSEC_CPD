s = input()
t = input()

position = 0

for c in t:
    if s[position] == c:
        position += 1

print(position + 1)
