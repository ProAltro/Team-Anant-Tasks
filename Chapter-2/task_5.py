import numpy as np
from task_4 import quaternion
from task_1 import cross_product_matrix


def q_cross(q):
    a, b = q
    psi = [b * np.eye(3) + cross_product_matrix(a), -a.T]
    psi = np.vstack(psi)
    n = np.array([[*a, b]]).T
    q_cross = np.hstack([psi, n])
    return q_cross


def q_cross_prod(q1, q2):
    q1 = q_cross(q1)
    a, b = q2
    q2 = np.array([*a, b]).T

    q_cross_prod = q1 @ q2
    a, b = q_cross_prod[:3], q_cross_prod[3]
    return [a, b]


def q_dot(q):
    a, b = q
    q_dot = [[-b * np.eye(3) + cross_product_matrix(a), -a], [-a.T, 0]]
    return q_dot


def q_inv(q):
    a, b = q
    norm_q = np.linalg.norm([np.linalg.norm(a), b])
    norm_q = norm_q**2
    q_inv = [-a / norm_q, b / norm_q]
    return q_inv


if __name__ == "__main__":
    q = list(map(float, input("Enter quaternion (sep by space): ").split()))
    q = [np.array(q[:3]), q[3]]

    q_cross_ = q_cross(q)
    q_dot_ = q_dot(q)
    q_inv_ = q_inv(q)

    print("Quaternion is: ", q)
    print("Quaternion cross is: ", q_cross_)
    print("Quaternion dot is: ", q_dot_)
    print("Quaternion inverse is: ", q_inv_)

    # Sanity check inversion
    q_inv_inv = q_inv(q_inv_)
    a, b = q
    a_ii, b_ii = q_inv_inv
    assert np.allclose(a, a_ii, atol=1e-5)
    assert np.allclose(b, b_ii, atol=1e-5)
    print("Sanity check passed!")
