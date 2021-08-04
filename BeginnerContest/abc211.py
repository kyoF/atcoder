# a
# a,b = map(int, input().split(' '))
# print((a-b)/3+b)

# b
# s = ''
# check_list = ['H','2B','3B']
# for _ in range(4):
#     s += input()
# if 'HR' in s:
#     s = s.replace('HR', '')
# else:
#     print('No')
#     exit()
# for check_s in check_list:
#     if check_s in s:
#         continue
#     else:
#         print('No')
#         exit()
# print('Yes')
# 別解
# s = set()
# for _ in range(4):
#     s.add(input())
# print('Yes' if len(s)==4 else 'No')

# c
# S = input()
# tar = "chokudai"
# mod = 10**9+7
# dp = [[0 for _ in range(len(tar)+1)] for _ in range(len(S)+1)]
# for i in range(len(S)+1):
#     dp[i][0] = 1
# for i in range(len(S)):
#     for j in range(len(tar)):
#         if S[i] != tar[j]:
#             dp[i+1][j+1] = dp[i][j+1]
#         if S[i] == tar[j]:
#             dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod
# print(dp[len(S)][len(tar)])
