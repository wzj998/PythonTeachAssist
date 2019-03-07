array_now = input().split()
for i in range(len(array_now)):
    array_now[i] = int(array_now[i])
array_now.sort()
for i in range(len(array_now)):
    if i == len(array_now) - 1:
        print(array_now[i], end="")
    else:
        print(array_now[i], end="->")

