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


map_ = MyMap()
q = Question()
do_input(map_, q)

