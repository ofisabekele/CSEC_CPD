import math

Y, W = map(int, input().split())

m = max(Y, W)

win = 6 - m + 1

g = math.gcd(win, 6)

print(str(win // g) + "/" + str(6 // g))
