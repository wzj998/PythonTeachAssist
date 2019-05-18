import functools

a = input()
b = input()
da = eval(a)
db = eval(b)
ans = eval(a)

for i in db:
    if i in da:
        ans[i] = da[i] + db[i]
    else:
        ans[i] = db[i]

keys = []
for i in ans:
    keys.append(i)


def cmp0(s1, s2):
    if isinstance(s1, str):
        s1 = ord(s1)
    if isinstance(s2, str):
        s2 = ord(s2)

    if s1 < s2:
        return -1
    if s1 > s2:
        return 1
    return 0


keys = sorted(keys, key=functools.cmp_to_key(cmp0))
# print(keys)

print("{", end="")
index = -1
for i in keys:
    index += 1
    if isinstance(i, str):
        print("\"" + i + "\"", end="")
    else:
        print(str(i), end="")
    print(":" + str(ans[i]), end="")

    if index < len(keys) - 1:
        print(",", end="")

    pass
print("}", end="")
