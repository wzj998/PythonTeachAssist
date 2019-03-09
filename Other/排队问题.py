import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from mpl_toolkits.mplot3d import axes3d


def f1(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)
    # ans = 0

    # return ans


def f2(x_now, y_now):
    ans = 0
    if x_now >= 0:  # 甲在0s及以后去排队
        if x_now > y_now:
            ans = 1  # 等1s 或者 拿不到盒饭(T2-T1)*k==1
            pass
        elif x_now == y_now:
            ans = (0+1)*0.5  # 同时到，随机决定先后，要么不用等要么等1s((T2-T1)*k==1)
            pass
        else:
            ans = 0  # 肯定不用等
        pass
    else:
        if x_now > y_now:
            ans = 1  # 也是1，-(-0.5)<1所以不会等完上一位还没到饭点
            pass
        elif x_now == y_now:
            ans = (-x_now+1)*0.5  # 和 x_now >= 0的同时到情况同理，然而先到需要等-x_now
            pass
        else:
            ans = -x_now  # 先到需要等到饭点
        pass
    return ans

n = 16

# 用meshgrid生成一个二维数组
x, y = np.meshgrid(np.linspace(-1.0, 0.5, n), np.linspace(-1.0, 0.5, n))

z = f1(x, y)  # (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)
# print(z)



for i_x in range(n):
    for i_y in range(n):
        xx = -1 + (0.5 - (-1))*i_x / (n-1)
        yy = -1 + (0.5 - (-1)) * i_y / (n - 1)
        # print(xx, yy)
        z[i_x][i_y] = f2(xx, yy) - f2(yy, xx)
for i_x in range(n):
    for i_y in range(n):
        print(z[i_x][i_y], end=',')
    print()

p_null_space = scipy.linalg.null_space(z)  # 求出一组可行解（还未满足概率和为1但是成比例的）
sum_p_null_space = sum(p_null_space)[0]
print("sum_p_null_space =", sum_p_null_space)
p_fianl = p_null_space * 1.0 / sum_p_null_space  # 乘上相应比例，使得和为1
for i in range(len(p_null_space)):
    print(p_fianl[i][0])
print("sum_ =", sum(p_fianl)[0])

yansuan = np.dot(z, p_fianl)  # 验算乘回去是不是0
for i_x in range(n):
    for i_y in range(1):
        print(yansuan[i_x][i_y], end=',')
    print()

ax = plt.gca(projection='3d')  # 返回的对象就是导入的axes3d类型对象
plt.title('3D Surface', fontsize=20)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
plt.tick_params(labelsize=10)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='jet')

plt.show()