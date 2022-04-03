list_num = []
for number in range(1, 1000, 2):
    list_num.append(number ** 3)
list_sev = []
for ind, num in enumerate(list_num):
    sum_fig = 0
    while num > 0:
        sum_fig = sum_fig + num % 10
        num = num // 10
    if sum_fig % 7 == 0:
        list_sev.append(list_num[ind])
print(sum(list_sev))
list_sev.clear()
for ind, num in enumerate(list_num):
    list_num[ind] = list_num[ind] + 17
for ind, num in enumerate(list_num):
    sum_fig = 0
    while num > 0:
        sum_fig = sum_fig + num % 10
        num = num // 10
    if sum_fig % 7 == 0:
        list_sev.append(list_num[ind])
print(sum(list_sev))
