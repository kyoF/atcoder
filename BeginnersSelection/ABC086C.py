# import sys
# count = int(input())
# t, x, y = [], [], []
# loop_num, pre_time, place_sum = 0, 0, 0

# for idx in range(count):
#     tnum, xnum, ynum = map(int, input().split(' '))
#     t.append(tnum)
#     x.append(xnum)
#     y.append(ynum)

# for idx, time in enumerate(t):
#     loop_num = time - pre_time
#     pre_time = time
#     for i in range(loop_num):
#         if place_sum < x[idx]+y[idx]:
#             place_sum += 1
#         elif place_sum > x[idx]+y[idx]:
#             place_sum -= 1
#         else:
#             place_sum += 1
#             if i+1 == loop_num and place_sum == x[idx]+y[idx]:
#                 break
#         if place_sum != x[idx]+y[idx] and i+1 == loop_num:
#             print('No')
#             sys.exit()
# print('Yes')

count = int(input())
info = []
loop_num = pre_time = place_sum = 0
for idx in range(count):
    info.append(list(map(int, input().split(' '))))
for lst in info:
    loop_num = lst[0] - pre_time
    pre_time = lst[0]
    for i in range(loop_num):
        if place_sum < lst[1]+lst[2]:
            place_sum += 1
        elif place_sum > lst[1]+lst[2]:
            place_sum -= 1
        else:
            place_sum += 1
            if i+1 == loop_num and place_sum == lst[1]+lst[2]:
                break
        if place_sum != lst[1]+lst[2] and i+1 == loop_num:
            print('No')
            exit()
print('Yes')
