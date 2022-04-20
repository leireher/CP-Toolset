# Gauss-Jordan elimination with full pivoting.
# Uses:
#   (1) solving systems of linear equations (AX=B)
#   (2) inverting matrices (AX=I)
#   (3) computing determinants of square matrices
# Running time: O(n^3)
# INPUT:    a[][] = an nxn matrix
#           b[][] = an nxm matrix
# OUTPUT:   X      = an nxm matrix (stored in b[][])
#           A^{-1} = an nxn matrix (stored in a[][])
#           returns determinant of a[][]

import sys
EPS = 1e-10

def GaussJordan(a, b):
    n, m = len(a), len(b[0])
    irow, icol, ipiv = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]
    det = 1.

    for i in range(n):
        pj, pk = -1, -1
        for j in range(n):
            if ipiv[j] == 0:
                for k in range(n):
                    if ipiv[k] == 0 and (pj == -1 or abs(a[j][k]) > abs(a[pj][pk])):
                        pj, pk = j, k

        if abs(a[pj][pk]) < EPS:
            print("Matrix is singular.", file=sys.stderr)
            sys.exit(1)

        ipiv[pk] += 1
        a[pj], a[pk] = a[pk], a[pj]
        b[pj], b[pk] = b[pk], b[pj]

        if pj != pk:
            det *= -1

        irow[i], icol[i] = pj, pk

        c = 1.0 / a[pk][pk]
        det *= a[pk][pk]
        a[pk][pk] = 1.0

        for p in range(n):
            a[pk][p] *= c

        for p in range(m):
            b[pk][p] *= c

        for p in range(n):
            if p != pk:
                c = a[p][pk]
                a[p][pk] = 0
                for q in range(n):
                    a[p][q] -= a[pk][q] * c

                for q in range(m):
                    b[p][q] -= b[pk][q] * c

    for p in reversed(range(n)):
        if irow[p] != icol[p]:
            for k in range(n):
                a[k][irow[p]], a[k][icol[p]] = a[k][icol[p]], a[k][irow[p]]

    return det
