str = input()
index_jin = str.index("#")
str = str[0:index_jin]
str_ = ""
index_1st_16 = -1
index_1st_minus = -1
is_negative = False
index = 0
for chr in str:
    chr = chr.lower()
    if 0 <= ord(chr) - ord('0') <= 9:
        str_ += chr
    elif chr in ['a', 'b', 'c', 'd', 'e', 'f']:
        str_ += chr
        if index_1st_16<0:
            index_1st_16 = index
        # if index_1st_16 > 0:
        #     if str[index_1st_16 - 1] == '-':
        #         is_negative = True
        # pass
    elif chr == '-':
        if index_1st_minus<0:
            index_1st_minus = index
        pass
    index += 1

if str_ == "":
    # ans = ""
    ans = 0
else:
 ans = int(str_, 16)
# print(index_1st_minus, index_1st_16)
is_negative = index_1st_minus < index_1st_16 and index_1st_minus >= 0 and index_1st_16 >= 0
if is_negative:
    ans = -ans
print(ans)
