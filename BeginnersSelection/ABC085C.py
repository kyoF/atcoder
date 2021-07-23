# n, y = map(int, input().split(' '))
# for a in range(n+1):
#     for b in range(n+1):
#         for c in range(n+1):
#             if 10000*a + 5000*b + 1000*c == y and a+b+c == n:
#                 if n-a-b >= 0:
#                     print(f'{a} {b} {c}')
#                     exit()
# print('-1 -1 -1')

n, y = map(int, input().split(' '))
for a in range(n+1):
    for b in range(n+1):
        if 10000*a + 5000*b + 1000*(n-a-b) == y:
            if n-a-b >= 0:
                print(f'{a} {b} {n-a-b}')
                exit()
print(f'{-1} {-1} {-1}')