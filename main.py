import time

from usefull import cepat, jarak_3, buat_tree, t_equal

try:
    t = 1
    while True:
        n = int(input())
        A = []

        for i in range(n):
            x, y, z, vx, vy, vz = map(int, input().split(' '))
            A.append([x, y, z, vx, vy, vz])

        # print('INITIAL CONDITION ---------')
        # print('posisi asteroid')
        # for i in range(int(len(A))):
        #     print('  asteroid', i, ':', A[i][0], A[i][1], A[i][2],
        #           '  dengan kecepatan :', A[i][3], A[i][4], A[i][5])
        # print()
        # print()
        # print()
        # print()
        # print()

        counter = 0
        buf = None
        hitungan = 0
        start = time.time()
        while True:
            # print(hitungan,'---------------------------------------------------------')
            # cari jarak ke tiap tiap titik
            if hitungan > 0:
                for i in range(len(A)):
                    A[i] = cepat(A[i], 0.1)

            # print('posisi')
            # for i in range(int(len(A))):
            #     print('  asteroid', i, ':', A[i][0], A[i][1], A[i][2],
            #           '  dengan kecepatan :', A[i][3], A[i][4], A[i][5])
            # print()

            G = {}
            for i in range(n):
                G[i] = {}
                for j in range(n):
                    if i is not j:
                        # G[i][j] = float("{0:.2f}".format(jarak_3(A[i], A[j])))
                        G[i][j] = jarak_3(A[i], A[j])

            # print('Graph dengan jarak')
            # for i in G:
            #     print('  ', i, G[i])
            # print()
            # masukkan data tersebut ke algoritma prim
            T = buat_tree(G)

            # print('Tree yang dihasilkan')
            # for i in T:
            #     print('  ', i, T[i])
            # print()

            if buf:
                if t_equal(T, buf):
                    # tidak switch
                    pass
                else:
                    # switch
                    counter += 1
                    buf = T
                    # print(T, buf)
                    # print('   SWITCH', hitungan - 1)
            else:
                counter += 1
                buf = T
                # print('   SWITCH', hitungan-1)

                # start = time.time()
                # while True:
                #     if time.time() - start > 0.5:
                #         break

            hitungan += 1

            if time.time() - start > 0.00000001:
                break
        # input()
        # print()
        # print()
        # print()
        # print()

        # print(counter)

        print("Case %d: %d" % (t, counter))

        t += 1
except EOFError:
    pass