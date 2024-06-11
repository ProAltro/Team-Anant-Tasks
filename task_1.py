import numpy as np


def cross_product_matrix(v):
    vc = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    return vc


if __name__ == "__main__":
    v = list(map(int, input("Enter vector elements seperated by space: ").split()))
    v = np.array(v)

    v_cross = cross_product_matrix(v)
    print("Cross product of vector is: \n", v_cross)
