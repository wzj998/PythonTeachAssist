def is_passed(id_now):
    # print(id_now)
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # id_array_str = list(id_now)
    sum_now = 0
    for i in range(len(weight)):
        if 9>=ord(id_now[i]) - ord('0') >=0:
            pass
        else:
            return False
        # print(i, id_now[i])
        sum_now += weight[i] * int(id_now[i])
    Z = sum_now % 11

    zm = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

    M = zm[Z]

    if M == id_now[len(id_now) - 1]:
        return True
    else:
        return False

    pass


n = int(input())
ids = [''] * n
all_passed = True
for i in range(n):
    ids[i] = input()
    if is_passed(ids[i]):
        pass
    else:
        all_passed = False
        print(ids[i])
if all_passed:
    print("All passed")
