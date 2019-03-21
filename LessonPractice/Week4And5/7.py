a_str = input().split()[1:]
# print(a_str)
a = [0] * len(a_str)
count_by_number = {}
for i in range(len(a_str)):
    a[i] = int(a_str[i])
    if a[i] in count_by_number:
        count_by_number[a[i]] += 1
    else:
        count_by_number[a[i]] = 1
ans_number = 0
ans_count = 0
for key_now in count_by_number:
    # print(key_now, count_by_number[key_now])
    if count_by_number[key_now]>ans_count:
        ans_count = count_by_number[key_now]
        ans_number = key_now
print(ans_number, ans_count)


