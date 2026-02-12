s = input()

upper_count = 0
lower_count = 0

for ch in s:
    if ch.isupper():
        upper_count = upper_count + 1
    else:
        lower_count = lower_count + 1

if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())
