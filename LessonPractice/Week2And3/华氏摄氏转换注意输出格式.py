def fahr2celsius(f):
    return 5*(f-32)/9


lower, upper = map(int, input().split())
if 0 < lower <= upper <= 100:
    print("fahr celsius")
    for t_now in range(lower, upper+1, 2):
        print("%d%6.1f" % (t_now, fahr2celsius(t_now)))
    pass
else:
    print("Invalid.")
