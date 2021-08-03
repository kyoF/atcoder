# # a
# a,b = map(int, input().split(' '))
# if a>0 and b==0:
#     print('Gold')
# elif a==0 and b>0:
#     print('Silver')
# else:
#     print('Alloy')

# b
# x = list(input())
# pre_item = ''
# counter = 0
# if x[0]==x[1]==x[2]==x[3]:
#     counter=3
# else:
#     for idx, num in enumerate(x):
#         if idx == 0:
#             pre_num = num
#         else:
#             if int(pre_num)+1 == int(num) or (num=='0' and pre_num=='9'):
#                 counter += 1
#                 pre_num = num
# print('Weak') if counter == 3 else print('Strong')

# c
n,m = map(int, input().split(' '))
list_a = [*map(int, input().split(' '))]
list_b = [*map(int, input().split(' '))]
result = -1
for a_item in list_a:
    for b_item in list_b:
        if result == -1 or abs(a_item - b_item) < result:
            result = abs(a_item - b_item)
print(result)

# d
q = int(input())
bag = []
min_num_list = []
for _ in range(q):
    action = input()
    if ' ' in action:
        action,num = map(int, action.split(' '))
    if action == 1:
        bag.append(num)
    elif action == 2:
        bag = map(lambda x:x+num, bag)
    else:
        min_num_list.append(min(bag))
        bag = bag.pop(bag.index(min(bag)))
for item in min_num_list:
    print(item)