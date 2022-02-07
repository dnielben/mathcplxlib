from typing import List, Tuple

import mathcplx as lc


def sumavec(v, w):
    tamano = len(v)
    # inicializar suma del tamano correcto
    suma = [(0, 0) for i in range(tamano)]
    j = 0
    # recorrer v y w sumando elemento por element
    # OJO, para sumar use sumacplx(c1,c2)
    while j < tamano:
        suma[j] = lc.sumacplx(v[j], w[j])
        j = j + 1
    # retornar suma que es un vector
    return suma


def multscalar(c, v):
    tamano = len(v)
    # inicializar mult del tamano correcto
    mult = [(0, 0) for i in range(tamano)]
    j = 0
    # recorrer v multiplicando c por elemento
    # OJO, para mult escalar use multcplx(c1,c2)
    while j < tamano:
        mult[j] = lc.multcplx(c, v[j])
        j = j + 1
    # retornar mult que es un vector
    return mult

def multmatrix(A,B):
    sizeAm = len(A)
    sizeAn = len(A[0])
    sizeBm = len(B)
    sizeBn = len(A[0])

    sizeRes_m = sizeAm
    sizeRes_n = sizeBn

    if sizeAn != sizeBm:
        raise Exception('Incompatible sizes')

    # inicializar mresult del tamano correcto
    result = [[(0, 0) for i in range(sizeRes_n)] for j in range(sizeRes_m)]

    j = 0
    # recorrer A  y B multiplicando
    while j < sizeRes_m:
        k = 0
        while k < sizeRes_n:
            h = 0
            while h < sizeAn:
                result[j][k] = lc.sumacplx(result[j][k], lc.multcplx(A[j][h], B[h][k]))
                h = h + 1
            k= k + 1
        j = j + 1
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test with vectors
    v = [(3, 7), (8, 9), (3.4, -7.8)]
    w = [(5, 6), (6, 8), (0, 0)]
    print(sumavec(v, w))
    print(multscalar((2, 3), w))

    # test with matrices
    A = [[(0,3), (2,5)], [(1,-3), (1,-5)]]
    B = [[(1,2), (2,-5)], [(0,3), (1,4)]]
    print(A)
    print(B)
    # Verify in wolfran web using the following expr.:
    # [[3i,2+5i],[1-3i,1-5i]] * [[1+2i,2-5i],[3i,1+4i]]
    print(multmatrix(A, B)) # result: [[(-21, 9), (-3, 19)], [(22, 2), (8, -12)]]
