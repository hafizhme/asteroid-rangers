from math import sqrt, pow


def jarak_3(a, b):
    return sqrt(
        pow(a[0] - b[0], 2)
        + pow(a[1] - b[1], 2)
        + pow(a[2] - b[2], 2)
    )


def cepat(a,s):
    a[0] += a[3] * s
    a[1] += a[4] * s
    a[2] += a[5] * s
    return a


def ada_sirkuit(T, u, x, y):
    t = len(T)
    if x not in T:
        t += 1
    if y not in T:
        t += 1
    if t - 2 == u:
        return False
    return True


def buat_tree(G):
    n = len(G)
    T = {}
    x, y = None, None
    for a in G:
        for b in G[a]:
            try:
                if x is not None and y is not None:
                    if G[a][b] < G[x][y]:
                        if not ada_sirkuit(T, 0, a, b):
                            x = a
                            y = b
                else:
                    buf = G[a][b]
                    # print(a,b,x,y)
                    if not ada_sirkuit(T, 0, x, y):
                        x = a
                        y = b
            except KeyError:
                pass
            # print(a, b, x, y)

    # print('init')
    # print(' ', G)
    # print(' ', T)
    xy = G[x].pop(y)
    yx = G[y].pop(x)
    T[x] = {y: xy}
    T[y] = {x: yx}

    for u in range(1, n - 1):
        # print(u)
        # print(' ', G)
        # print(' ', T)

        # cari yang paling kecil dan bersisian
        x, y = None, None
        for a in T:
            for b in G:
                try:
                    if x is not None and y is not None:
                        if G[a][b] < G[x][y]:
                            if not ada_sirkuit(T, u, a, b):
                                x = a
                                y = b
                    else:
                        buf = G[a][b]
                        if not ada_sirkuit(T, u, a, b):
                            x = a
                            y = b
                except KeyError:
                    pass

        # masukkan hasil
        xy = G[x].pop(y)
        yx = G[y].pop(x)
        try:
            T[x][y] = xy
        except KeyError:
            T[x] = {y: xy}

        try:
            T[y][x] = yx
        except KeyError:
            T[y] = {x: yx}

    # print(G)
    return T


def t_equal(T1, T2):
    if T1.keys() != T2.keys():
        return False

    for k in T1:
        if T1[k].keys() != T2[k].keys():
            return False

    return True
