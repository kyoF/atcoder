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

# c
S = input()
tar = "abc"
mod = 10**9+7
dp = [[0 for _ in range(len(tar)+1)] for _ in range(len(S)+1)]
for i in range(len(S)+1):
    dp[i][0] = 1
for i in range(len(S)):
    for j in range(len(tar)):
        if S[i] != tar[j]:
            dp[i+1][j+1] = dp[i][j+1]
        if S[i] == tar[j]:
            dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod
print(dp)
# [
#     '' a b c
#     [1,0,0,0], ''
#     [1,1,0,0], a
#     [1,2,0,0], a
#     [1,2,2,0], b
#     [1,2,4,0], b
#     [1,2,4,4], c
#     [1,2,4,8], c
# ]
print(dp[len(S)][len(tar)])
