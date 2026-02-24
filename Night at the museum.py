s = input()

current = 'a'
total = 0

for c in s:
    diff = abs(ord(c) - ord(current))
    step = min(diff, 26 - diff)
    total += step
    current = c

print(total)
