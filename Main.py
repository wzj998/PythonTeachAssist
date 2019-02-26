class PolyNode:  # 多项式节点
    n = 0
    a = 0

    def __init__(self, n, a):
        self.n = n
        self.a = a
        pass
    pass


class PolyLine:  # 一行多项式
    nodes = []  # 每一项
    k = 0  # 有多少项

    # 可能用字典更科学哦 不过最多10项问题不大

    def combine(self):  # 合并同类项 合并完排序
        dict_n_a = {}  # key是指数 value是系数
        for each in self.nodes:
            if each.n in dict_n_a:  # has_key 过时了
                dict_n_a[each.n] += each.a
                pass
            else:
                dict_n_a[each.n] = each.a
                pass

        knew = len(dict_n_a.keys())
        for key_now in dict_n_a:  # 删掉0的项
            a_now = dict_n_a[key_now]
            if a_now == 0:
                knew -= 1

        self.k = knew
        self.nodes = [PolyNode(0, 0)] * knew

        i = 0
        for key_now in dict_n_a:
            a_now = dict_n_a[key_now]
            if a_now == 0:
                continue
            self.nodes[i] = PolyNode(key_now, a_now)
            i += 1
            pass

        self.nodes.sort(key=lambda each_node: each_node.n, reverse=True)

        pass

    def add(self, other):
        ans = PolyLine()
        ans.k = self.k
        ans.nodes = [PolyNode(0, 0)] * ans.k
        for i in range(0, ans.k, 1):
            ans.nodes[i] = self.nodes[i]

        ans.k += other.k
        ans.nodes.extend(other.nodes)  # 要用extend而不是append
        ans.combine()
        return ans
        pass

    def from_string(self, str_from):
        str_array = str_from.split(" ")
        self.k = int(str_array[0])
        self.nodes = [PolyNode(0, 0)]*self.k
        # print(len(self.nodes))
        index_node_start = 1
        for i in range(0, self.k, 1):
            n = float(str_array[index_node_start])
            a = float(str_array[index_node_start+1])
            self.nodes[i] = PolyNode(n, a)
            index_node_start += 2
        pass

    def to_string(self):  # 要注意精确到一位小数 不知道指数会不会是小数题目没说 好像也没说排序。。。
        ans = ""
        ans += str(self.k)  # + " "
        for each in self.nodes:
            # if each.a == 0: 放到combine弄吧
            #     continue
            ans += " " + str(int(each.n)) + " " + str(("%.1f" % each.a))
            pass
        return ans
        pass
    pass


def do_input(p1now, p2now):
    str1 = str(input())
    p1now.from_string(str1)
    str2 = str(input())
    p2now.from_string(str2)
    pass


def do_output(p1now, p2now):
    p_sum = p1now.add(p2now)
    # print(p1now.to_string())
    # print(p2now.to_string())
    print(p_sum.to_string())
    pass


p1 = PolyLine()
p2 = PolyLine()
do_input(p1, p2)
# print(p1.to_string())
# print('\n')
# print(p2.to_string())
do_output(p1, p2)




