# ABC083B Some Sums
n, a, b = map(int, input().split())
# total = 0
# for i in range(1, n+1):
#     if a <= sum(list(map(int, str(i)))) <= b:
#         total += i
# print(total)
print(sum(i for i in range(1,n+1) if a<=sum(map(int, str(i)))<=b))