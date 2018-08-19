import BT2.Task

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
