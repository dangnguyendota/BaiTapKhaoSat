# encoding: utf-8
# module Task
"""
Bài tập 5
Tạo ngày: 19/8/2018 10:00PM
Bởi: Nguyễn Đăng Nguyên
Đề bài: Cho một con xúc xắc có 6 mặt được đánh số từ 1 đến 6. Viết chương trình tính giá trị xấp xỉ của
xác xuất tổng của 5 lần tung liên tiếp bằng 17.
Bài làm: Cho nó tự gieo 5 lần xong tính tổng nếu bằng 17 thì cộng lại. Làm giả lập như thế 1 triệu lần, tính số lần có tổng bằng 17.
"""

import numpy as np

def _xs(count, total):
    """
    Tính xác suất tung đồng xu n lần có tổng các mặt bằng m.
    :param count: số lần tung.
    :param total: tổng kỳ vọng.
    :return:
    """
    _t = 0
    for i in range(1000000):
        _tmp = np.random.randint(1, 6, size=count)
        if np.sum(_tmp) == total:
            _t+=1
    return _t/1000000