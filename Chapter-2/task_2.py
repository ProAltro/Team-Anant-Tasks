import numpy as np
from task_1 import cross_product_matrix


def attitude_matrix(e, v):
    ec = cross_product_matrix(e)
    att_mat = np.cos(v) * np.eye(3) + np.sin(v) * ec + (1 - np.cos(v)) * np.outer(e, e)
    return att_mat


if __name__ == "__main__":
    e = input("Enter axis of rotation (sep by space): ")
    e = list(map(int, e.split()))
    e = np.array(e) / np.linalg.norm(e)

    v = np.radians(int(input("Angle of rotation (in degrees): ")))

    attitude = attitude_matrix(e, v)
    print("Attitude matrix is: \n", attitude)
