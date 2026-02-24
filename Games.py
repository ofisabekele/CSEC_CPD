n = int(input())

home = []
guest = []

for i in range(n):
    h, a = map(int, input().split())
    home.append(h)
    guest.append(a)

count = 0

for i in range(n):
    for j in range(n):
        if i != j:
            if home[i] == guest[j]:
                count += 1

print(count)
