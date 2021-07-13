# ABC088B Card Game for Two
# n = int(input())
# c = list(map(int, input().split()))
# a=0
# b=0
# count=1
# for i in sorted(c, reverse=True):
#     if count%2==1:
#         a+=i
#     else:
#         b+=i
#     count+=1
# print(a-b)
_ = input()
c = sorted(map(int, input().split()), reverse=True)
print(sum(c[::2])-sum(c[1::2]))