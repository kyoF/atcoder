# ABC087B Coins
import itertools as it
a, b, c, x = map(int, [input() for _ in range(4)])
count = 0
for a, b, c in it.product(range(a+1), range(b+1), range(c+1)):
    if 500*a + 100*b + 50*c == x:
        count += 1
print(count)