# Suma de complejos.
def sumacplx(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])

def multcplx(c1,c2):
    real = (c1[0] * c2[0]) - (c1[1] * c2[1])
    img  = (c1[0] * c2[1]) + (c1[1] * c2[0])
    return (real, img)

def divcplx(c1,c2):
    real = ((c1[0] * c2[0]) + (c1[1] * c2[1])) / ((c2[0] ** 2) + (c2[1] ** 2))
    imag = ((c2[0] * c1[1]) - (c1[0] * c2[1])) / ((c2[0] ** 2) + (c2[1] ** 2))
    return (real, imag)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sumacplx((3.5, 7), (4.2, 8)))  # (3.5 + 7i) + (4.2 + 8i) = (7.7 + 15i)
    print(multcplx((3, 7), (4, 8)))  # (3 + 7i) * (4 + 8i) = (-44 + 52i)
    print(divcplx((-2, 1), (1, 2)))  # (-2 + 1i) / (1 + 2i) = (0,1)


