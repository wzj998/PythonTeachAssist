# print("Hello")
StrLine = input()
A = int(StrLine.split()[0])
B = int(StrLine.split()[1])
Sum = A + B
# print(Sum)

bNonNegative = (A+B >= 0)
# print(bNonNegative)

StrSum = str(abs(Sum))
# print(StrSum)

StrAns = ""
CountFromRight = 0
for i in range(len(StrSum) - 1, -1, -1):
    # print(i)

    if CountFromRight % 3 == 0 and CountFromRight != 0:
        StrAns = "," + StrAns
    StrAns = StrSum[i] + StrAns
    CountFromRight += 1

if not bNonNegative:
    StrAns = "-" + StrAns
print(StrAns)




