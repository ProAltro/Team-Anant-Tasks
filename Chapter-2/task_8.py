import numpy as np
from task_2 import attitude_matrix
from task_4 import quaternion
from task_5 import q_cross_prod as q_cross
from task_6 import quaternion_to_matrix


def euler_angles(phi, theta, psi):
    e1 = np.array([1, 0, 0])
    e2 = np.array([0, 1, 0])
    e3 = np.array([0, 0, 1])

    q = q_cross(
        q_cross(quaternion(e1, phi), quaternion(e2, theta)), quaternion(e3, psi)
    )
    A = attitude_matrix(e1, phi) @ attitude_matrix(e2, theta) @ attitude_matrix(e3, psi)

    return q, A


if __name__ == "__main__":
    phi, theta, psi = map(float, input("Enter euler angles (sep by space): ").split())
    q, A = euler_angles(np.radians(phi), np.radians(theta), np.radians(psi))
    print("Quaternion is: ", q)
    print("Attitude matrix is: \n", A)

    # Sanity check
    random_e = np.array([np.random.random(), np.random.random(), np.random.random()])
    random_e = random_e / np.linalg.norm(random_e)
    random_v = np.radians(np.random.randint(0, 180))
    q, A = euler_angles(random_v, random_v, random_v)

    assert np.allclose(A, quaternion_to_matrix(q), atol=1e-5)
    print("Sanity check passed!")
