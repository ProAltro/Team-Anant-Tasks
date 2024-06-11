import numpy as np
from task_2 import attitude_matrix
from task_4 import quaternion
from task_2 import cross_product_matrix


def quaternion_to_matrix(q):
    a, b = q
    A = (
        (b**2 - np.dot(a, a)) * np.eye(3)
        - 2 * b * cross_product_matrix(a)
        + 2 * np.outer(a, a)
    )

    return A.T


if __name__ == "__main__":
    q = list(map(float, input("Enter quaternion (sep by space): ").split()))
    a, b = np.array(q[:3]), q[3]
    b = np.cos(b / 2)
    a = a * np.sin(b / 2) / np.linalg.norm(a)
    q = [a, b]

    q_matrix = quaternion_to_matrix(q)
    print("Quaternion to matrix is: \n", q_matrix)

    # Sanity check
    random_e = np.array([np.random.random(), np.random.random(), np.random.random()])
    random_e = random_e / np.linalg.norm(random_e)
    random_v = np.radians(np.random.randint(0, 180))
    q_matrix = quaternion_to_matrix(quaternion(random_e, random_v))

    print(attitude_matrix(random_e, random_v))
    print(q_matrix)
    assert np.allclose(attitude_matrix(random_e, random_v), q_matrix, atol=1e-5)
    print("Sanity check passed!")
