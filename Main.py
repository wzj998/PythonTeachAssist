class MyMap:
    n = 0
    m = 0
    dist = [[]]
    n_teams_by_city = []
    pass


class Question:
    c1 = 0
    c2 = 0
    pass


class Ans:
    shortest_dist = -1
    num_paths = 0
    # last_node_when_shortest = [[]] 怕是再dfs更科学
    n_teams_max = 0
    dist_from_c1 = []
    pass


def do_input(map_now, q):
    first_line = input()
    line_split = first_line.split()
    map_now.n = int(line_split[0])
    map_now.m = int(line_split[1])
    q.c1 = int(line_split[2])
    q.c2 = int(line_split[3])

    second_line = input()
    line_split = second_line.split()
    map_now.n_teams_by_city = [0] * map_now.n
    for i in range(0,map_now.n,1):
        map_now.n_teams_by_city[i] = int(line_split[i])

    map_now.dist = [([-1]*map_now.n) for i in range(map_now.n)]  # -1表示正无穷
    for i in range(map_now.n):
        map_now.dist[i][i] = 0  # 自己到自己是0
    for i in range(0,map_now.m,1):
        line_now = input()
        line_split = line_now.split()
        c1 = int(line_split[0])
        c2 = int(line_split[1])
        l = int(line_split[2])
        map_now.dist[c1][c2] = l
        map_now.dist[c2][c1] = l

    # for i in range(map_now.n):
    #     for j in range(map_now.n):
    #         print(map_now.dist[i][j], end=" ")
    #     print()

    pass


def do_dijkstra(map_now, c1, c2, ans_now):
    left_or_right = [False] * map_now.n  # left表示已经加入源点集合
    dist_from_c1 = [-1] * map_now.n
    # 先把c1加入源点集合
    left_or_right[c1] = True
    for i in range(map_now.n):
        dist_from_c1[i] = map_now.dist[c1][i]
    for t in range(map_now.n - 1):  # 还剩n-1轮循环要把所有点加入源点集合
        node_closest = -1  # 先找到右边集合离源点最近的
        min_dist_now = -1
        for i in range(map_now.n):
            if not left_or_right[i]:
                dist_now = dist_from_c1[i]
                # print("dist_from_c1",i,dist_now)
                if min_dist_now < 0 or (dist_now < min_dist_now and dist_now != -1):  # 要注意-1是正无穷
                    min_dist_now = dist_now
                    node_closest = i
        if min_dist_now == -1:
            break  # 说明大事不妙

        # print("node_closest", node_closest)
        left_or_right[node_closest] = True

        # 接下来根据新加进来的点，更新右边的dist_from_c1
        for i in range(map_now.n):
            if not left_or_right[i]:
                dist_now = dist_from_c1[i]
                dist_new = dist_from_c1[node_closest] + map_now.dist[node_closest][i]
                if dist_from_c1[node_closest] == -1 or map_now.dist[node_closest][i] == -1:
                    dist_new = -1
                    # 正无穷，不做更新
                else:
                    if dist_now > dist_new or dist_now == -1:
                        dist_from_c1[i] = dist_new

    ans_now.shortest_dist = dist_from_c1[c2]
    ans_now.dist_from_c1 = dist_from_c1
    # for i in range(map_.n):
    #     print(dist_from_c1[i])
    pass


def do_dfs(map_now, c1, c2, ans_now, total_dist_now, total_n_teams):
    # print(c1,c2,total_dist_now,total_n_teams)
    for node_next in range(map_now.n):
        if c1 != node_next:
            # print("node_next",node_next)
            total_dist_next = total_dist_now + map_now.dist[c1][node_next]
            if map_now.dist[c1][node_next] == -1 or total_dist_now == -1:
                total_dist_next = -1
            total_n_teams_new = total_n_teams + map_.n_teams_by_city[node_next]
            # print(total_dist_next, ans_now.dist_from_c1[node_next])
            if total_dist_next == ans_now.dist_from_c1[node_next] and total_dist_next != -1:
                if c2 == node_next:
                    ans_now.num_paths += 1
                    if total_n_teams_new > ans_now.n_teams_max:
                        ans_now.n_teams_max = total_n_teams_new
                    pass
                else:
                    do_dfs(map_now, node_next, c2, ans_now, total_dist_next, total_n_teams_new)
    pass


map_ = MyMap()
q = Question()
do_input(map_, q)
ans = Ans()
do_dijkstra(map_, q.c1, q.c2, ans)
# for i in range(map_.n):
#     print(ans.dist_from_c1[i])
do_dfs(map_, q.c1, q.c2, ans, 0, map_.n_teams_by_city[q.c1])
if q.c1 == q.c2:
    ans.num_paths = 1
    ans.n_teams_max = map_.n_teams_by_city[q.c1]
print(ans.num_paths, ans.n_teams_max)

