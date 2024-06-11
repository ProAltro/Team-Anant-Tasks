import numpy as np, random
from task_2 import attitude_matrix


def euler_axis_angle(A):
    tr = A.trace()
    v = np.arccos((tr - 1) / 2)

    e = np.array(
        [A[2, 1] - A[1, 2], A[0, 2] - A[2, 0], A[1, 0] - A[0, 1]]
    )  # (You'll get 2sin(v) * e)
    e = e / np.linalg.norm(e)

    return e, v


if __name__ == "__main__":
    A = []
    print("Enter the matrix:")
    for i in range(3):
        A.append(list(map(float, input().split())))
    A = np.array(A)

    e, v = euler_axis_angle(A)
    print("Euler's axis is: ", e)
    print("Angle of rotation is: ", np.degrees(v))

    # Sanity check
    random_e = np.array([random.random(), random.random(), random.random()])
    random_e = random_e / np.linalg.norm(random_e)
    random_v = np.radians(random.randint(0, 180))
    e, v = euler_axis_angle(attitude_matrix(random_e, random_v))

    assert np.allclose(random_e, e, atol=1e-5)
    assert np.allclose(random_v, v, atol=1e-5)
    print("Sanity check passed!")
