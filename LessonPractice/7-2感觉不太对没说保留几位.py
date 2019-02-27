str_split = input().split()
a = float(str_split[0])
b = float(str_split[1])
c = float(str_split[2])
ans = b * b - 4 * a * c
if float(round(ans)) == ans:
    ans = round(ans)
print(ans)


