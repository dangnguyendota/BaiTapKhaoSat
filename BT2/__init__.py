import BT2.Task

__author__ = "Nguyễn Đăng Nguyên"
__class__= "KSTN-CNTT-K60"
__school__= "Đại học BKHN"

class Point(Task.Point):
    """
    Call sang bên file BT2\Task
    """
    def __init__(self, x, y, z):
        Task.Point.__init__(self, x, y, z)


def projection(d: Point, a: Point, b: Point, c: Point):
    """
    Call sang bên file BT2\Task
    """
    return Task._projectionAPointAnd3Points(d, a, b, c)
