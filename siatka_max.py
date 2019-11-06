import numpy as np

funkcja = lambda x, y: 2*x**2-3*y


def siatka(nx=8, ny=8):
    A = np.zeros((nx, ny))

    for i in range(nx):
        for j in range(ny):
            A[i, j] = funkcja(i, j)

    for i in range(nx):
        for j in range(ny):
            if A[i, j] == np.amax(A):
                b = i + 1
                a = j + 1
                break
            else:
                continue

    print("Wartość maksymalna funkcji wynosi {}, w punkcie siatki {},{}".format(np.amax(A), a, b))
    print(A)

if __name__ == '__main__':
    siatka(12, 7)
