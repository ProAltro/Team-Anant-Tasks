import numpy as np
from task_3 import euler_axis_angle
from task_4 import quaternion
from task_6 import quaternion_to_matrix
from task_2 import attitude_matrix


def matrix_to_quaternion(A):
    e, v = euler_axis_angle(A)
    return quaternion(e, v)


if __name__ == "__main__":
    A = []
    print("Enter the matrix:")
    for i in range(3):
        A.append(list(map(float, input().split())))
    A = np.array(A) / np.linalg.norm(A)

    q = matrix_to_quaternion(A)
    print("Quaternion is: ", q)

    # Sanity check
    random_e = np.array([np.random.random(), np.random.random(), np.random.random()])
    random_e = random_e / np.linalg.norm(random_e)
    random_v = np.radians(np.random.randint(0, 180))
    q = matrix_to_quaternion(attitude_matrix(random_e, random_v))

    assert np.allclose(
        attitude_matrix(random_e, random_v),
        quaternion_to_matrix(quaternion(random_e, random_v)),
        atol=1e-5,
    )
    print("Sanity check passed!")
