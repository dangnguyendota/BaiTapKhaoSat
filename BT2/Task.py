# encoding: utf-8
# module Task
"""
Bài tập 2
Tạo ngày: 19/8/2018 10:20PM
Bởi: Nguyễn Đăng Nguyên
Đề bài: Cho 3 điểm 𝑎, 𝑏, 𝑐 trong không gian 3 chiều với tọa độ (2, 4, 5), (4, 7, 9), (7, 9, 2). Viết chương
trình tìm hình chiếu của điểm 𝑑 với tọa độ (30, 25, 56) trên mặt phẳng tạo bởi ba điểm 𝑎, 𝑏, c.
Bài làm: Sử dụng công thức d = (30 + A*t, 25 + B*t, 56 + C*t) với (A, B, C) là vector pháp tuyến của mặt phẳng ABC.
"""


class Point:
    """
    Lớp Point biểu diễn 1 điểm trong không gian Oxyz.
    """

    def __init__(self, x, y, z):
        """
        Đầu vào của lớp point là tọa độ của điểm đó.
        :param x: tọa độ x
        :param y: tọa độ y
        :param z: tọa độ z
        """
        self.x = x
        self.y = y
        self.z = z

    def toString(self):
        """
        Phương thức này trả về 1 chuỗi biểu diễn thông tin của điểm.
        :return:
        """
        return "Point(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"


class Vector3:
    """
    Lớp Vector3 biểu diễn 1 vector trong không gian Oxyz.
    """

    def __init__(self, x, y, z):
        """
        Đầu vào của lớp Vector3 là thông tin của vector đó.
        :param x: Độ dài hình chiếu trên trục Ox.
        :param y: Độ dài hình chiếu trên trục Oy.
        :param z: Độ dài hình chiếu trên trục Oz.
        """
        self.x = x
        self.y = y
        self.z = z

    def toString(self):
        """
        Phương thức này trả về 1 chuỗi biểu diễn thông tin của vector.
        :return:
        """
        return "Vector(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"


class Plane:
    """
    Lớp Plane biểu diễn 1 mặt phẳng trong không gian Oxyz.
    1 mặt phẳng được biểu diễn bởi phương trình: A(x - x0) + B(y-y0) + C(z-z0) = 0
    """
    def __init__(self, A, B, C, x0, y0, z0):
        """
        Đầu vào của lớp Plane là thông tin về phương trình của mặt phẳng đó.
        A(x - x0) + B(y-y0) + C(z-z0) = 0.
        :param A:
        :param B:
        :param C:
        :param x0:
        :param y0:
        :param z0:
        """
        self.A = A
        self.B = B
        self.C = C
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0

    def toString(self):
        """
        Phương thức này trả về 1 chuỗi biểu diễn thông tin của mặt phẳng.
        :return:
        """
        return ("Plane(" + str(self.A) + ".(x - " + str(self.x0) + ")  + " + str(self.B) + ".(y - " + str(
            self.y0) + ") + " + str(
            self.C) + ".(z - " + str(self.z0) + ") = 0)")


def _Vector3From2Points(point1: Point, point2: Point):
    """
    Trả về 1 vector có giá là đường thẳng đi qua 2 điểm point1 và point2.
    :param point1: điểm thứ nhất.
    :param point2: điểm thứ hai.
    :return: Vector3
    """
    x = point1.x - point2.x
    y = point1.y - point2.y
    z = point1.z - point2.z
    return Vector3(x, y, z)


def _normalFrom2Vectors(vector1: Vector3, vector2: Vector3):
    """
    Trả về vector vuông góc với 2 vector vector1 và vector2.
    :param vector1:
    :param vector2:
    :return: Vector3()
    """
    return Vector3(vector1.y * vector2.z - vector1.z * vector2.y, vector1.z * vector2.x - vector1.x * vector2.z,
                   vector1.x * vector2.y - vector1.y * vector2.x)


def _normalFrom3Points(point1: Point, point2: Point, point3: Point):
    """
    Trả về vector pháp tuyến của mặt phẳng đi qua 3 điểm point1, point2, point3.
    :param point1:
    :param point2:
    :param point3:
    :return: Vector3().
    """
    return _normalFrom2Vectors(_Vector3From2Points(point1, point2), _Vector3From2Points(point2, point3))


def _planeFromANormalAPoint(normal: Vector3, point: Point):
    """
    Trả về mặt phẳng đi qua điểm point và có vector pháp tuyến normal.
    :param normal: Vector pháp tuyến của mặt phẳng.
    :param point: Điểm nằm trên mặt phẳng.
    :return: Plane().
    """
    return Plane(normal.x, normal.y, normal.z, point.x, point.y, point.z)


def _planeFrom3Points(point1: Point, point2: Point, point3: Point):
    """
    Trả về mặt phẳng đi qua 3 điểm.
    :param point1: điểm 1.
    :param point2:  điểm 2.
    :param point3: điểm 3.
    :return: Plane()
    """
    normal = _normalFrom3Points(point1, point2, point3)
    return _planeFromANormalAPoint(normal, point3)


def _projectionWithAPointAndAPlane(point: Point, plane: Plane):
    """
    Trả về hình chiếu của 1 điểm trên một mặt phẳng.
    :param point: điểm.
    :param plane: mặt phẳng.
    :return: Point()
    """
    _t = (plane.A * (plane.x0 - point.x) + plane.B * (plane.y0 - point.y) + plane.C * (plane.z0 - point.z)) / (
            plane.A ** 2 + plane.B ** 2 + plane.C ** 2)
    return Point(point.x + plane.A * _t, point.y + plane.B * _t, point.z + plane.C * _t)


def _projectionAPointAnd3Points(inputPoint: Point, point1: Point, point2: Point, point3: Point):
    """
    Trả về hình chiếu của điểm lên một mặt phẳng đi qua 3 điểm khác.
    :param inputPoint: điểm cần tìm hình chiếu.
    :param point1: điểm nằm trên mặt phẳng 1.
    :param point2: điểm nằm trên mặt phẳng 2.
    :param point3: điểm nằm trên mặt phẳng 3.
    :return: Point()
    """
    _plane = _planeFrom3Points(point1, point2, point3)
    return _projectionWithAPointAndAPlane(inputPoint, _plane)
