# # 0. PracticeA Welcome To AtCoder
# a = int(input())
# b, c = map(int, input().split())
# s = input()
# print(a+b+c, s)

# # ABC086A Product
# a, b = map(int, input().split())
# print("Odd" if a%2 and b%2 else "Even")

# # ABC081A Placing Marbles
# print(input().count("1"))

# # ABC081B Shift only
# _ = input()
# l = [*map(int, input().split())]
# count = 0
# while not any(i%2 for i in l):
#     l = [i/2 for i in l]
#     count += 1
# print(count)

# ABC087B Coins
# import itertools as it
# a, b, c, x = map(int, [input() for _ in range(4)])
# count = 0
# for a, b, c in it.product(range(a+1), range(b+1), range(c+1)):
#     if 500*a + 100*b + 50*c == x:
#         count += 1
# print(count)

# ABC083B Some Sums
# n, a, b = map(int, input().split())
# # total = 0
# # for i in range(1, n+1):
# #     if a <= sum(list(map(int, str(i)))) <= b:
# #         total += i
# # print(total)
# print(sum(i for i in range(1,n+1) if a<=sum(map(int, str(i)))<=b))

# ABC088B Card Game for Two
# # n = int(input())
# # c = list(map(int, input().split()))
# # a=0
# # b=0
# # count=1
# # for i in sorted(c, reverse=True):
# #     if count%2==1:
# #         a+=i
# #     else:
# #         b+=i
# #     count+=1
# # print(a-b)
# _ = input()
# c = sorted(map(int, input().split()), reverse=True)
# print(sum(c[::2])-sum(c[1::2]))

# ABC085B - Kagami Mochi