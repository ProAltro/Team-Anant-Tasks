import numpy


def quaternion(e, v):
    q = [e * numpy.sin(v / 2), numpy.cos(v / 2)]
    return q


if __name__ == "__main__":
    e = input("Enter axis of rotation (sep by space): ")
    e = list(map(int, e.split()))
    e = numpy.array(e) / numpy.linalg.norm(e)
    v = numpy.radians(int(input("Angle of rotation (in degrees): ")))
    q = quaternion(e, v)
    print("Quaternion is: ", q)
