T = int(input())
for _ in range(T):
    cube = [
        [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)
    ]
    U = cube[1][1]
    D = cube[3][1]
    F = cube[2][1]
    B = cube[0][1]
    L = cube[1][0]
    R = cube[1][2]
    for i in range(3):
        for j in range(3):
            U[i][j] = "w"
            D[i][j] = "y"
            F[i][j] = "r"
            B[i][j] = "o"
            L[i][j] = "g"
            R[i][j] = "b"

    def rotate(face, dir):
        global U, D, F, B, L, R
        if face == "U":
            if dir == "+":
                U = list(map(list, zip(*U[::-1])))
            else:
                U = list(map(list, zip(*U)))[::-1]
        elif face == "D":
            if dir == "+":
                D = list(map(list, zip(*D[::-1])))
            else:
                D = list(map(list, zip(*D)))[::-1]
        elif face == "F":
            if dir == "+":
                F = list(map(list, zip(*F[::-1])))
            else:
                F = list(map(list, zip(*F)))[::-1]
        elif face == "B":
            if dir == "+":
                B = list(map(list, zip(*B[::-1])))
            else:
                B = list(map(list, zip(*B)))[::-1]
        elif face == "L":
            if dir == "+":
                L = list(map(list, zip(*L[::-1])))
            else:
                L = list(map(list, zip(*L)))[::-1]
        elif face == "R":
            if dir == "+":
                R = list(map(list, zip(*R[::-1])))
            else:
                R = list(map(list, zip(*R)))[::-1]

        rotate_side(face, dir)

    def rotate_side(face, dir):
        W = X = Y = Z = None
        # if dir == '+':
        #     W, X, Y, Z = Z, W, X, Y
        #   else:
        #     W, X, Y, Z = X, Y, Z, W
        if face == "U":
            W = [B[0][2], B[0][1], B[0][0]]
            X = [R[0][2], R[0][1], R[0][0]]
            Y = [F[0][2], F[0][1], F[0][0]]
            Z = [L[0][2], L[0][1], L[0][0]]
            for i in range(3):
                B[0][i], R[0][i], F[0][i], L[0][i] = (
                    L[0][i],
                    B[0][i],
                    R[0][i],
                    F[0][i],
                )
            if dir != "+":
                # W, X, Y, Z = Z, W, X, Y
                for i in range(3):
                    B[0][i], R[0][i], F[0][i], L[0][i] = (
                        L[0][i],
                        B[0][i],
                        R[0][i],
                        F[0][i],
                    )
                for i in range(3):
                    B[0][i], R[0][i], F[0][i], L[0][i] = (
                        L[0][i],
                        B[0][i],
                        R[0][i],
                        F[0][i],
                    )
        elif face == "D":
            W = [F[2][0], F[2][1], F[2][2]]
            X = [R[2][0], R[2][1], R[2][2]]
            Y = [B[2][0], B[2][1], B[2][2]]
            Z = [L[2][0], L[2][1], L[2][2]]
            for i in range(3):
                F[2][i], R[2][i], B[2][i], L[2][i] = (
                    L[2][i],
                    F[2][i],
                    R[2][i],
                    B[2][i],
                )
            if dir != "+":
                for i in range(3):
                    F[2][i], R[2][i], B[2][i], L[2][i] = (
                        L[2][i],
                        F[2][i],
                        R[2][i],
                        B[2][i],
                    )
                for i in range(3):
                    F[2][i], R[2][i], B[2][i], L[2][i] = (
                        L[2][i],
                        F[2][i],
                        R[2][i],
                        B[2][i],
                    )
        elif face == "F":
            W = [U[2][0], U[2][1], U[2][2]]
            X = [R[0][0], R[1][0], R[2][0]]
            Y = [D[0][2], D[0][1], D[0][0]]
            Z = [L[2][2], L[1][2], L[0][2]]

            # W, X, Y, Z = Z, W, X, Y
            for i in range(3):
                U[2][i], R[i][0], D[0][2 - i], L[2 - i][2] = (
                    L[2 - i][2],
                    U[2][i],
                    R[i][0],
                    D[0][2 - i],
                )
            if dir != "+":
                for i in range(3):
                    U[2][i], R[i][0], D[0][2 - i], L[2 - i][2] = (
                        L[2 - i][2],
                        U[2][i],
                        R[i][0],
                        D[0][2 - i],
                    )
                for i in range(3):
                    U[2][i], R[i][0], D[0][2 - i], L[2 - i][2] = (
                        L[2 - i][2],
                        U[2][i],
                        R[i][0],
                        D[0][2 - i],
                    )
        elif face == "B":
            W = [U[0][2], U[0][1], U[0][0]]
            X = [L[0][0], L[1][0], L[2][0]]
            Y = [D[2][0], D[2][1], D[2][2]]
            Z = [R[2][2], R[1][2], R[0][2]]
            # W, X, Y, Z = Z, W, X, Y
            for i in range(3):
                U[0][2 - i], L[i][0], D[2][i], R[2 - i][2] = (
                    R[2 - i][2],
                    U[0][2 - i],
                    L[i][0],
                    D[2][i],
                )
            if dir != "+":
                for i in range(3):
                    U[0][2 - i], L[i][0], D[2][i], R[2 - i][2] = (
                        R[2 - i][2],
                        U[0][2 - i],
                        L[i][0],
                        D[2][i],
                    )
                for i in range(3):
                    U[0][2 - i], L[i][0], D[2][i], R[2 - i][2] = (
                        R[2 - i][2],
                        U[0][2 - i],
                        L[i][0],
                        D[2][i],
                    )

        elif face == "L":
            W = [U[0][0], U[1][0], U[2][0]]
            X = [F[0][0], F[1][0], F[2][0]]
            Y = [D[0][0], D[1][0], D[2][0]]
            Z = [B[2][2], B[1][2], B[0][2]]
            # W, X, Y, Z = Z, W, X, Y
            for i in range(3):
                U[i][0], F[i][0], D[i][0], B[2 - i][2] = (
                    B[2 - i][2],
                    U[i][0],
                    F[i][0],
                    D[i][0],
                )
            if dir != "+":
                for i in range(3):
                    U[i][0], F[i][0], D[i][0], B[2 - i][2] = (
                        B[2 - i][2],
                        U[i][0],
                        F[i][0],
                        D[i][0],
                    )
                for i in range(3):
                    U[i][0], F[i][0], D[i][0], B[2 - i][2] = (
                        B[2 - i][2],
                        U[i][0],
                        F[i][0],
                        D[i][0],
                    )
        elif face == "R":
            W = [U[2][2], U[1][2], U[0][2]]
            X = [B[0][0], B[1][0], B[2][0]]
            Y = [D[2][2], D[1][2], D[0][2]]
            Z = [F[2][2], F[1][2], F[0][2]]
            # W, X, Y, Z = Z, W, X, Y
            for i in range(3):
                U[2 - i][2], B[i][0], D[2 - i][2], F[2 - i][2] = (
                    F[2 - i][2],
                    U[2 - i][2],
                    B[i][0],
                    D[2 - i][2],
                )
            if dir != "+":
                for i in range(3):
                    U[2 - i][2], B[i][0], D[2 - i][2], F[2 - i][2] = (
                        F[2 - i][2],
                        U[2 - i][2],
                        B[i][0],
                        D[2 - i][2],
                    )
                for i in range(3):
                    U[2 - i][2], B[i][0], D[2 - i][2], F[2 - i][2] = (
                        F[2 - i][2],
                        U[2 - i][2],
                        B[i][0],
                        D[2 - i][2],
                    )

    n = int(input())
    cmds = list(input().rstrip().split())
    for cmd in cmds:
        face, dir = cmd
        rotate(face, dir)
    for line in U:
        print("".join(line))
