# ABC081B Shift only
_ = input()
l = [*map(int, input().split())]
count = 0
while not any(i%2 for i in l):
    l = [i/2 for i in l]
    count += 1
print(count)